import os
import boto3
import time
import json
import boto3
import json
from botocore.exceptions import ClientError
import datetime
from amazon_web_services_helpers.aws_helper import AwsHelper


class S3Helper:
    @staticmethod
    def get_s3_bucket_region(bucket_name):
        client = boto3.client('s3')
        response = client.get_bucket_location(Bucket=bucket_name)
        aws_region = response['LocationConstraint']
        return aws_region

    @staticmethod
    def get_file_names(bucket_name, prefix, max_pages, allowed_file_types, aws_region=None):
        files = []
        current_page = 1
        has_more_content = True
        continuation_token = None
        s3client = AwsHelper().getClient('s3', aws_region)
        while has_more_content and current_page <= max_pages:
            if continuation_token:
                list_objects_response = s3client.list_objects_v2(
                    Bucket=bucket_name,
                    Prefix=prefix,
                    ContinuationToken=continuation_token)
            else:
                list_objects_response = s3client.list_objects_v2(
                    Bucket=bucket_name,
                    Prefix=prefix)
            if list_objects_response['IsTruncated']:
                continuation_token = list_objects_response['NextContinuationToken']
            else:
                has_more_content = False
            for doc in list_objects_response['Contents']:
                doc_name = doc['Key']
                doc_ext = FileHelper.get_file_extenstion(doc_name)
                doc_ext_lower = doc_ext.lower()
                if doc_ext_lower in allowed_file_types:
                    files.append(doc_name)
        return files

    @staticmethod
    def write_to_s3(content, bucket_name, s3_file_name, aws_region=None):
        s3 = AwsHelper().get_resource('s3', aws_region)
        object = s3.Object(bucket_name, s3_file_name)
        object.put(Body=content)

    @staticmethod
    def read_from_s3(bucket_name, s3_file_name, aws_region=None):
        s3 = AwsHelper().get_resource('s3', aws_region)
        obj = s3.Object(bucket_name, s3_file_name)
        return obj.get()['Body'].read().decode('utf-8')
