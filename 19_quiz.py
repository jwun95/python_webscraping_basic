import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")


for index, row in enumerate(data_rows):
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        print(f"=========== 매물 {index+1} ===========")
        print(f"거래:{data[0]}")
        print(f"공급/전용면적:{data[1]}")
        print(f"매물가(만원):{data[2]}")
        print(f"동:{data[3]}")
        print(f"층:{data[4]}")

