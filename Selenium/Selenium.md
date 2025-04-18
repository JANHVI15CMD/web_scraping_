
#  Selenium – Complete Notes for Web Scraping & Automation

---

##  What is Selenium?

Selenium is a powerful open-source **Python tool** that automates browser actions.

 It allows you to:
- Open websites like a human
- Click buttons, fill forms, scroll, take screenshots
- Scrape **dynamic content** loaded via JavaScript (which BeautifulSoup/Requests can’t do)

 **Think of it as a robot that controls your web browser for you.**

---

##  Why Use Selenium for Web Scraping?

| Feature | Explanation |
|--------|-------------|
| Handles JavaScript | Works with dynamic, JS-loaded websites |
| Interacts like a Human | Can click, scroll, type, hover, etc. |
| Works with All Browsers | Chrome, Firefox, Edge, Safari |
| Supports Waits | Handles slow-loading elements with waits |
| Extracts Final HTML | Gets content after all JavaScript has loaded |

---

##  How to Set Up Selenium

###  Step 1: Install Selenium

Open your terminal or VS Code terminal and run:

```bash
pip install selenium
```

---

###  Step 2: Install ChromeDriver (Match your browser version)

You need **ChromeDriver** to control Google Chrome via Selenium.

### Option A: Manual Method

1. Go to: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
2. Download version that matches your browser
3. Extract and keep it somewhere (e.g., `C:\webdriver`)
4. Add that folder to system `PATH`

### Option B ( Recommended): Install via Chocolatey (Windows only)

---

##  What is Chocolatey?

Chocolatey is a **package manager for Windows**, like `apt` for Ubuntu or `brew` for Mac.

- It lets you install tools like Node.js, ChromeDriver, Python, etc., from the terminal.
- No need to manually download .exe files or set up paths.

###  Install Chocolatey (Only once)

Open **PowerShell as Administrator** and run:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

###  Install ChromeDriver using Chocolatey

```bash
choco install chromedriver
```

That’s it — ChromeDriver is installed and automatically added to your system `PATH`.

---

##  How to Use Selenium With Logged-in Chrome Browser

By default, Selenium opens a fresh browser with no login, history, or bookmarks.

###  To use your **logged-in browser profile**:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:/Users/YOUR_USERNAME/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Default")  # Or "Profile 1", etc.

driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com")
```

 You will now be logged into YouTube, Gmail, etc.

---

##  Locating Elements

To interact with anything, you must first **locate it**.

| Locator | Example | Description |
|--------|---------|-------------|
| `id` | `By.ID, "email"` | Fastest, most reliable |
| `name` | `By.NAME, "username"` | Use when id not available |
| `class` | `By.CLASS_NAME, "btn"` | For CSS-based elements |
| `tag` | `By.TAG_NAME, "a"` | For all `<a>` tags |
| `XPath` | `By.XPATH, "//input[@type='text']"` | Most flexible for deep or complex tags |
| `CSS Selector` | `By.CSS_SELECTOR, "div > p.text"` | Cleaner and faster than XPath |

---

##  Interacting with Elements

### Type in Input Field

```python
from selenium.webdriver.common.by import By
element = driver.find_element(By.ID, "email")
element.send_keys("test@example.com")
```

### Clear Field

```python
element.clear()
```

### Click Button

```python
driver.find_element(By.ID, "submit").click()
```

### Press ENTER

```python
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.ENTER)
```

---

##  Handle Dropdowns and Multi-Select

```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "menu"))

dropdown.select_by_index(1)
dropdown.select_by_value("option1")
dropdown.select_by_visible_text("Option 1")

# Deselect for multi-select
dropdown.deselect_all()
```

---

##  Scroll the Page

### Scroll to Element:

```python
driver.execute_script("arguments[0].scrollIntoView();", element)
```

### Scroll Down/Up by Pixels:

```python
driver.execute_script("window.scrollBy(0, 500)")  # scroll down
driver.execute_script("window.scrollBy(0, -500)") # scroll up
```

### Scroll to Page Bottom:

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

---

##  Waits in Selenium

| Type | Usage | Description |
|------|-------|-------------|
| **Implicit Wait** | `driver.implicitly_wait(10)` | Waits up to 10s for all elements |
| **Explicit Wait** | Uses condition | Waits until specific condition is met |
| **Sleep** | `time.sleep(5)` | Not recommended — slows down scripts |

### Example (Explicit Wait):

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "submit"))
)
```

---

##  Handle Alerts

```python
alert = driver.switch_to.alert
alert.accept()        # Click OK
alert.dismiss()       # Click Cancel
alert.text            # Get alert text
alert.send_keys("Hi") # For prompt alerts
```

---

##  Frames & IFrames

If an element is inside an `<iframe>`, you must switch into it:

```python
driver.switch_to.frame("iframe_id_or_name")
# Interact with elements here
driver.switch_to.default_content()  # Back to main page
```

---

##  Testing Tools Comparison

| Tool | Purpose |
|------|---------|
| **Command Prompt (cmd)** | Basic Windows shell. Can run Python, pip |
| **PowerShell** | Advanced version of cmd with extra scripting power |
| **VS Code Terminal** | Built-in terminal in Visual Studio Code. Can run cmd, PowerShell, Git Bash etc. |

 You can switch between them in VS Code from the dropdown in the terminal tab.

---

##  Best Practices

-  Use **Explicit Waits**, not `sleep()`
-  Hide sensitive info like passwords using `.env` or `os.environ`
-  Use `try-except` blocks to catch and handle errors
-  Run browser in headless mode for faster scraping
-  Use Page Object Model for big projects
-  Use browser **DevTools → Inspect** to find tags and classes

---

