FROM klakegg/hugo:alpine as hugo
COPY . /src

FROM staticfloat/nginx-certbot
COPY ./infrastructure/docker/nginx/default.conf /etc/nginx/user.conf.d:ro
COPY --from=hugo /target /var/www/html
