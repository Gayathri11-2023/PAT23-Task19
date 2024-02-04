from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class loginautomation:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def sleep(self, seconds):
            sleep(seconds)
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)
    def usernameinputbox(self, value, key):
        self.driver.find_element(by=By.ID, value="user-name").send_keys(key)
        self.sleep(5)
    def passwordinputbox(self, value, key):
        self.driver.find_element(by=By.ID, value="password").send_keys(key)
        self.sleep(5)

    def loginbtn(self):
        self.driver.find_element(by=By.ID, value="login-button").click()
        self.sleep(10)

    # Fetch the title of the web page
    def gettitle(self):
        return self.driver.title


    # Fetch the current url
    def geturl(self):
        return self.driver.current_url


    # Get the page source
    def getpagesource(self):
           return self.driver.page_source

    def save_page_content_to_file(self, filename):
        page_content = self.getpagesource()
        with open(filename, "w", encoding="utf=8") as file:
            file.write(page_content)
        print(f"Page source saved to {filename}")

    def quit(self):
        self.driver.quit()

    # Save the page source to a text file

    def login(self):

        self.boot()
        self.usernameinputbox("username", self.username)
        self.passwordinputbox("password", self.password)
        self.loginbtn()



url = "https://www.saucedemo.com/"

obj = loginautomation(url, "standard_user", "secret_sauce")
obj.login()

# Fetch and print the title of the webpage
title = obj.gettitle()
print("Title of the webpage:", title)

# Fetch and print the current URL of the webpage
current_url = obj.geturl()
print("Current URL of the webpage:", current_url)

# Save the entire content of the webpage to a text file
obj.save_page_content_to_file("webpage_task_11.txt")


'''
url = "https://www.saucedemo.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the desired webpage
driver.get(url)
driver.maximize_window()
sleep(5)

# Find the username input field and enter username
usernameInputBox = driver.find_element(by=By.ID, value="user-name")
usernameInputBox.send_keys("standard_user")
sleep(5)

# Find the password input field and enter password
passwordInputBox = driver.find_element(by=By.ID, value="password")
passwordInputBox.send_keys("secret_sauce")
sleep(5)

# find the login button and click
submitBtn = driver.find_element(by=By.ID, value="login-button")
submitBtn.click()
sleep(10)

# Fetch the title of the web page
title = driver.title
print("Title of the web page:", title)

# Fetch the current url
current_url = driver.current_url
print("Current URL of the webpage:", current_url)

# Get the page source
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Save the page source to a text file
file_name = "webpage_task_11.txt"
with open(file_name,"w", encoding="utf=8") as file:
    file.write(page_source)
print(f"Page source saved to {file_name}")


'''