## OS
FROM centos:7.4.1708

## Arguments
ARG PYTHON_VERSION=3.6.6
ARG PYTHON_PATH=/usr/local/bin

## Env
ENV PATH ${PYTHON_PATH}/bin:$PATH

## yum install
RUN yum install -y \
    https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm && \
    yum -y update && \
    yum install -y \
        git \
        gcc \
        make \
        zlib-devel \
        bzip2 \
        bzip2-devel \
        readline-devel \
        sqlite \
        sqlite-devel \
        openssl-devel \
        xz \
        xz-devel \
        libffi-devel \
        nginx \
        supervisor && \
    yum reinstall -y glibc-common && \
    yum clean all

## Japanese
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

ENV LC_ALL ja_JP.UTF-8
ENV TZ Asia/Tokyo

## SET pyenv and install python
WORKDIR /tmp
RUN git clone git://github.com/pyenv/pyenv.git && \
    pyenv/plugins/python-build/install.sh
RUN python-build ${PYTHON_VERSION} ${PYTHON_PATH}

RUN mkdir /app
COPY src/ /app/

WORKDIR /app
