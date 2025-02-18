
import requests
from bs4 import BeautifulSoup

def user_input():
    return input("Enter the full input URL: ")

def web_scraper(get_url):
    try:
        response = requests.get(get_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'td', 'tr', 'div'])
        clean_text = '\n\n'.join([element.get_text(separator=" ", strip=True) for element in elements])

        print(f"\nContent from {get_url}")
        print("="*50) 
        print(clean_text)

        with open("content.txt", "w", encoding="utf-8") as file:
            file.write(clean_text)
        print("\n Scraped content saved to 'content.txt'!")

    except requests.exceptions.HTTPError as err:
        print(f" HTTP Error Code: {err}")
    except Exception as e:
        print(f" Error occurred while parsing HTML: {e}")

if __name__ == "__main__":
    get_url = user_input().strip()
    if not get_url:
        print(" Error: URL cannot be empty!")
    else:
        web_scraper(get_url)

    