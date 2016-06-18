# Overview and Our Stack

- Four Tier Microservice Django Web Application Built On Docker Containers
  - Layer 1: MySQL database
  - Layer 2: Models API
  - Layer 3: Service level API
  - Layer 4: Web Interface

# Requirements

- Django 1.8.8
- Python 3.4.3
- Docker 1.9.1
- Containers handle the rest!

# Running the project

```
git clone https://github.com/bjs9yv/CS4501.git
docker-compose build
docker-compose up
```
Direct your browser to http://localhost:8000/

# Layer 1: MySQL database
  - Migrations: Django fixtures

# Layer 2: Models API
  - API: Django Rest API
  - Authentication: Cookies with custom SHA-256 authentication tokens

# Layer 3: Service level API
  - Search: Kafka/zookeeper queuing + Elastic Search (ES) 

# Layer 4: Web Interface
  - UI: Bootstrap
