
import os

import boto3
from botocore.exceptions import ClientError
from pathlib import Path


BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "python-api-s3-automation-umar-2026")
REGION = os.getenv("AWS_REGION", "eu-north-1")
OBJECT_KEY = os.getenv("S3_OBJECT_KEY")

PROJECT_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = PROJECT_DIR / "data" / "downloads"


def download_from_s3(object_key=OBJECT_KEY):
    """Download a JSON file from Amazon S3."""

    if not object_key:
        print("Set S3_OBJECT_KEY to the name of an object in the configured bucket.")
        return False

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    destination = DOWNLOAD_DIR / Path(object_key).name

    s3_client = boto3.client("s3", region_name=REGION)

    try:
        s3_client.download_file(
            BUCKET_NAME,
            object_key,
            str(destination)
        )

        print(f"Successfully downloaded {object_key}.")
        print(f"Saved to: {destination}")
        return True

    except ClientError as error:
        print(f"S3 download failed: {error}")
        return False


if __name__ == "__main__":
    raise SystemExit(0 if download_from_s3() else 1)

