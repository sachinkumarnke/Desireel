FROM nginx:alpine

# Copy static files
COPY ./static /usr/share/nginx/html/static
COPY ./static_root /usr/share/nginx/html/static_root
COPY ./media /usr/share/nginx/html/media
COPY ./templates /usr/share/nginx/html/templates

# Copy nginx configuration
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]