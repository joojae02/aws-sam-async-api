import json
import time

def lambda_handler(event, context):
    # input_data = json.loads(event['body'])
    
    time.sleep(60)  # Sleep for 5 seconds
    # result = process_data(input_data)
    
    # print(f"Lambda B completed processing: {result}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Asynchronous processing completed by Lambda B',
            'result': "resultB"
        })
    }

def process_data(data):
    # Implement your data processing logic here
    return "Processed asynchronously by Lambda B: " + str(data)