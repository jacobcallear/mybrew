'''Defines functions to save/read class instance data into MySQL tables.'''
from textwrap import dedent

import pymysql

# Set MySQL credentials here
CREDENTIALS = {
    'host': 'localhost',
    'user': 'root',
    'port': 3306,
    'password': 'terrorhurtz-18',
    'db': 'mybrew'
}

def read_classes_from_mysql(cls, table, credentials=CREDENTIALS):
    '''Returns list of one class instance for each row in MySQL table.'''
    connection = pymysql.connect(**credentials)
    try:
        # Read table from MySQL
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {table};')
        # Return list of class instances
        classes = []
        while row := cursor.fetchone():
            # Ignore first field (ID)
            classes.append(cls.from_list(row[1:]))
        print(f'Read data from {credentials["db"]}.{table}')
        return classes
    except Exception as e:
        print('Error reading from database')
        print(e)
    finally:
        cursor.close()
        connection.close()

def write_classes_to_mysql(class_list, table, credentials=CREDENTIALS, truncate=False):
    '''Write class instance attributes to a MySQL table.'''
    connection = pymysql.connect(**credentials)
    # List attributes of each class instance
    rows = (cls.to_list() for cls in class_list)
    try:
        cursor = connection.cursor()
        # Get field names
        cursor.execute(dedent(f'''\
            SHOW COLUMNS
            FROM {table}'''))
        fields = (field for field, *_ in cursor.fetchall())
        # Ignore ID field
        next(fields)
        fields = ', '.join(fields)
        # Clear table to avoid duplicating rows
        if truncate:
            cursor.execute(f'TRUNCATE TABLE {table}')
        for row in rows:
            # For each class instance, add attributes to table row
            cursor.execute(dedent(f'''\
                INSERT INTO
                    {table} ({fields})
                VALUES(
                    {to_sql_value_string(row)}
                );'''))
    # Do not change database if a row fails
    except Exception as e:
        print('Error inserting rows')
        print(e)
        connection.rollback()
    # If went smoothly, commit changes
    else:
        connection.commit()
        print(f'Saved data to rounds.{table}')
    finally:
        cursor.close()
        connection.close()

def to_sql_value_string(values):
    '''Converts list of values to a comma-separated SQL string.
    
    Pretty dodgy! Will fail for strings containing quotation marks.
    
    Example:
        >>> values = ['string', 10, True]
        >>> to_sql_value_string(values)
        '"string", 10, 1'
    '''
    output = []
    for i in values:
        # Quote strings
        if isinstance(i, str):
            i = f'"{i}"'
        # Convert bool to tinyint
        elif isinstance(i, bool):
            if i:
                i = 1
            else:
                i = 0
        output.append(str(i))
    return ', '.join(output)