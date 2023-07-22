FROM klakegg/hugo:0.100.0-ext-alpine-onbuild AS hugo

FROM nginx
COPY ./infrastructure/docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./infrastructure/docker/nginx/includes/ /etc/nginx/includes/
COPY --from=hugo /target /var/www/html/
