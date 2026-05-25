# Web Scraping — Book Site

Target: [books.toscrape.com](https://books.toscrape.com/), a sandbox catalog designed for scraping practice. The goal here is to collect the titles of every two-star book across the site.

```python
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
```

```python
two_star_titles = []

for n in range(1, 2):   # 51 for full website
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
# ['Starving Hearts (Triangular Trade Trilogy, #1)',
#  'Libertarianism for Beginners',
#  "It's Only the Himalayas"]
```

Notes:

- Each `.product_pod` is one book card on the page. The rating shows up as a CSS class on a `<p>` element (`star-rating Two`, `star-rating Three`, etc.), which is why `.star-rating.Two` works as a selector.
- `book.select('a')[1]['title']` reaches the second `<a>` inside the card — the first is the cover link, the second wraps the title text.
- Scaling up is just a matter of widening the `range(1, 2)` to cover all 50 pages.
