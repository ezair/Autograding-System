FROM python:3.6

WORKDIR /usr/src/app
COPY ./requirements.txt .

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
             python3 \
  && rm -rf /var/lib/apt/lists/* \
  && groupadd django \
  && useradd -g django -s /bin/bash django \
  && pip install --upgrade pip \
  && pip install -r requirements.txt

CMD ["./runserver.sh", "0.0.0.0:8000"]
