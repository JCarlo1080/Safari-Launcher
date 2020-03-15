#!/bin/zsh/python3

from selenium import webdriver

browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')    
browser.get('https://www.youtube.com')

class Safari():
    def __init__(self):
        self.driver = webdriver.Safari()
    def play(self):
        name = input ('enter a youtube name: ')
        self.driver.get('https://www.youtube.com/user/'+name+'/videos')
        
bot = Safari() 
bot.play
