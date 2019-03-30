# HW1

## 簡介
 使用 `requests` 及 `BeautifulSoup` 爬取 iLearn 上的課程

## 使用方法
根據提示文字輸入帳密

## 功能
* 顯示目前ilearn裏面該學期所有課程與老師名稱
* 對帳號密碼進行錯誤處理

## 登入原理

### 觀察 登入表單所需資訊
登入通常都要 POST 所以先登入錯誤帳密讓 POST的網頁在開發人員工具->網路顯示出來
觀察登入表單參數發現需要帳密以及 logintoken
而 logintoken 每次都會變
因此先把 logintoken GET下來

### 先建立Session物件
此時會發現透過 POST 還是無法登入，原因是 cookie 每次都會變，因此瀏覽器認爲你是不同人，因此要把 cookie 存起來，每次HTTP時那出 cookie 就可以通行無阻不線次數

利用 Session() 函式存入 cookie，建立登入物件

### 重新取得logintoken
此時有了登入物件就可以先 GET 下 logintoken
再加上帳密打包成 data 還有你的 cookie 身份證透過 POST 成功完成登入

### 登入例外處理
1. 寫一個無限迴圈
2. 如果密碼輸入正確，程式結束跳出迴圈
3. 如果密碼輸入錯誤，繼續執行迴圈

##  輸出範例
   ![](https://i.imgur.com/bl87ZDG.jpg)
