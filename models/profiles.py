import boto3

def model(table_name):
    return dict(
        AttributeDefinitions=[
            {'AttributeName':'ExternalID','AttributeType':'S' },
            {'AttributeName':'convoConfigID','AttributeType':'S'}
        ],
        TableName=table_name,
        KeySchema=[
            {'AttributeName':'ExternalID','KeyType':'HASH'}
        ],
        LocalSecondaryIndexes=[],
        GlobalSecondaryIndexes=[],
        ProvisionedThroughput={},
        StreamSpecification={}
    )
