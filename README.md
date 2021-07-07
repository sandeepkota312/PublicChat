This procedure is determined to only windows users. I would recommend to use pycharm to run this application.

1. Install Python 3.9.5 version - https://www.python.org/downloads/
2. Create a new project in your pycharm and open that project.
3. Clone this git repository to your system and place them in the project folder.
4. In the terminal go to pizza repository using the command 'cd PublicChat'.
5. Then type the following commands in sequence as follows:
    1. pip install -r requirements.txt
    2. python manage.py makemigrations
    3. python manage.py migrate
    4. python manage.py createsuperuser - Then add a username, email and password in the following steps as mentioned in the terminal
    5. python manage.py runserver
6. Then use the link mentioned in the terminal to open the framework.

Note: Give proper input when you are trying to register. If any invalid input given the page gets refreshed asking for input again.
