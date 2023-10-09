# chatbot-chat-service

**Description**  
Acts as a chatbot using OpenAI language models to answer questions related to a product.

**Dependencies**  
- Python 3.10
- OpenAI Python package
- LangChain
- AWS Lambda Python Runtime

**Installation**  
1. Install required Python packages.
2. Deploy to AWS Lambda.

**API**  
- Trigger via HTTP POST with JSON payload containing:
  - `userInput`
  - `history`
  - `productPanelContent`