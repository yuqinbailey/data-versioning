#!/bin/bash

set -e

export IMAGE_NAME=dvc-docker-image
export BASE_DIR=$(pwd)
export SECRETS_DIR=$(pwd)/../AC215_S2S/src/secrets/
export SSH_DIR=$HOME/.ssh
export GCS_BUCKET_NAME="s2s_data"
export GCP_PROJECT="ac215-project"
export GCP_ZONE="us-central1-a"


# Build the image based on the Dockerfile
docker build -t $IMAGE_NAME -f Dockerfile .

sudo docker run --rm --name $IMAGE_NAME --privileged  -ti \
-v "$BASE_DIR":/app \
-v "$SECRETS_DIR":/secrets \
-v "$SSH_DIR":/home/app/.ssh \
-e GOOGLE_APPLICATION_CREDENTIALS=/secrets/dvc-secrets.json \
-e GCP_PROJECT=$GCP_PROJECT \
-e GCP_ZONE=$GCP_ZONE \
-e GCS_BUCKET_URI=$GCS_BUCKET_URI \
$IMAGE_NAME
