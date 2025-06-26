FROM nginx:stable-alpine

COPY ./apps/docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./apps/docker/nginx/js_server.conf /etc/nginx/conf.d/default.conf

CMD [ "nginx", "-g", "daemon off;" ]