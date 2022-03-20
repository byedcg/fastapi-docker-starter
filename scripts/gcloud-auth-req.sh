source .env
curl -H \
    "Authorization: Bearer $(gcloud auth print-identity-token)" \
    ${GCP_SERVICE_URL}