import logging
import boto3
from botocore.exceptions import ClientError


class S3Client:
    def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):
        self.service_name = "s3"
        self.s3 = boto3.client(self.service_name)
        self.region_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.connect()
    def connect(self):
        try:
            self.s3 = boto3.client(
                service_name=self.service_name,
                region_name=self.region_name,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            )
        except Exception as e:
            logging.error(e)

    def create_presigned_url(self, bucket_name, object_name, expiration=600):
        """S3 객체를 공유하기 위해 사전인증 URL 생성하기

        :param bucket_name: string
        :param object_name: string
        :param expiration: 사전인증 URL이 유효한 시간(초) / default: 10분
        :return: 문자열의 사전인증URL. 오류가 있으면 None 반환
        """
        try:
            response = self.s3.generate_presigned_url('get_object',
                                                      Params={'Bucket': bucket_name,
                                                              'Key': object_name},
                                                      ExpiresIn=expiration)
        except ClientError as e:
            logging.error(e)
            return None

        # 사전인증 URL이 포함된 응답
        return response
