import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# click on tab page 
def scroll_to_block(name):
    element = driver.find_element(By.ID, name)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)

#put value to imput 
def put_text_to_input(name_of_imput, resolved_text):
    imput = driver.find_element(By.ID, name_of_imput)
    imput.send_keys(resolved_text)
    time.sleep(1)

# click on element's
def cick_on_element(name_of_element):
    element = driver.find_element(By.ID, name_of_element)
    element.click()
    time.sleep(1)


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the Python website
driver.get("http://localhost:8081")

# Print the page title
print("Result of search")
print(driver.title)

scroll_to_block("portfolio")
scroll_to_block("contact")
scroll_to_block("about")
scroll_to_block("name")

put_text_to_input("name","Ваня Щаников")
put_text_to_input("phone","88005553535 ")
put_text_to_input("email","idapen@ithub.ru")
put_text_to_input("message","Длинный текст тут. Длинный текст тут.")

scroll_to_block("submitSuccessMessage")

cick_on_element("submitSuccessMessage")

time.sleep(10)


# # Find the search bar using its name attribute
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)

# # Print the current URL
# print(driver.current_url)

# Close the browser window
driver.close()
