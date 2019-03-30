import requests
from bs4 import BeautifulSoup
import getpass
import re

# 設定
url  = "https://ilearn2.fcu.edu.tw/login/index.php"
while 1:

    username = input('請輸入學號NID:')
    password = getpass.getpass('請輸入密碼:')
    max_teachers = 2

     # 建立Session物件
    s = requests.Session()
    # 透過 GET 取得 loginData
    r_login = s.get(url)
    # print(res.cookies)
    loginData = BeautifulSoup(r_login.text,'html.parser')
    #print(loginData)

    # 打包帳密與logintoken
    data = {
        'username':username,
        'password':password,
        'logintoken':loginData.find('form',id='login').find_all('input')[-1]['value'],
    }

    #登入並建立存取課程頁面的物件
    r = s.post(url,data=data)
    CourseData = BeautifulSoup(r.text,'html.parser')
    course_url = "https://ilearn2.fcu.edu.tw/user/index.php?"


    #逐一進入所有課程，抓下老師與課程名稱再輸出
    try:
        for course in CourseData.find('div',id='custom_menu_courses').find_all('li')[0].find_all('a')[2:]:
            number = re.search(r"[0-9][0-9]+",course['href']).group()     
            member_url = course_url+"id={}".format(number)
            r_course = s.post(member_url,data=data)
            MemberData = BeautifulSoup(r_course.text,'html.parser')
            course_name = MemberData.find('h1').text
            course_id = MemberData.find('form',id='formatmenu').find('input')['value']
            teacher_url = "contextid={}&roleid=3".format(course_id)
            r_teacher = s.post(course_url+teacher_url,data=data)
            TeacherData = BeautifulSoup(r_teacher.text,'html.parser')
            string = "課程名稱：{}".format(course_name)
            string += "教師："
            for index,row in enumerate(range(max_teachers)):
                try:
                    teacher = TeacherData.find('td',id="user-index-participants-{}_r{}_c1".format(number,str(row))).text

                    if index and teacher:
                        string += ('、')
                    string += teacher
                except:
                    pass
            print(string)
        break

    except:
        print("try again")
        continue