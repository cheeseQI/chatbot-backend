import json
from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate


# Define a chat prompt template for use with the language model
template = ChatPromptTemplate.from_messages([
    ("system", 
     """You are a helpful AI Chat bot. Your goal is to answer the question 
     related to product with the product information as reference: {productPanelContent};
     Here is the history conversation: {history};
     """),
    ("ai", ""),
    ("human", "{user_input}"),
])

def handler(event, context):
    print('Received event:')
    print(event)
    llm = OpenAI()

    # Parse data in body
    if 'body' in event:
        try:
            parsed_body = json.loads(event['body'])
            user_input = parsed_body.get('userInput', '')
            history = parsed_body.get('history', '')
            productPanelContent = parsed_body.get('productPanelContent', '')
        except json.JSONDecodeError:
            print('Error parsing JSON body')

    if user_input:
        message = template.format_messages(
            user_input=user_input,
            history=history,
            productPanelContent=productPanelContent
        )
        print(message)
        response_text = llm.predict_messages(message).content
    else:
        response_text = "No input provided"
    
    # Format the raw text here
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
