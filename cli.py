"""
Module that contains the command line app.
"""
import argparse
import os
from google.cloud import storage


GCS_BUCKET_NAME = os.environ["GCS_BUCKET_NAME"]

def download_data():
    print("download_data")

    bucket_name = GCS_BUCKET_NAME

    # Initiate Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix="features/")

    # Download annotations
    for blob in blobs:
        print("Downloading file:", blob.name)

        blob_folder_structure = os.path.dirname(blob.name)
        if not os.path.exists(blob_folder_structure):
            os.makedirs(blob_folder_structure, exist_ok=True)
        blob.download_to_filename(blob.name)


def main(args=None):
    if args.download:
        download_data()


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="Data Versioning CLI.")

    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download labeled data from a GCS Bucket",
    )

    args = parser.parse_args()

    main(args)
