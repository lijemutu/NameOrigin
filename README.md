# MexicanPolitician
API para obtener información de políticos mexicanos y usar una API pública para conocer el origen o nacionalidad de sus nombres o apellidos/API to get info from mexican politicians and use public API to know their names origin

## Introduction
Alguna vez has notado como los apellidos del gobernador, alcalde, diputado o cualquier otro político suenan diferente al del resto de la población, ¿Suenan como de otro país?...

Have you ever noticed how your the last names of your state governor, mayor, deputy or any other politician has something different than most of population, does it sound from another country?...



## Development Installation 

### Dependencies

* Docker.
* Docker compose.
* Python >= 3.8.3
* Pip.
* Virtual environment tool. (venv, virtualenvwrapper)
* Git.

### Installation
From any terminal with dependencies installed run the following commands.

Grab the repo from github.
~~~
git clone https://github.com/lijemutu/NameOrigin.git
~~~

~~~
cd NameOrigin
~~~

Build the application and run it through Docker compose

~~~
docker build -t . && docker compose -f docker-compose-dev-yml up -d
~~~
An app and postgres container will be created in port 5000 and 5432.

During development kil app container in order to keep postgres running for the development app.

## Deployment

### Aws ECS Service
A aws ecs service was used according to [this](https://www.youtube.com/playlist?list=PL0dOL8Z7pG3IWsvseNd-JoFTHL16P_iTC) tutorial, and using docker-compose.yml file but since this service is not free I went the free layer route.

### EC2 deployment

After creating a EC2 instance with a public IP and with a image pushed in docker hub repo run the one-liner in ec2conf.sh