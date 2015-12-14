FROM alpine:latest
MAINTAINER yagermadden@gmail.com
ENV SHELL=/bin/bash

RUN apk update && \
apk add --update musl \
python3 \
python3-dev \
postgresql \
postgresql-dev \
build-base \
bash \
vim \
tmux \
git

RUN pip3 install \
psycopg2 \
git+https://github.com/tk0miya/testing.postgresql.git

RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

# VOLUME /working
WORKDIR /working
RUN mkdir -p  /working/bin
RUN ln -s /usr/bin/vim /working/bin/vi
RUN ln -s /usr/bin/python3 /working/bin/python
ADD dotfiles/* /root/
ADD solarized.vim /root/.vim/colors/
ADD togglebg.vim /root/.vim/autoload/
ADD *demo*.py /working/
ADD sample/ /working/sample

CMD ["/bin/bash"]