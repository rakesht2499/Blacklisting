FROM python:3.11

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY blacklisting blacklisting/
WORKDIR blacklisting
COPY requirements.txt ./
COPY starting.sh .
RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["sh", "starting.sh"]
