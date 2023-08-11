import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Replace 'url_here' with the actual URL you want to extract emails from
url = 'https://apps.shopify.com/judgeme'
response = requests.get(url)
content = response.text

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all email addresses using regular expression
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emails_found = re.findall(email_pattern, soup.get_text())

# Create a DataFrame to store the results
data = {'Emails': emails_found}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
email_addresses = 'email_addresses.xlsx'
df.to_excel(email_addresses, index=False)

print(f"Email addresses saved to '{email_addresses}'")
