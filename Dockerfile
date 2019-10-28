FROM quay.io/cdis/py27base:pybase2-1.0.2

ENV DEBIAN_FRONTEND=noninteractive

# the www-data user is created in the parent image, just reusing it here
RUN mkdir -p /opt/ctds/acronymbot \
    && chown www-data /opt/ctds/acronymbot

COPY . /acronymbot
WORKDIR /acronymbot

RUN python -m pip install -r requirements.txt \
    && COMMIT=`git rev-parse HEAD` && echo "COMMIT=\"${COMMIT}\"" >acronymbot/version_data.py \
    && VERSION=`git describe --always --tags` && echo "VERSION=\"${VERSION}\"" >>acronymbot/version_data.py 

WORKDIR /opt/ctds/acronymbot

CMD /dockerrun.sh
