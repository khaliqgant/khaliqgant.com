FROM klakegg/hugo:alpine as hugo

FROM nginx
COPY ./infrastructure/docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=hugo /public /var/www/html
