FROM python:alpine3.6

WORKDIR /var/src/site-gala

COPY requirements.txt /var/src/site-gala/requirements.txt
RUN apk add --no-cache zlib-dev libjpeg-turbo-dev freetype-dev lcms2-dev libwebp-dev musl-dev openjpeg-dev tiff-dev gcc && \
    pip install -r requirements.txt

COPY ./ /var/src/site-gala/

RUN /var/src/site-gala/manage.py migrate

CMD /var/src/site-gala/manage.py runserver 0.0.0.0:80
