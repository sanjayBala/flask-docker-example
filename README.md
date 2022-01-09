# Build Docker Image

## Debian
docker build -t flask-runner:debian -f Dockerfile.debian .

## Alpine
docker build -t flask-runner:alpine -f Dockerfile.alpine .