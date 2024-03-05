import requests
from bs4 import BeautifulSoup
from googlesearch import search

def retrieve_passages_from_web(question):
    # Perform a Google search and get the top 5 results
    search_results = list(search(f"{question}", num_results=5))

    # Extract relevant passages from the search results
    urls = []
    for result in search_results:
        urls.append(result)

    return urls

def fetch_content(url, max_length=500):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from paragraphs
        paragraphs = soup.find_all('p')

        # Combine paragraphs into content
        content = ' '.join([paragraph.get_text() for paragraph in paragraphs])

        # Remove unwanted details (you may need to customize this part based on your needs)
        unwanted_phrases = ['Official website', 'Call or Text', 'Your browser is not supported']
        content = ' '.join([line for line in content.split('\n') if not any(phrase in line for phrase in unwanted_phrases)])

        # Limit the length of the content
        if len(content) > max_length:
            content = content[:max_length] + '...'

        return content.strip()
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None


