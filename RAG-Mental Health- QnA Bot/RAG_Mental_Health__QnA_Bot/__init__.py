from flask import Flask

app = Flask(__name__)

from RAG_Mental_Health__QnA_Bot.helpers import fetch_content, retrieve_passages_from_web

import RAG_Mental_Health__QnA_Bot.views  # Import views after initializing app and functions
