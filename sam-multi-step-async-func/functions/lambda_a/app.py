import json

def lambda_handler(event, context):
    # Process the incoming request
    # input_data = json.loads(event['body'])  # Assuming the input is in the 'body' field
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Request processed successfully by Lambda A',
            'result': "result"
        })
    }
