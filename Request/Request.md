
#  Primer on Web

##  1. Client-Server Architecture

- The **Client-Server Model** is the backbone of modern web and network communication.
  
###  Client:
- A **client** (like a browser or mobile app) sends requests to a server.
- Example: Chrome, Firefox, Postman, or a mobile app making API calls.

###  Server:
- A **server** listens and responds with data (HTML page, JSON, image, etc.).
- Example: Google’s web servers responding with search results.

###  How It Works:
- Client sends a **request** (like “get me the homepage”)
- Server sends back a **response** (the HTML content of the homepage)

---

##  2. HTTP: Request & Response

HTTP (Hypertext Transfer Protocol) enables **data exchange** between a client and a server.

###  HTTP Request
- Sent **from client to server**
- Contains:
  - **Method** (e.g., GET, POST)
  - **URL** (the resource address)
  - **Headers** (extra metadata)
  - **Body** (optional – like form data)

###  HTTP Response
- Sent **from server to client**
- Contains:
  - **Status Code** (e.g., 200 OK)
  - **Headers**
  - **Body** (content/data, often HTML or JSON)

---

##  3. HTTP Methods (aka HTTP Verbs)

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Load a webpage |
| **POST** | Submit data | Submit a form |
| **PUT** | Update data (replace) | Update a full profile |
| **PATCH** | Update data (partial) | Change email only |
| **DELETE** | Remove resource | Delete a post |

---

##  4. HTTP Status Codes

These 3-digit codes tell you the **result of a request**.

###  Success Codes (2xx)
| Code | Meaning |
|------|---------|
| 200 | OK (Success) |
| 201 | Created (New Resource Created) |

###  Redirection (3xx)
| Code | Meaning |
|------|---------|
| 301 | Moved Permanently |
| 302 | Found (Temporarily moved) |

###  Client Errors (4xx)
| Code | Meaning |
|------|---------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |

###  Server Errors (5xx)
| Code | Meaning |
|------|---------|
| 502 | Bad Gateway |
| 503 | Service Unavailable |

---

##  5. Core Web Technologies

These three technologies are the foundation of modern web pages:

###  HTML (HyperText Markup Language)
- Gives **structure** to web content.
- Uses tags like `<h1>`, `<p>`, `<a>`, `<img>`.

###  CSS (Cascading Style Sheets)
- Handles **style and layout**: colors, fonts, spacing.
- Example: Turn a plain page into a beautiful UI.

###  JavaScript
- Adds **interactivity and logic**.
- Used for:
  - Dynamic content loading
  - Validating forms
  - Handling events like clicks

---

##  Why This Matters for Web Scraping?

- **HTML knowledge** helps locate the data to scrape.
- **CSS selectors** help target specific elements.
- **JavaScript knowledge** is essential for scraping **dynamic websites** (using tools like Puppeteer or Selenium).

---


#  Python `requests` Module – Web Scraping Essential

##  What is `requests`?

- A simple, powerful, and beginner-friendly Python library for sending **HTTP requests**.
- Makes working with web data easier than using `urllib`.

###  Key Features:
-  **Simple Syntax** – Easy for beginners to understand.
-  **Session Management** – Persist cookies & auth across multiple requests.
-  **Automatic Content Decoding** – No need to handle encodings manually.
-  **Built-in Error Handling** – Catch common errors like 404, 500, etc.
-  **Wide Community Support** – Tons of tutorials and documentation.

---

##  Common Applications of `requests`

1. **Web Scraping**
   - Retrieve HTML content to parse using `BeautifulSoup`, `lxml`, etc.

2. **API Interaction**
   - Communicate with REST APIs using `GET`, `POST`, etc.
   - Example: Fetching data from Twitter API.

3. **File Uploads**
   - Easily send files to a server using a form.

4. **Session-Based Auth**
   - Maintain login sessions across multiple requests (e.g., user login scraping).

5. **Form Submission**
   - Send data to a form on a website.

---

##  GET Requests with Query Parameters

```python
import requests

params = {'brand': 'samsung', 'price': 'under_15000'}
response = requests.get("https://example.com/products", params=params)
print(response.text)
```

- `params` are added after `?` in the URL.
- Use it to **filter/search** content.

---

##  POST Requests to Send Data

```python
data = {'username': 'john', 'password': 'secret'}
response = requests.post("https://example.com/login", data=data)
print(response.status_code)
```

###  Sending JSON:
```python
json_data = {'name': 'John', 'email': 'john@example.com'}
response = requests.post("https://example.com/api", json=json_data)
```

- Use `data` for form-like data
- Use `json` to send structured JSON

---

##  HTTP Headers in `requests`

Headers = Extra info sent with the request (like ID card for the client).

###  Common Headers:

| Header | Purpose |
|--------|---------|
| `Authorization` | Pass tokens, API keys |
| `Content-Type` | Type of data being sent (`application/json`) |
| `User-Agent` | Info about the client/browser |
| `Accept` | Tells server what type of response to send |

###  Example:
```python
headers = {
  'Authorization': 'Bearer my_token',
  'Content-Type': 'application/json',
  'User-Agent': 'MyApp/1.0'
}
response = requests.get("https://example.com/api", headers=headers)
```

### Tips:
- Always read API docs for required headers.
- Incorrect headers can trigger 401, 403, or 415 errors.

---

