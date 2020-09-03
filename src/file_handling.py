'''Defines functions to create class instances from csv files.'''
import csv

def write_classes_to_csv(class_list, file_path):
    '''Writes class instance attributes to a csv.'''
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cls.to_list() for cls in class_list)
    print(f'Saved to {file_path}')

def read_classes_from_csv(cls, file_path):
    '''Returns list of one class instance for each row of a csv.'''
    instances = []
    with open(file_path) as f:
        rows = csv.reader(f)
        for row in rows:
            # Skip blank lines
            if row == '':
                continue
            # Create class instance from csv row
            try:
                instance = cls.from_list(row)
            except ValueError:
                print('Failed to read row')
                continue
            instances.append(instance)
    print(f'Read data from {file_path}')
    return instances