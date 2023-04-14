from s3client import S3Client
import requests
import yaml

if __name__ == '__main__':
    with open('config.yaml') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    region_name = conf['region_name']
    aws_access_key_id = conf['aws_access_key_id']
    aws_secret_access_key = conf['aws_secret_access_key']

    s3_client = S3Client(region_name, aws_access_key_id, aws_secret_access_key)

    bucket_name = 'skon-battery-defect'
    filepath = 'models/yes.png'
    ob_url = s3_client.create_presigned_url(bucket_name, filepath, expiration=60)  # 60초동안 유효한 url
    print(ob_url)

    if ob_url is not None:
        response = requests.get(ob_url)
    print(response)
