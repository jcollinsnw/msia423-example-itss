# Example Flask App

## Objective 
Create the basic skeleton of a web app that connects to, queries, and serves data from a relational database. 

## Package requirements
* [Flask](http://flask.pocoo.org/docs/0.12/)
* [FlaskSQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#a-minimal-application)  
    * A flask plugin for [SQLAlchemy](http://www.sqlalchemy.org/). SQLAlchemy is an Object Relational Mapper (ORM), which means it allows interaction with relational data models using object oriented approaches, like those typically used in python. 
    * This project uses SQLAlchemy to create, read from, and write to relational databases. 
    * SQLAlchemy's flexibility will allow for a smooth transition from using a local database to using something like Amazon RDS. All that needs to change is a configuration in the app code (see [this blog](https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80) for more on transition to RDS)
* [Jinja](http://jinja.pocoo.org/docs/2.10/templates/) for creating HTML templates with Python.
* [PyMySQL](https://github.com/PyMySQL/PyMySQL) for connecting to Amazon RDS
## New additions
* Added view that allows user to input data into the database.


## Components 
* Relational database 
* Data model 
* View(s)
* Templates 
    * HTML 
* Static files
    * CSS
    * JS

## Suggested steps
1. Create conda environment for new app 

    `conda create -n msiapp python=3`
    
2. Activate environment and add Conda Forge channel (if not in channel list yet)

    `source activate msiapp`

    `conda config --add channels conda-forge`

3. Install required packages 

    `conda install flask`
    
    `conda install flask-sqlalchemy`

4. Create directory structure (see repo)
5. Create a config file with the information necessary to create your database connection. **Do not commit this file.** 
You never want to commit files with keys or passwords. The file should look like this: 
     
    ```python
    SECRET_KEY = 'development_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/tracks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ``` 
    The `SECRET_KEY` should be a unique, arbitrary string specific to the application that should be 
    random/difficult to guess - "development_key" is just an example. 
    
    When you create your RDS database, you will change these parameters. 
6. `msiapp/__init__.py` includes the line of code: 

    `application.config.from_envvar('MSIA_SETTINGS', silent=True)`
    
    which tells the application to look at the environmental variable `MSIA_SETTINGS` for the path to your config file. 
    This means you need to set this environmental variable yourself by going to command line and entering:
    
    `export MSIA_SETTINGS="path/to/where/your/config/file/is.config`

6. Define data model (see `msiapp/models.py`) - this can be a placeholder and change as the students better define their project's data needs
7. Create local table with data model and insert some data (see `create_db.py`)
8. Write html template for main page that displays (all or some of the )data from the table in some way. 
    
    Flask uses [`jinja2`](http://jinja.pocoo.org/docs/2.10/templates/) syntax for templates. In it's most basic application, the template is a normal html page but with
    
    `{{ datafield }}`
    
    in the locations where data from the table is wanted. See `msiapp/templates/index.html` for a very basic example 
9. Create a view (see `application.py`) that presents data from the table through html rendered from the `msiapp/templates/index.html` template.

    A view separates the way in which a user interacts with information and the the way that it is manipulated by the app. 
    The "user" in this case can be an actual user interacting through a web page, or it could be a remote application 
    interacting with it through web services. 
10. Get up application running 
    
    If you haven't executed `create_db()` and created your database, from the command line:
    
    `python create_db.py` 
    
    Now run your application: 
    
    `python application.py`
    
    You should be able to go to the IP address that it responds with and see your web app

11. (Optional for now) Add some basic formatting via a CSS file (see `msiapp/static/basic.css`)