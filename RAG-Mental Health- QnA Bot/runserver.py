"""
This script runs the RAG_Mental_Health__QnA_Bot application using a development server.
"""

from os import environ
from RAG_Mental_Health__QnA_Bot import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
