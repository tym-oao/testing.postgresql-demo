FROM debian:jessie

RUN apt-get update \
&& apt-get install \
python3 \
postgresql-9.4

RUN su - postgres -c "pg_dropcluster --stop 9.4 main"
RUN pip install testing.postgresql

ADD myapp /app

CMD ["su", "postgres", "-c", "nosetests"]
