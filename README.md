# mybrew

![Python tests and lints status](https://github.com/jacobcallear/mybrew/workflows/tests/badge.svg)

Intuitive command-line interface for a cafe database.

Add people, drinks, preferences, and rounds to a MySQL database without writing
complicated SQL queries.

## Demo

1. Open a terminal and enter `python -m mybrew`

2. Enter your MySQL password - the required database and tables are
   automatically set up for you

![Screen recording of mybrew starting in terminal](/img/startup.gif)

3. You are now in the `mybrew` CLI! Use the `help` command to list options

![Screenshot of mybrew help command output](/img/help.png)

4. Auto-completion and suggestions will help you get the hang of `mybrew`

![Screen recording of mybrew command auto-suggestion](/img/auto-suggestion.gif)

## Installation

1. Ensure you have [Python](https://www.python.org/downloads/) >= 3.6
   and [MySQL](https://www.mysql.com/) installed.
2. [Download](https://github.com/jacobcallear/mybrew/archive/master.zip)
   and unzip this repository
3. Ensure MySQL credentials in *mybrew/credentials.py* are correct
4. In the terminal, `cd` into the `mybrew/mybrew/` folder
5. Run the following command:

   ```bash
   pip install .
   ```

## Trouble Shooting

Can't start `mybrew`? The `python -m mybrew` command (or `py -m mybrew` on
Windows) only works when the `mybrew` folder is on the Python Path. Either add
it to the Python Path, or run the app directly by entering the following
command in the terminal:

```bash
$ cd mybrew
$ python mybrew/app.py
```
