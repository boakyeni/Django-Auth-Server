### Django Single Sign On Microservice Application for Development

To demo, clone, create .env and run ```docker compose --build``` then ```docker compose up -d```

Create a superuser with ```docker compose exec api python3 manage.py createsuperuser```

Go to o/authorize/register/

Create an application and note down clientid and clientsecretkey

use RSA for oidc

add http://localhost:8080/dashboard to redirect uri and http://localhost:8080 to postlogout uri

More detailed instructions coming soon

