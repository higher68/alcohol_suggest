FROM postgres:9.5.12

ARG UID=501
ARG GID=20

COPY postgresql.conf /etc/postgresql

ENV TZ Asia/Tokyo

RUN usermod -u ${UID} postgres && \
    groupmod -g ${GID} -o postgres

RUN mkdir -p /var/log/postgresql && \
    chown postgres:postgres /var/log/postgresql

COPY init/ /docker-entrypoint-initdb.d/ 
