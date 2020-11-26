To Create Database
------------------------------------------------
first enter python interactive
from project import d, create_app
db.create_all(app=create_app())

To Run the Project on Mac
------------------------------------------------
cd to the project directory

python3 -m venv auth

source auth/bin/activate

export FLASK_APP=project

export FLASK_ENV=development

pip install -r requirements.txt

flask run


To Run the Project on Window
------------------------------------------------
cd to the project directory

py -3 -m venv auth

auth\Scripts\activate

set FLASK_APP=project

export FLASK_ENV=development

pip install -r requirements.txt

flask run
