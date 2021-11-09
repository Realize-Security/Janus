FROM nginxinc/nginx-unprivileged:1.20.1-alpine

LABEL maintainer="Realize Security Ltd."

ARG SSL_PARAMS_PATH
ARG SSL_PRIVKEY
ARG SSL_FULLCHAIN
ARG DEPLOY_ENV

ENV SSL_FULLCHAIN $SSL_FULLCHAIN
ENV SSL_PRIVKEY $SSL_PRIVKEY

USER root

COPY ./certs/$DEPLOY_ENV/$SSL_FULLCHAIN /etc/ssl/
COPY ./certs/$DEPLOY_ENV/$SSL_PRIVKEY /etc/ssl/private/
COPY ./dhparam4096.pem /etc/ssl/certs/dhparam4096.pem
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf
COPY ./ssl-params.conf $SSL_PARAMS_PATH
COPY ./run.sh /run.sh

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    mkdir -p /vol/log/nginx && \
    chown nginx:nginx /vol/log/nginx && \
    chmod 755 /etc/ssl/$SSL_FULLCHAIN && \
    chmod 755 /etc/ssl/private/$SSL_PRIVKEY && \
    chmod 755 /etc/ssl/certs/dhparam4096.pem && \
    chmod 755 $SSL_PARAMS_PATH && \
    chmod +x /run.sh

VOLUME /vol/static
VOLUME /vol/log/nginx

USER nginx

CMD ["/run.sh"]