# Email

## Sending with `smtplib`

```python
import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)  # 587 = TLS; 465 = SSL
smtp_object.ehlo()
smtp_object.starttls()

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email, password)

from_address = email
to_address = ''
subject = ''
message = ''
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_addr=from_address, to_addrs=to_address, msg=msg)
smtp_object.quit()
```

> **App passwords**
>
> Gmail and many providers require a generated *app password*, not your account password. Never hardcode credentials.


## Receiving with `imaplib`

```python
import imaplib
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
M.login(email, password)

M.list()
M.select('inbox')
```

### Search keywords

| Keyword | Meaning |
|---|---|
| `ALL` | All messages (subject to imaplib size limits — raise via `imaplib._MAXLINE`) |
| `BEFORE date` | Before date (format: `01-Nov-2000`) |
| `ON date` | On date |
| `SINCE date` | After date |
| `FROM string` | All from sender containing string |
| `TO string` | All sent to address containing string |
| `CC string` / `BCC string` | CC / BCC match |
| `SUBJECT string`, `BODY string`, `TEXT "with spaces"` | Subject / body / text contains |
| `SEEN`, `UNSEEN` | Read / unread |
| `ANSWERED`, `UNANSWERED` | Replied / unreplied |
| `DELETED`, `UNDELETED` | Marked deleted or not |

You can combine with `AND` and `OR`. Full reference: <https://developer.4d.com/docs/API/IMAPTransporterClass#authorized-search-keys>.

```python
type_, data = M.search(None, 'BEFORE 01-Nov-2000')
type_, data = M.search(None, 'FROM example')
type_, data = M.search(None, 'SUBJECT "example"')
```

### Fetching and parsing a message

```python
import email

result, email_data = M.fetch(data[0], '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':   # or 'text/html'
        body = part.get_payload(decode=True)
        print(body)
```
