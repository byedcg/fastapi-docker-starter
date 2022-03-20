source .env
docker run -p 8002:${PORT} -e PORT=${PORT} IMAGE_URL
