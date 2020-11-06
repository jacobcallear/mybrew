# mybrew

Intuitive command-line interface for a cafe database.

Add people and drinks to a MySQL database, and associate them with each other as
preferences and rounds.

## Set-Up

1. Install [MySQL](https://www.mysql.com/) and
   [Python](https://www.python.org/downloads/)
2. [Download](https://github.com/jacobcallear/mybrew/archive/master.zip)
   or clone this repository
3. Ensure MySQL credentials in *mybrew/credentials.py* are correct
4. Install python requirements
   ```bash
   $ cd mybrew
   $ pip install -r requirements.txt
   ```

## Demo

1. Open a terminal and enter `python -m mybrew`

2. Enter your MySQL password - the required database and tables are
   automatically set up for you

![Animation of mybrew starting in terminal](demo-gifs/startup.gif)

3. You are now in the `mybrew` CLI! Use the `help` command to list options

![Animation of help command in mybrew](demo-gifs/help-command.gif)

4. Auto-completion and suggestions will help you get the hang of `mybrew`

![Animation of auto-completing commands in mybrew](demo-gifs/autocompletion.gif)

## Trouble Shooting

Can't start `mybrew`? The `python -m mybrew` command (or `py -m mybrew` on
Windows) only works when the `mybrew` folder is on the Python Path. Either add
it to the Python Path, or run the app directly by entering the following
command in the terminal:

```bash
$ cd mybrew
$ python mybrew/app.py
```
