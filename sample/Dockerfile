FROM debian:jessie

RUN apt-get update \
&& apt-get install \
python3 \
postgresql-9.4

RUN su - postgres -c "pg_dropcluster --stop 9.4 main"

ADD myapp /app

CMD "su postgres -c nosetests"
