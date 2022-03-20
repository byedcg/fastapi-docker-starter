source .env
docker image rm $IMAGE_NAME
docker build -f Dockerfile -t $IMAGE_NAME .
