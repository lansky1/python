# Web Scraping, Images & Email

## Web Scraping

Stack: `requests`, `bs4` (BeautifulSoup), `lxml` parser.

```python
import requests
import bs4
```

```python
result = requests.get("https://example.com")
```

A `Response` object exposes a lot of metadata:

```python
print(result.apparent_encoding)
print(result.connection)
print(result.content)
print(result.cookies)
print(result.elapsed)
print(result.encoding)
print(result.headers)
print(result.history)
print(result.is_permanent_redirect)
print(result.json)
print(result.raw)
print(result.ok)
print(result.url)
print(result.text)
print(result.raise_for_status)
print(result.status_code)   # 200
```

Parse the HTML:

```python
soup = bs4.BeautifulSoup(result.text, "lxml")
soup
soup.select('title')              # returns a list of matches
soup.select('title')[0].getText()
```

```python
type(soup)                          # bs4.BeautifulSoup
type(soup.select('title'))          # bs4.element.ResultSet
type(soup.select('title')[0])       # bs4.element.Tag
type(soup.select('title')[0].getText())  # str
```

### CSS selectors with `.select()`

| Syntax | Match Results |
| --- | --- |
| `soup.select('div')` | All `<div>` elements |
| `soup.select('#some_id')` | The element with `id="some_id"` |
| `soup.select('.notice')` | All elements with CSS class `notice` |
| `soup.select('div span')` | Any `<span>` descendants of a `<div>` |
| `soup.select('div > span')` | Any `<span>` that is a **direct** child of a `<div>` |

### Sending a real User-Agent

Generic agents like `python-requests/x` may be blocked. Set a descriptive header:

```python
url = "https://en.wikipedia.org/wiki/Grace_Hopper"

headers = {
    "User-Agent": "LearningScraper/0.1 (your_email@example.com) requests"
}

res = requests.get(url, headers=headers, timeout=10)
res.raise_for_status()
```

```python
soup = bs4.BeautifulSoup(res.text, "lxml")
soup.select('.vector-toc-text')[1].text
```

```python
for item in soup.select('.vector-toc-text'):
    print(item.text)   # or .getText()
```

### Downloading images via the parsed page

```python
url = "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)"

headers = {
    "User-Agent": "LearningScraper/0.1 (your_email@example.com) requests"
}

res = requests.get(url, headers=headers, timeout=10)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
```

```python
type(soup.select('.mw-file-element')[1])
soup.select('.mw-file-element')[1]['src']   # use img tag in markdown to render
```

```python
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg"

headers = {
    "User-Agent": "LearningScraper/0.1 (your_email@example.com) requests"
}

res_image = requests.get(url, headers=headers, timeout=10)

with open('my_computer_file.jpg', 'wb') as f:
    f.write(res_image.content)
```

> Wikipedia's robot policy can still block downloads even with a custom User-Agent. Respect `robots.txt`.

## Working With Images

Using **Pillow** — a fork of the Python Imaging Library (PIL).

```python
# blue = Image.open('blue_color.png')
# blue_new = blue.convert('RGB')
# blue_new.save("blue_new.jpg")
# blue = Image.open('blue_new.jpg')
```

```python
from PIL import Image
mac = Image.open('example.jpg')
type(mac)
# PIL.JpegImagePlugin.JpegImageFile
```

```python
# mac.show()   # opens in desktop image viewer
mac
```

```python
print(mac.size)                # (1993, 1257)
print(mac.format_description)  # JPEG (ISO 10918)
print(mac.filename)            # example.jpg
```

### Cropping

```python
mac.crop((0, 0, 100, 100))
# Measuring from top-left corner (0, 0)
# Returns: <PIL.Image.Image image mode=RGB size=100x100>
```

```python
pencils = Image.open('pencils.jpg')
width, height = pencils.size

# (left, upper, right, lower) in pixel coordinates
pencils.crop((0, 0, width / 3, height / 10))
pencils.crop((0, 1100, width / 3, height))
```

```python
width_mac, height_mac = mac.size
# 1993, 1257
computer = mac.crop((width_mac / 10 * 4 + 40,
                     height_mac / 10 * 6.5,
                     width_mac / 10 * 6 - 10,
                     height_mac))
```

### Pasting, resizing, rotating

```python
mac.paste(im=computer, box=(0, 0))
mac

mac.resize((3000, 500))
mac.rotate(90)
```

### Color transparency

```python
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

red.putalpha(0)   # full transparency
red

blue.paste(im=red, box=(0, 0), mask=red)
blue
# <PIL.PngImagePlugin.PngImageFile image mode=PA size=200x200>

# blue.save("...")   # save (and overwrite if filename already exists)
```

## Sending Email — `smtplib`

```python
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)   # 587 = TLS, 465 = SSL
smtp_object.ehlo()
# (250, b'smtp.gmail.com at your service, ...')

smtp_object.starttls()
# (220, b'2.0.0 Ready to start TLS')

import getpass
email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')

smtp_object.login(email, password)
```

```python
from_address = email
to_address = ''
subject = ''
message = ''
msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_addr=from_address, to_addrs=to_address, msg=msg)
# Returns an empty dictionary on success
```

```python
smtp_object.quit()
```

## Receiving Email — `imaplib`

```python
import imaplib   # or use the higher-level `email` module
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')

M.login(email, password)
M.list()
M.select('inbox')
```

### Search keywords

| Keyword | Definition |
| --- | --- |
| `'ALL'` | Returns all messages in your folder. Often there are size limits from `imaplib`. To raise them: `imaplib._MAXLINE = 100` (or whatever you need). |
| `'BEFORE date'` | Returns all messages before the date. Date must be formatted as `01-Nov-2000`. |
| `'ON date'` | Returns all messages on the date. |
| `'SINCE date'` | Returns all messages after the date. |
| `'FROM string'` | Returns all messages from the sender. String can be an email or a fragment. |
| `'TO string'` | Returns all outgoing email to the recipient. |
| `'CC string'` and/or `'BCC string'` | Search by CC/BCC. |
| `'SUBJECT string'`, `'BODY string'`, `'TEXT "string with spaces"'` | Subject/body/text search. Wrap multi-word strings in double quotes. |
| `'SEEN'`, `'UNSEEN'` | Read or unread. |
| `'ANSWERED'`, `'UNANSWERED'` | Replied or not. |
| `'DELETED'`, `'UNDELETED'` | Deleted or not. |

You can combine these with logical `AND` and `OR`. Full list: [IMAPTransporter — Authorized search keys](https://developer.4d.com/docs/API/IMAPTransporterClass#authorized-search-keys).

```python
type, data = M.search(None, 'BEFORE 01-Nov-2000')
type, data = M.search(None, 'FROM example')
type, data = M.search(None, 'SUBJECT "example"')
```

```python
result, email_data = M.fetch(data[0], '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
```

```python
import email

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':   # also 'text/html'
        body = part.get_payload(decode=True)
        print(body)
```
