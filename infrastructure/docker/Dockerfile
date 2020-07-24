FROM klakegg/hugo:alpine-onbuild as hugo
COPY . /src

FROM staticfloat/nginx-certbot
COPY ./infrastructure/docker/nginx/default.conf /etc/nginx/user.conf.d/default.conf
COPY ./infrastructure/docker/nginx/includes/ /etc/nginx/includes/
COPY --from=hugo /target /var/www/html
