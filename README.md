# Blacklisting
An in-memory Blacklisting Service using Django framework.

[Refer this website for API Usage](https://rakesht2499.github.io/Blacklisting/) [Site Under Construction]

## Pre-requisites

- Docker

#### Running In local

- Python3

## How to Start Server

#### Using Docker

```shell script
docker build -t blacklisting .
docker run -p 8000:8000 blacklisting
```
The above commands start the server in port 8000

#### Without Docker

```shell script
pip install -r requirements.txt
cd blacklisting
python manage.py runserver
```

## How to use

### API's

#### GET

Lists all the IPv4 address from DB

**Request**

```shell script
curl -XGET 'localhost:8000/v1/blacklist'
```

**Response**
```shell script
HTTP/1.1 200 OK
{"all_ip": ["192.168.97.10", "192.168.98.10", "192.168.08.58", "192.168.0.2", "192.168.0.25"]}
```

##### POST

**Request**

```shell script
curl -XPOST 'localhost:8000/v1/blacklist' \
        --header 'Content-Type: application/json' \
        --data-raw '"{\"ip\" : \"192.168.0.3\"}"'
```

**Response**
```shell script
HTTP/1.1 201 Created
```

##### DELETE

**Request**

```shell script
curl -XDELETE 'localhost:8000/v1/blacklist' \
        --header 'Content-Type: application/json' \
        --data-raw '"{\"ip\" : \"192.168.0.3\"}"'
```

**Response**
```shell script
HTTP/1.1 200 OK
```

##### DELETE

```shell script
curl -XDELETE localhost:8000/v1/blacklist
        --body '{"ip":"192.168.92.68"}'
```

### Copyrights
```
/**
 * 
 * @author Rakesh Kumar T
 * @github rakesht2499
 *
 */
```
