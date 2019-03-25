import requests
from bs4 import BeautifulSoup
import getpass

username = input('請輸入學號:')
password = getpass.getpass('請輸入密碼:')

url = 'https://ilearn2.fcu.edu.tw/login/index.php'

s = requests.Session()

loginPage = s.get('https://ilearn2.fcu.edu.tw/login/index.php')

bs_loginPage = BeautifulSoup(loginPage.text, "html.parser")

loginData = {
    'username': username,
    'password': password,
    'logintoken': bs_loginPage.find_all("input", attrs={"name": "logintoken"})[0]["value"]
}

#login
s.post('https://ilearn2.fcu.edu.tw/login/index.php', data=loginData)

coursePage = s.get('https://ilearn2.fcu.edu.tw/')
bs_coursePage = BeautifulSoup(coursePage.text, "html.parser")

course = bs_coursePage.select('div.coc-mycurricular')[0].select('div.course')

for i in course:
    print(i.get_text())