📂 PriceHawk — Amazon Price Tracker 🦅
PriceHawk is a simple Python tool that tracks product prices on Amazon and sends you an email alert when the price drops below your target.

✅ How It Works
Scrapes an Amazon product page using requests + BeautifulSoup + Selenium.

Extracts the latest price.

Compares it to your target price.

Sends you an email if the price is lower.

📦 Project Structure
bash
Copy
Edit
PriceHawk/
 ├── scraper/
 │   └── scraper.py       # Main price checker script
 ├── selenium_runner/
 │   └── price_scraper.py # Selenium price extractor
 ├── README.md
 
🚀 Setup Instructions
1️⃣ Clone this repo
bash
Copy
Edit
git clone https://github.com/YourUsername/PriceHawk.git
cd PriceHawk
2️⃣ Install requirements
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Create .env
Add your Gmail App Password and emails:
Create a .env file in the project root:

env
Copy
Edit
EMAIL_PASS=your_gmail_app_password
EMAIL_USER=your_gmail@gmail.com
EMAIL_RECIPIENT=recipient_email@gmail.com
✅ Use an App Password:

How to create a Gmail App Password

4️⃣ Update your product URL and target price
Open scraper/scraper.py and edit:

python
Copy
Edit
URL = 'YOUR_AMAZON_PRODUCT_URL'

# Set your target price (in INR)
if price_int < YOUR_TARGET_PRICE:
    send_mail()
5️⃣ Update sender and recipient in scraper.py
Edit send_mail() to use environment variables:
Change:

python
Copy
Edit
server.login('w61931333@gmail.com', email_password)
server.sendmail(
    'w61931333@gmail.com',
    'besharam202@gmail.com',
    msg
)
✅ Replace with:

python
Copy
Edit
server.login(os.environ.get('EMAIL_USER'), email_password)
server.sendmail(
    os.environ.get('EMAIL_USER'),
    os.environ.get('EMAIL_RECIPIENT'),
    msg
)
Now your email credentials and recipient come from .env — no hardcoding.

6️⃣ Set up Chromedriver for Selenium
Your selenium_runner/price_scraper.py needs Chrome + Chromedriver.

✅ Download Chromedriver:
https://chromedriver.chromium.org/downloads

✅ Make sure:

Chrome is installed.

Chromedriver version matches your Chrome version.

Chromedriver is in your PATH or in the project root.

7️⃣ Run PriceHawk!
bash
Copy
Edit
python scraper/scraper.py
It will scrape the product page.

Compare the price.

Send you an email if the price is lower than your target.

✅ price_scraper.py — What you need to change
Nothing!
You don’t need to edit selenium_runner/price_scraper.py.
Just make sure your Chromedriver works.

📝 .gitignore
Create a .gitignore with:

bash
Copy
Edit
__pycache__/
*.pyc
.env
venv/
Never commit your .env.

📬 Example Output
sql
Copy
Edit
Current Price: 249999
Price fell down!
Hey email has been sent
⚡️ Next Steps
Add a scheduler (cron on Linux, Task Scheduler on Windows) to run it hourly.

Or uncomment the while(True) loop to run continuously.

Extend it to multiple products!

✨ That’s it!
🦅 PriceHawk will now watch your product and email you when it’s a good deal.

📣 License
MIT — use freely!