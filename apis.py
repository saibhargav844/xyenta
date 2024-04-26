import requests
import pandas as pd

# Replace 'API_KEY' with your actual API key from NewsAPI
API_KEY = '36a8e43d4a644d4d8d48a432c76dba05'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    articles = data['articles']
    # Extracting relevant data from the articles
    article_data = [(article['title'], article['description'], article['url']) for article in articles]
    # Creating DataFrame
    dataframe = pd.DataFrame(article_data, columns=['Title', 'Description', 'URL'])
    print(dataframe)
else:
    print("Failed to retrieve data:", data['message'])
    print("Status code:", response.status_code)
