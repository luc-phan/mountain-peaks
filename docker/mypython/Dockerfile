FROM python:3
ENV PYTHONUNBUFFERED=1
RUN pip install pipenv
WORKDIR /code/mysite
CMD pipenv install && pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000
