import os
import sys
from code import *


def create(directory):
    try:
        os.makedirs(directory + "/app/templates")
        os.makedirs(directory + "/app/static")
        os.makedirs(directory + "/app/static/css")
    except:
        print("Error")
        exit(0)
    
    with open(directory + "/app/__init__.py", "a") as f:
        f.write(str(a[0]))
    with open(directory + "/app/routes.py", "a") as f:
        f.write(str(a[1]))
    with open(directory + "/app/forms.py", "a") as f:
        f.write(str(a[2]))
    with open(directory + "/blog.py", "a") as f:
        f.write(str(a[3]))
    with open(directory + "/config.py", "a") as f:
        f.write(str(a[4]))
    with open(directory + "/app/models.py", "a") as f:
        f.write(str(a[5]))
    with open(directory + "/requirements.txt", "a") as f:
        f.write(str(a[6]))
    with open(directory + "/app/templates/base.html", "a") as f:
        f.write(str(a[7]))
    with open(directory + "/app/static/css/master.css", "a") as f:
        f.write("")

try:
    directory = input("Enter directory: ")

    if directory:
        create(directory)
    else:
        create(os.getcwd())
except:
    print("Error")