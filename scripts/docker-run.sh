source .env
docker rm $CONTAINER_NAME
docker run -d --name $CONTAINER_NAME -p 8001:80 $IMAGE_NAME