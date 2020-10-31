import os
import json
import pytest
import boto3
from botocore.exceptions import ClientError

@pytest.fixture
def bucket():
    TEST_BUCKET = "erm-testautoengineer-test"
    s3 = boto3.resource('s3',
        region_name='ap-southeast-2',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
        aws_secret_access_key=os.environ['AWS_SECRET_KEY']
    )
    try:
        s3.meta.client.head_bucket(Bucket=TEST_BUCKET)
    except ClientError:
        pytest.fail(f"bucket {TEST_BUCKET} doesn't exit")
    return s3.Bucket(TEST_BUCKET)


def test_bucket_contains_only_1_object(bucket):
    all_objects = list(bucket.objects.all())
    assert len(all_objects) == 1
    
    
def test_object_content(bucket):
    TEST_OBJ_KEY = "samplefile_9d0ccca0-ac99-44b2-aae6-edfa0d18c1b5.json"
    obj = bucket.Object(TEST_OBJ_KEY)
    file_content = obj.get()['Body'].read().decode()
    json_content = json.loads(file_content)
    assert json_content[0]["userId"] == 1
    