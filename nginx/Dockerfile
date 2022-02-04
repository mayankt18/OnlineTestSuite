FROM nginx:1.19

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
COPY jcc.nitdgplug.org.pem /etc/nginx/jcc.nitdgplug.org
COPY jcc.nitdgplug.org.key /etc/nginx/jcc.nitdgplug.org.key
EXPOSE 80