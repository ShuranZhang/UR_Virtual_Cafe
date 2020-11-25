To Run the Project
cd to the project directory
python3 -m venv auth
source auth/bin/activate
export FLASK_APP=project
export FLASK_ENV=development
pip install -r requirements.txt
flask run
