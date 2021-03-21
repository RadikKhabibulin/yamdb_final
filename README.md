![yamdb_workflow.yml](https://github.com/radikkhabibulin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# YaMDb_final

This project is REST API for the YaMDb service - a database of reviews of movies, books and music.
To view the documentation for working with this API after deploying and launching the project, follow the link http://127.0.0.1:5003/redoc/ .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. This project contains the yamdb_workflow.yml file. This file performs some instructions when push the project to its github directory. To understand these actions go to the website https://docs.github.com/en/actions.

### Prerequisites

To start the project, you need to install Docker. Download this program from the official [website](https://www.docker.com/).

```
Install Docker by following the installation instructions on Windows and macOS.
Installation instructions for Linux: https://docs.docker.com/engine/install/ubuntu/ .

```

## Deployment

1. Сreate an env file in the root directory of the project and add the following variables to it:
    FROM_EMAIL=<example@gmail.com>
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=<postgres_name>
    POSTGRES_USER=<postgres_user>
    POSTGRES_PASSWORD=<postgres_password>
    DB_HOST=db
    DB_PORT=<port>

2. Create an image and run the containers with the command:
```
docker-compose up
```

## Create a superuser in database container

1. After deployment find out the container id of the yamdb_final_web command:
```
docker container ls
```

3. Log in to the container using its ID and perform database migrations:
```
docker exec -it <CONTAINER ID> bash
```
or
```
winpty docker exec -it <CONTAINER ID> bash
```
and
```
python manage.py createsuperuser
```

4. If you need to populate the database with your own data, replace
   the "fixtures.json" file with your own and run the Deployment section.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Docker](https://www.docker.com/) - Automatic deployment of the project

## Authors

* **Radik Khabibulin** - *Initial work* - [RadikKhabibulin](https://github.com/RadikKhabibulin)
