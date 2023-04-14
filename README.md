# S3-Client : Get Object From AWS S3 via presigned url

## Install package
```shell
pip3 inistall -r requirements.txt
```

## make config file
create `config.yaml` file
```yaml
region_name : <your S3 Bucket Region>
aws_access_key_id : <User Access Key>
aws_secret_access_key : <User Access Key>
```
## example of using S3-Client
- edit main.py
```python
bucket_name = <your bucket name>
filepath = <your object path in bucket>
```
## run 
```shell
python3 main.py
```
