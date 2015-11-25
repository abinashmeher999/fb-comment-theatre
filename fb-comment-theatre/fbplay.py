import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import pysrt
from bs4 import BeautifulSoup

##############
num_actors = 2
srt_file = './tmr.srt'
timeline = 'https://www.facebook.com/username'
##############

def fb_login(browser, username, password):
    username_field = browser.find_element_by_id('email')
    username_field.click()
    username_field.send_keys(username)
    password_field = browser.find_element_by_id('pass')
    password_field.click()
    password_field.send_keys(password)
    login_btn = browser.find_element_by_id('loginbutton')
    login_btn.click()

def startPlay():
    myproxy = "10.3.100.207:8080"
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myproxy,
        'ftpProxy': myproxy,
        'sslProxy': myproxy,
        'noProxy': ''
        })
    try:
        browsers = []
        for i in range(0, num_actors):
            browsers.append(webdriver.Firefox(proxy=proxy))
        print("Connection with Firefox Browser Succeeded")
    except Exception, e:
        print e
        for browser in browsers:
            browser.close()
        print("Connection with Firefox Failed")
        sys.exit()

    try:
        url = 'http://www.facebook.com'
        for browser in browsers:
            browser.get(url)
        fb_login(browsers[0], )
        #fb_login(browsers[1], )
        browsers[0].get(timeline)
        name_elem = browsers[0].find_element_by_id('fb-timeline-cover-name')
        print name_elem.text

        time.sleep(10)
        print("Successfully Logined into Facebook.com")

    except KeyboardInterrupt:
        for browser in browsers:
            browser.close()

    for browser in browsers:
        browser.close()

if __name__ == "__main__":
    startPlay()
    #subs = pysrt.open(srt_file)
    #for subtitle in subs:
        #print subtitle.text
        #time.sleep(0.5)


