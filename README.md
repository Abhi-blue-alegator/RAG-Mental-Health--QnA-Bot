# RAG-Mental Health- QnA Bot

The RAG Pipeline project is an implementation of a chatbot system that leverages the powerful combination of retrieval-based and generative models. The pipeline consists of two main stages: retrieval and generation. In the retrieval stage, the system extracts relevant information from the web using a Google search API to gather passages related to the user's query on mental health. The retrieved passages are then processed to filter out unwanted details, ensuring the relevance and quality of the information.

In the second stage, a GPT-2 (Generative Pre-trained Transformer 2) model is employed for text generation. The system formulates a prompt using the user's question and the retrieved passages, creating a context-rich input for the generative model. The GPT-2 model generates a response, providing insightful and context-aware answers to the user's queries on mental health.
