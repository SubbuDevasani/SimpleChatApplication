FROM postgres:latest
ADD . /tmp/SimpleChatApplication
WORKDIR /tmp/SimpleChatApplication
COPY createdb.sql /docker-entrypoint-initdb.d
