FROM klakegg/hugo:alpine-onbuild AS hugo

FROM staticfloat/nginx-certbot
COPY ./infrastructure/docker/nginx/default.conf /etc/nginx/user.conf.d/default.conf
COPY ./infrastructure/docker/nginx/includes/ /etc/nginx/includes/
COPY ./infrastructure/docker/nginx/start.sh /start.sh
COPY --from=hugo /target /var/www/html/

RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
