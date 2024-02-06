import requests
from bs4 import BeautifulSoup

# Replace 'your_url_here' with the actual URL of the website
url = 'https://www.davidsbridal.com/store-list'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <p> tags with the specified class
    paragraphs = soup.find_all('p', class_='textstyled__TextStyled-sc-1qzarz-0 epsTcP')

    # Write the text content of each paragraph to a .txt file
    with open('output.txt', 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(paragraph.text + '\n')

    print("Scraped content written to output.txt")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
