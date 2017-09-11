docker build -t gala .
docker run -name gala -d -p 80:80 -v ~/web/site-gala:/var/src/site-gala gala
docker exec -it gala sh
