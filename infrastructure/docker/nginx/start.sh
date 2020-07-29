#!/bin/bash
sed -i '3i\server_name '"$APP_URL;'"\' /etc/nginx/conf.d/certbot.conf

nginx -g "daemon off;"
