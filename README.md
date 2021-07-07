This procedure is determined to only windows users. I would recommend to use pycharm to run this application.

Install Python 3.9.5 version - https://www.python.org/downloads/
Create a new project in your pycharm and open that project.
Clone this git repository to your system and place them in the project folder.
In the terminal go to pizza repository using the command 'cd pizza'.
Then type the following commands in sequence as follows:
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser - Then add a username, email and password in the following steps as mentioned in the terminal
python manage.py runserver
Then use the link mentioned in the terminal to open the framework.
All the different API endpoints that are added in the application is mentioned in the webpage in the format 'Task':'/directory/'. Add that directory in the webpage to open that particular API endpoint
