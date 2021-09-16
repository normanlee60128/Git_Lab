from bs4 import BeautifulSoup
import requests
 
 
class Stock:
    #建構式
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers
    
    #爬取
    def scrape(self):
	response = requests.get("https://tw.stock.yahoo.com/q/q?s=2451")
	soup = BeautifulSoup(response.text.replace("加到投資組合", ""), "lxml")