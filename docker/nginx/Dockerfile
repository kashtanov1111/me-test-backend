FROM nginx:1.23
LABEL 'MAINTAINER' = 'Oleg V. Ivantsov, email: o.v.ivantsov@gmail.com'

RUN rm /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/nginx.conf
COPY servers/default.conf.template /etc/nginx/templates/

RUN apt-get update && apt-get install -y \
    mc \
    nano \
    software-properties-common \
    python3-certbot-nginx