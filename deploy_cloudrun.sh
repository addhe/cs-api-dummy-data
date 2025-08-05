# Deploy Flask app to Google Cloud Run
# Usage: bash deploy_cloudrun.sh

set -e

REGION=asia-southeast2
PROJECT=awanmasterpiece
SERVICE_NAME=nasabah-api
SOURCE_DIR=src

# Set environment variables (edit as needed or use --env-vars-file)
ENV_VARS="SUPABASE_URL=$SUPABASE_URL,SUPABASE_KEY=$SUPABASE_KEY,API_KEY=$API_KEY"

gcloud run deploy $SERVICE_NAME \
  --source $SOURCE_DIR \
  --region $REGION \
  --project $PROJECT \
  --allow-unauthenticated \
  --set-env-vars $ENV_VARS

echo "\nDeployment to Cloud Run triggered. Check GCP Console for status."
