# Flask Learn App
Our first flask application before we start do world better

### Requirements
* Python3.6+
* pip ~19.03+
* virtualenv

### Setup 
``` $ pip install -r requirements.txt```

To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

``` $ export FLASK_APP=app.py```

If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

``` > set FLASK_APP=app.py```

Run:

``` $ flask run```

### Usage:

URI | Method| Description
--- | --- | --- | 
/users/list | GET | Show all names of users in system
/users/delete/\<username\> | GET | Delete a user by username
/users/add/ | POST | Add new user, check if exist



