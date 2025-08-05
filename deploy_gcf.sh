#!/bin/bash
# Deploy FastAPI app to Google Cloud Functions (2nd gen, Python 3.11)
# Usage: bash deploy_gcf.sh

set -e

REGION=asia-southeast2
PROJECT=awanmasterpiece
FUNCTION_NAME=nasabah-api
ENTRY_POINT=app
RUNTIME=python311
SOURCE_DIR=src

# Set environment variables (edit as needed or use --env-vars-file)
ENV_VARS="SUPABASE_URL=$SUPABASE_URL,SUPABASE_KEY=$SUPABASE_KEY,API_KEY=$API_KEY"

gcloud functions deploy $FUNCTION_NAME \
  --gen2 \
  --region=$REGION \
  --project=$PROJECT \
  --runtime=$RUNTIME \
  --source=$SOURCE_DIR \
  --entry-point=$ENTRY_POINT \
  --trigger-http \
  --allow-unauthenticated \
  --set-env-vars=$ENV_VARS

echo "\nDeployment triggered. Check GCP Console for status."
