FROM quay.io/cdis/python-nginx:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN adduser -D -g '' acronymbotuser

RUN mkdir -p /opt/ctds/acronymbot \
    && chown acronymbotuser /opt/ctds/acronymbot

COPY . /acronymbot
WORKDIR /acronymbot

RUN python -m pip install -r requirements.txt \
    && COMMIT=`git rev-parse HEAD` && echo "COMMIT=\"${COMMIT}\"" >acronymbot/version_data.py \
    && VERSION=`git describe --always --tags` && echo "VERSION=\"${VERSION}\"" >>acronymbot/version_data.py 

WORKDIR /opt/ctds/acronymbot

USER acronymbotuser

CMD /dockerrun.sh
