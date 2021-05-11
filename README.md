# Project
## Table of contents

* [Car rental website](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Domain Description](#domain_description)


## Car rental website

There is a website for car rental company (non-commercial)


## Technologies

HTML, CSS, Python 3.8.5, framework Flask, Database MySql Ver 8.0.23-0ubuntu0.20.04.1, git, Flask-RESTful, SQLAlchemy and so on...\
Supporting Programs: Sublime Text 3 - editor with a free evaluation period,
OS - System running Ubuntu Linux,
PyCharm - is an integrated development environment (IDE) used in computer programming, specifically for the Python language 

## Setup
TODO: 
* add mysql
* Flask
* Sqlalchemy
* instructions on how to build a project from the command line 
* how to start it 
* and at what addresses the Web service and the Web application will be available after launch
> The instructions for starting a web site locally on a computer are described for users Linux and OS X

First of all to create and run all the web applications that we will develop throughout, you will need working copies 
of the following software:
*	[The Python Programming Language](https://www.python.org/downloads/)
*	[virtualenv: A tool to create isolated environments for Python packages](https://virtualenv.pypa.io/en/latest/installation.html)
*	[pip: The package manager to install Python packages](https://pip.pypa.io/en/stable/installing/)

You need to find a directory in which you want to create the virtualenv on yours PC.\
I have created a virtualenv called myvenv. The general command is in the format:

```
$ python3 -m venv myvenv
```

Start your virtual environment by running:

```
$ source myvenv/bin/activate
```

After all these steps you need to run "Project" project, install it locally using clone command in terminal or
under the repository name, click Clone or download.
This command copies all the files in a repository to your computer,
and begins tracking them in git. You do this by typing in on the command line:
 
```
$ git clone https://github.com/RadchenkoVlada/Project.git
```
 
Now that you have your virtualenv started, you can install Django.
Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:

```
$ python -m pip install --upgrade pip
```

## Domain Description

My task provide a variety of cars for rent on the site. There are a number of **cars** of various brands in your 
fleet.
------------------------
