import os


class AppConfig:
    APP_AWS_S3_BUCKET_NAME = os.environ.get("APP_AWS_S3_BUCKET_NAME", None)
    APP_AWS_ENDPOINT_URL = os.environ.get("APP_AWS_ENDPOINT_URL", None)
    APP_AWS_ACCESS_KEY_ID = os.environ.get("APP_AWS_ACCESS_KEY_ID", None)
    APP_AWS_SECRET_ACCESS_KEY = os.environ.get("APP_AWS_SECRET_ACCESS_KEY", None)
    APP_AWS_REGION_NAME = os.environ.get("APP_AWS_REGION_NAME", "us-east-1")
