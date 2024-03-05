from flask import render_template, request
from datetime import datetime

# Import the function that fetches and processes content
from RAG_Mental_Health__QnA_Bot import app, fetch_content, retrieve_passages_from_web

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    # Your existing code to fetch passages from the web
    user_question = request.args.get('user_question', '')  # Get user input from the query parameter
    
    # Fetch passages for the search results
    search_result_urls = retrieve_passages_from_web(user_question)
    
    # Fetch content from each URL
    passages = [fetch_content(url) for url in search_result_urls]

    #Stage-2
    from transformers import GPT2LMHeadModel, GPT2Tokenizer

    # Fetch content from each URL
    passages = [fetch_content(url) for url in search_result_urls]

    # Combine passages into a single string for context
    context = ' '.join(passages)

    # Formulate prompt for GPT-2
    prompt = f"Prompt: {user_question}\nContext: {context}\nResponse:"

    # Load pre-trained GPT-2 model and tokenizer
    model_name = 'gpt2'  # You can use other GPT-2 variants like 'gpt2-medium', 'gpt2-large', etc.
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Tokenize the prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Truncate input_ids if it exceeds max_length
    max_length = 150  # Choose an appropriate value
    if input_ids.size(1) > max_length:
        input_ids = input_ids[:, :max_length]

    # Generate response using GPT-2
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        max_new_tokens=500,  # Adjust as needed
    )

    # Decode the generated response
    generated_response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Render the home page with the generated response
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        generated_response=generated_response  # Pass the generated response to the template
    )

