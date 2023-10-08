import json
from langchain.llms import OpenAI

def handler(event, context):
    print('Received event:')
    print(event)
    llm = OpenAI()

    # parse data in body
    if 'body' in event:
        user_input = event['body']
    else:
        user_input = ''

    if user_input is not None:
        response_text = llm.predict(user_input)
    else:
        response_text = "No input provided"
    formatted_text = response_text.replace('\n', '<br>')

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(formatted_text)
    }

    return response
