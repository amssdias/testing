FROM python:3.9

COPY . my_project/

WORKDIR /my_project

RUN pip install -r requirements.txt
RUN python manage.py migrate

ENTRYPOINT python manage.py runserver 0.0.0.0:8000 --settings=calorie_counter.settings.local