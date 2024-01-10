from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Set up the browser
driver = webdriver.Chrome()

# Open the Instagram profile URL
url = "https://www.instagram.com/guviofficial/"
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Find the followers and following count using Xpath
followers_xpath = "//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[2]//button[1]"
following_xpath = "//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[3]//button[1]"

followers_count = driver.find_element(By.XPATH, followers_xpath).text
following_count = driver.find_element(By.XPATH, following_xpath).text

# Print the results
print("Followers count:", followers_count)
print("Following count:", following_count)

# Close the browser window
driver.quit()