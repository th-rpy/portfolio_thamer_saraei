git add .
git commit -m "Initial commit"
python3 manage.py makemigrations
python3 manage.py migrate
git push heroku master
heroku run python3 manage.py makemigrations
heroku run python3 manage.py migrate