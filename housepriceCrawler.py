#開啟輸出txt檔
f = open('data.txt', 'w',encoding = 'utf-8')  
#爬5頁的資料
for i in range(5):
    name_list = []
    address_list = []
    ping_list = []
    room_list = []
    year_list = []
    temp = 0
    url = "https://www.sinyi.com.tw/buy/list/Tainan-city/Taipei-R-mrtline/03-mrt/default-desc/"+ str(i+1)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    names = soup.select("div.LongInfoCard_TypeMobile div.LongInfoCard_Type_Name")
    addresses = soup.select("div.LongInfoCard_TypeMobile div.LongInfoCard_Type_Address")
    information = soup.select("div.LongInfoCard_TypeMobile div.LongInfoCard_Type_HouseInfo span")
    print(url)

    for name in names :
        name_list.append(name.text)
    for address in addresses :
        address_list.append(address.text)
#從information中分別取3種資料
    for info in information:
        if temp%3 == 0:
            ping_list.append(info.text)
        elif temp%3 == 1:
            room_list.append(info.text)
        else:
            year_list.append(info.text)
        temp+=1
 #結合資料       
    for j in range (len(name_list)):
        house = [name_list[j],address_list[j],ping_list[j],room_list[j],year_list[j]]
        print(house)
#將資料寫入txt檔
        f.write(str(house)+"\n")
#關閉txt檔
f.close()