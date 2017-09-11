Installation
------------

```
$ docker build -t gala .
$ docker run -name gala -d -p 80:80 -v ~/web/site-gala:/var/src/site-gala gala
$ docker exec -it gala sh
/var/src/site-gala # ./manage.py migrate
```
Puis rendez-vous sur <localhost> pour admirer le résultat
