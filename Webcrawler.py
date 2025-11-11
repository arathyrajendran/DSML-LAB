import requests
import lxml
from bs4 import BeautifulSoup
import time # 👈 

url = 'https://www.rottentomatoes.com/top/bestofrt/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

print("Fetching main page...")

try:
    f = requests.get(url, headers=headers)
    f.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching main URL: {e}")
    exit()

movies_lst = []
soup = BeautifulSoup(f.content, 'lxml')

movie_links = soup.select('table.table a[href^="/m/"]') 
num = 0

print(f"Found {len(movie_links)} potential movie links. Starting detail scraping...")
print("-" * 30)

for anchor in movie_links:
    num += 1 
    e
    if 'href' not in anchor.attrs:
        continue 
        
    urls = 'https://www.rottentomatoes.com' + anchor['href']
    movies_lst.append(urls)
    movie_title = anchor.string.strip()
    
    try:
        movie_f = requests.get(urls, headers=headers, timeout=10) 
        movie_f.raise_for_status()
        movie_soup = BeautifulSoup(movie_f.content, 'lxml')
        
        movie_content = movie_soup.find('div', {'class': 'movie-synopsis clamp clamp-6 js-clamp'})
        
        synopsis = movie_content.string.strip() if movie_content else "Synopsis not found."
        
        print(f"{num}. Movie: {movie_title}")
        print(f"   Movie URL: {urls}")
        print(f"   Movie Info: {synopsis}")
        
    except requests.exceptions.RequestException as e:
        print(f"   [ERROR] Could not fetch data for {movie_title} ({urls}): {e}")
        synopsis = "Failed to fetch or parse."
    
    print("-" * 30)
    
    if num < len(movie_links): 
        time.sleep(2) 

print("Scraping complete!")