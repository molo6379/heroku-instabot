from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

chrome_path = r'C:\Users\molo6\Desktop\Untitled Folder\chromedriver'
browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

browser.implicitly_wait(5)
browser.get_screenshot_as_file('insta_main.png')

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("cat_cocochxnel")
password_input.send_keys("qkqhd921^^@")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

browser.implicitly_wait(15)

login_info = browser.find_element_by_xpath("//button[text()='나중에 하기']")
login_info.click()

browser.implicitly_wait(15)

# alarm_setting = browser.find_element_by_xpath("//button[text()='나중에 하기']")
# alarm_setting.click()

browser.implicitly_wait(15)

search_input = browser.find_element_by_css_selector("input[placeholder='검색']")
search_input.send_keys("#개스타그램")

browser.implicitly_wait(15)

tag_click = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
tag_click.click()

browser.implicitly_wait(15)

first_recent_pic = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]")
first_recent_pic.click()

cycle = random.randint(3, 6)

while True:
    for i in range(random.randint(20,30)):
        browser.implicitly_wait(5)
        try:
            like_button = browser.find_element_by_css_selector("svg[aria-label='좋아요']")
            like_button.click()
        except:
            pass
        sleep(random.randint(2,5))
        next_button = browser.find_element_by_xpath("//a[text()='다음']")
        next_button.click()
    cycle -= 1
    if cycle == 2:
        sleep(random.randint(900, 1500))
        cycle = random.randint(3,6)
    exit_button = browser.find_element_by_css_selector("svg[aria-label='닫기']")
    exit_button.click()
    browser.refresh()
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]").click()