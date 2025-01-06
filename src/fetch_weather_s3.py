import json
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = "devopsweatherdashboard"

def lambda_handler(event, context):
    """Fetch list of weather data files from S3"""
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="weather-data/")
        
        if "Contents" not in response:
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "No weather data found"})
            }
        
        files = [{"Key": obj["Key"], "LastModified": obj["LastModified"].isoformat()} for obj in response["Contents"]]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(files)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }