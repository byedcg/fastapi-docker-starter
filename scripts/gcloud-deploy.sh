# build
gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/container-name
# deploy
gcloud run deploy --image gcr.io/$GCP_PROJECT_ID/container-name --platform managed