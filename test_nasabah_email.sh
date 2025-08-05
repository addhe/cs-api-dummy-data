#!/bin/bash
# Test API nasabah by email using curl

API_URL="https://nasabah-api-361046956504.asia-southeast2.run.app/nasabah"
API_KEY="REMOVED_API_KEY"
EMAIL="addhe.warman@outlook.co.id"

curl -X GET "$API_URL?email=$EMAIL" \
  -H "x-api-key: $API_KEY" \
  -H "Accept: application/json"
