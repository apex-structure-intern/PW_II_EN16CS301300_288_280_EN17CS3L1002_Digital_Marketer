# Enter numbers in whatsapp.xlsx or replace it with another file
import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key,Controller


class Whatsapp:
    def __init__(self):
        self.keyboard=Controller()
        wb=xlrd.open_workbook("Whatsapp.xlsx")
        self.sheet=wb.sheet_by_index(0)
        self.numr=self.sheet.nrows
        driverpath="/usr/bin/chromedriver"
        self.driver=webdriver.Chrome(driverpath)
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(10)

    def send(self, message):
        for i in range(self.numr):
            number=self.sheet.cell_value(i,0)
            number=int(number)
            time.sleep(20)
            elem =self.driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
            elem.send_keys(number)
            time.sleep(5)
            elem.send_keys("\n")
            elem=self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            elem.send_keys(message)
            time.sleep(5)
            elem.send_keys("\n")
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)

if __name__ == "__main__":
    obj = Whatsapp()
    obj.send("I don't know what to do!!!")
