#!/bin/bash
# Usage: ./fetch_data.sh
# Requires: gcloud CLI, and access to the bucket (run `gcloud auth login` first)
set -e
BUCKET="gs://candy-rush-514202-openfoodfacts/preprocessed"

mkdir -p data
gcloud storage cp -r "$BUCKET/candy_by_country" data/
gcloud storage cp -r "$BUCKET/happiness_by_country" data/
echo "Done. Data is in ./data"