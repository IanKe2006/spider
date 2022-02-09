import requests
from bs4 import BeautifulSoup as soup

def GetPage(url):
  response = requests.get(url)
  doc = soup(response.text, "html.parser") 
  return doc

url = "http://www.stockq.org/market/cryptocurrency.php" #虛擬貨幣行情

myPage = GetPage(url)
result = myPage.select("table.marketdatatable td")

print('貨幣\t\t\t代碼\t\t價格(USD)\t一日\t\t七日\t\t總市值\t\t成交量(24h)')
print('====================\t==========\t==========\t==========\t==========\t==========\t==========')
r = 19    #資料第一列
colEnd = 7  #每列有7行資料
for row in range(0,8):  #只顯示前8列資料
  dataText = ''
  for col in range(0,colEnd):
    data = r + (row * colEnd + col)
    if data > 19 and col == 0:
      r = r + 2 #每列的前兩行不顯示內容(原網頁為編號或圖片，不顯示)
    data = r + (row * colEnd + col)
    #print(data)
    s = result[data].getText().strip()  #只取文字內容以及清除空白字
    if col == 0:
      s = s.replace('\n','')
      if len(s)<=6: #為顯示比較好看進行調整格式
        dataText = dataText + s + '\t\t\t'
      elif len(s)<13:
        dataText = dataText + s + '\t\t'
      else:
        dataText = dataText + s + '\t'
    else:
      dataText = dataText + s + '\t\t'
  print(dataText)