###Flask demo-store


#####To setup virtual environment and install:
######To run the project in virtual environment

    virtualenv --python=$(which python3) venv
    source venv/bin/activate
    pip3 install -r requirements.txt
######To run the server
    FLASK_APP=web/app.py flask run
######Author: Akerke Kesha