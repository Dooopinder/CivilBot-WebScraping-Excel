"""
Created on Wed Aug  2 02:50:14 2023
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

# Function to convert Indian numeric system values to standard numeric values
def indian_numeric_to_numeric(indian_value):
    if indian_value is None:
        return None
    # Remove the Rupee symbol and commas
    indian_value = indian_value.replace('₹', '').replace(',', '')
    if ' crore' in indian_value:
        return float(indian_value.replace(' crore', '')) * 10000000
    elif ' lakh' in indian_value:
        return float(indian_value.replace(' lakh', '')) * 100000
    else:
        return pd.to_numeric(indian_value, errors='coerce')

# Set up Firefox options
options = Options()
options.headless = True  # Change to True if you want Firefox to run in the background
options.binary_location = 'path/to/Mozilla Firefox/firefox.exe'

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=options)

# Go to a webpage
driver.get("https://etender.cpwd.gov.in/login.html")

wait = WebDriverWait(driver, 10)
# Find the "Tender Information" dropdown menu by its title and hover over it
dropdown_menu = driver.find_element_by_xpath("//li[@title='Tender Information']")
hover = ActionChains(driver).move_to_element(dropdown_menu)
hover.perform()

wait = WebDriverWait(driver, 10)
# Find the "All Tenders" option by its title and click it
all_tenders_option = driver.find_element_by_xpath("//li[@title='All Tenders']")
all_tenders_option.click()

# Wait for the dropdown menu to become available and select the "Region" option
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
dropdown_menu = wait.until(EC.presence_of_element_located((By.ID, "regionORprojectregion")))
dropdown = Select(dropdown_menu)
dropdown.select_by_value("0")  # Select the "Region" option

# Wait for the dropdown menu to become available and select the "New Tenders" option
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
dropdown_menu = wait.until(EC.presence_of_element_located((By.ID, "nStatus")))
dropdown = Select(dropdown_menu)
dropdown.select_by_value("105")  # Select the "New Tenders" option

# Wait for the dropdown menu to become available and select the "Delhi" option
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
dropdown_menu = wait.until(EC.presence_of_element_located((By.ID, "regionID")))
dropdown = Select(dropdown_menu)
dropdown.select_by_value("454") 

# Wait for the "Search" button to become available and click it
wait = WebDriverWait(driver, 12)  # Wait up to 12 seconds
search_button = wait.until(EC.presence_of_element_located((By.ID, "btnSearch")))
search_button.click()

# Wait for the dropdown menu to become available
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
dropdown_menu = wait.until(EC.presence_of_element_located((By.NAME, "awardedDataTable_length")))

# Create a Select object
dropdown = Select(dropdown_menu)

# Select the "50" option
dropdown.select_by_value("50")

# Find the "Estimated Cost(INR)" header and click it to sort
wait = WebDriverWait(driver, 17)
estimated_cost_header = driver.find_element_by_xpath("/html/body/div/div/div[4]/form/div[3]/div/div/div/div/div/table/thead/tr/th[5]")
estimated_cost_header.click()

wait = WebDriverWait(driver, 19)

# Find the table element using XPath
table_xpath = "//table[@id='awardedDataTable']"
table_element = driver.find_element_by_xpath(table_xpath)

# Get the HTML content of the table
html_content = table_element.get_attribute('outerHTML')

# Close the WebDriver
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table_data = []

# Access and show each row of the table
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    row_data = [cell.get_text() for cell in cells]
    table_data.append(row_data)

# Convert the list of lists to a pandas DataFrame
df = pd.DataFrame(table_data)

# Convert column E to numeric values
col_E_numeric = df.iloc[:, 4].apply(indian_numeric_to_numeric)

# Filter the DataFrame based on the specified condition for column E
filtered_df = df[col_E_numeric.between(2e7, 15e7)]

# Save the filtered DataFrame to an Excel file
excel_file = "filtered_table_data1.xlsx"
filtered_df.to_excel(excel_file, index=False)

# Save the DataFrame to an Excel file
excel_file = "table_data.xlsx"
df.to_excel(excel_file, index=False)
