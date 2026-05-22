# Web Scraping

Tools: `requests`, `beautifulsoup4` (`bs4`), `lxml`.

```python
import requests
import bs4

result = requests.get("https://example.com")
```

## Inspecting the response

```python
print(result.status_code)   # 200
print(result.ok)
print(result.url)
print(result.headers)
print(result.encoding)
print(result.text)          # decoded body
print(result.content)       # raw bytes
result.raise_for_status()   # raises on 4xx/5xx
```

## Parsing with BeautifulSoup

```python
soup = bs4.BeautifulSoup(result.text, "lxml")
soup.select('title')                  # list of matches
soup.select('title')[0].getText()     # text inside the tag

type(soup)                  # bs4.BeautifulSoup
type(soup.select('title'))  # bs4.element.ResultSet
```

## CSS-style selectors

| Syntax | Match |
|---|---|
| `soup.select('div')` | All `<div>` elements |
| `soup.select('#some_id')` | The element with `id="some_id"` |
| `soup.select('.notice')` | All elements with CSS class `notice` |
| `soup.select('div span')` | `<span>` anywhere inside a `<div>` |
| `soup.select('div > span')` | `<span>` **directly** inside a `<div>` |

## Setting a User-Agent

Generic agents like `python-requests/x.y` are often blocked.

```python
url = "https://en.wikipedia.org/wiki/Grace_Hopper"
headers = {"User-Agent": "LearningScraper/0.1 (your_email@example.com) requests"}
res = requests.get(url, headers=headers, timeout=10)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
for item in soup.select('.vector-toc-text'):
    print(item.text)
```

## Downloading an image

```python
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg"
res_image = requests.get(url, headers=headers, timeout=10)

with open('my_computer_file.jpg', 'wb') as f:
    f.write(res_image.content)
```

> **Respect site policies**
>
> Wikipedia and many sites enforce robot policies and rate limits. Read each site's `robots.txt` and terms of service before scraping at scale.

