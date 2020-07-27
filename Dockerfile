FROM quay.io/cdis/python-nginx:pybase3-1.2.0

ENV appname=acronymbot

ENV DEBIAN_FRONTEND=noninteractive

RUN adduser -D -g '' acronymbotuser

RUN mkdir -p /opt/ctds/acronymbot \
    && chown acronymbotuser /opt/ctds/acronymbot

RUN apk update \
    && apk add libffi-dev libressl-dev linux-headers musl-dev gcc \
    && apk add curl bash git

COPY . /opt/ctds/acronymbot
WORKDIR /opt/ctds/acronymbot

RUN pip3.6 install --upgrade pip && python3.6 -m pip install --upgrade wheel && python3.6 -m pip install -r requirements.txt \
    && COMMIT=`git rev-parse HEAD` && echo "COMMIT=\"${COMMIT}\"" >acronymbot/version_data.py \
    && VERSION=`git describe --always --tags` && echo "VERSION=\"${VERSION}\"" >>acronymbot/version_data.py 

WORKDIR /opt/ctds/acronymbot/acronymbot

USER acronymbotuser

ENTRYPOINT ["sh","-c","python3.6 acronymbot.py"]
