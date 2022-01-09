# flask-docker-example
The same flask application packaged in 3 different docker images to show how simple it can be to reduce docker image sizes while maintaining the same level of functionality.

You can find a walkthorough here - https://buggycodemaster.medium.com/building-smaller-docker-images-the-right-way-1b6c12c112e1

## Debian
docker build -t flask-runner:debian -f Dockerfile.debian .

## Alpine
docker build -t flask-runner:alpine -f Dockerfile.alpine .

## Alpine multi-stage
docker build -t flask-runner:alpine-multi-stage -f Dockerfile.alpine.multi-stage .
