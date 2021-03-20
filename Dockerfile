FROM python:3.8.5

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD ./entrypoint.sh
