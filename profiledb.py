import boto3


if __name__ == '__main__':
    client = boto3.client('dynamodb')
    create_table('test_table')
