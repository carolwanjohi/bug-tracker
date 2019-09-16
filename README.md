### Requirements
* virtual environment
```
Mac
Install virtual environment: sudo pip install virtualenv
Create virtual environment: virtualenv virtual
Enter virtual environment: source virtual/bin/activate
Exit virtual environment: deactivate

Ubuntu

Install virtual environment: sudo python3 -m pip install --user virtualenv
Create virtual environment: python3 -m venv virtual
Enter virtual environment: source virtual/bin/activate
Exit virtual environment: deactivate
```

* install dependancies
```
Enter virtual environment: source virtual/bin/activate
pip install -r requirements.txt
```

* create script for starting the application
```
Create the script: touch start.sh
Add in the script: python3.6 manage.py server
Make script executable: chmod a+x start.sh
Run the script to start the app: ./start.sh 
```

* create `.env` file for saving API creds
```
Create the file: touch .env
Add in th file: TOKEN='<Pivotal_Api_Token>'
```
