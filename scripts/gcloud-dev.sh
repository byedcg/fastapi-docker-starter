source .env
gcloud auth application-default login
gcloud beta code dev \
    --dockerfile=./Dockerfile \
    --application-default-credential \
    --local-port $LOCAL_PORT 
