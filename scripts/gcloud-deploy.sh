source .env
# configure 
gcloud run services replace service.yaml
# build
gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/$CONTAINER_NAME
echo "Container submitted!"
# deploy
gcloud run deploy $GCP_SERVICE_NAME \
    --image gcr.io/$GCP_PROJECT_ID/$CONTAINER_NAME \
    --platform managed
echo "Container deployed!"
