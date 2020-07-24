FROM klakegg/hugo:alpine-onbuild as hugo

FROM staticfloat/nginx-certbot
COPY ./infrastructure/docker/nginx/default.conf /etc/nginx/user.conf.d/default.conf
COPY --from=hugo /target /var/www/html
