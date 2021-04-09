# Personal Web Portfolio

## Built with
* [Django 2.2.2](https://www.djangoproject.com/)
* JavaScript
* [Python 3.6.8](https://www.python.org/)
* PostgreSQL

## Instructions
- Install [Python](https://www.python.org/) (v.3.6.8 is recommended).
- Clone or download this repository.
- Using a command prompt/terminal, go the project folder: `/web-portfolio/`
- Install the dependencies: 
`pip install -r requirements.txt`
- Create migration files for the database:
`python manage.py makemigrations`
- Apply migrations: 
 `python manage.py migrate`
- Run the server:
`python manage.py runserver [port number, default=8000]`
- Using a web browser, go to `http://127.0.0.1:[port]/`