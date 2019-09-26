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

* create [slack webhook](https://api.slack.com/incoming-webhooks)

* create `.env` file in the root directory of the project

* add the following information in it
```
TOKEN='<Pivotal_Api_Token>'
SLACK_WEBHOOK='<WEBHOOK_URL>'
```

### Interesting reads
* [Reading Environment Variables From .Env File In Python](https://robinislam.me/blog/reading-environment-variables-in-python/)
* [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* [Requirements Files](https://pip.pypa.io/en/latest/user_guide/#requirements-files)
* [Slack - Legacy Tokens](https://api.slack.com/custom-integrations/legacy-tokens)
* [Slack - Slack Apps](https://api.slack.com/slack-apps)
* [Slack - Incoming Webhooks](https://api.slack.com/incoming-webhooks)
