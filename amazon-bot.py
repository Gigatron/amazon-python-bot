from selenium import webdriver
from time import sleep

CARD_TO_BUYS = [
    "https://www.amazon.com/MSI-GeForce-RTX-3060-12G/dp/B08WPJ5P4R/ref=sr_1_2?dchild=1&keywords=3060+rtx&qid=1619637512&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sr=8-2",
    "https://www.amazon.com/ASUS-Graphics-DisplayPort-Military-Grade-Certification/dp/B08WHJPBFX/ref=sr_1_1?dchild=1&keywords=asus+3060+rtx&qid=1619637575&sr=8-1",
    "https://www.amazon.com/EVGA-GeForce-12G-P5-3657-KR-Dual-Fan-Backplate/dp/B08WM28PVH/ref=sr_1_2?dchild=1&keywords=evga+3060+rtx&qid=1619637588&sr=8-2"
]
SLEEP_IN_BETWEEN = 5


class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.com')
        sleep(50)

    def checkAndBuyPS5(self):
        while True:
            for card in CARD_TO_BUYS:
                self.driver.get(card)
                sleep(1)   
                try:
                    buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
                    buyNow.click()
                    sleep(2)
                    buyNow2 = self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn"]')
                    buyNow2.click()
                    sleep(2)
                    buyNow3 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input')  
                    buyNow3.click()
                    sleep(1)
                    self.driver.close()
                except Exception as e:
                    print(e)
                    sleep(1.5)
            sleep(SLEEP_IN_BETWEEN)
            
bot = PS5Bot()
bot.login()
bot.checkAndBuyPS5()
