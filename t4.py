import requests
from bs4 import BeautifulSoup
import openpyxl

def aip(url,limita=6):
    raspuns = requests.get(url)
    if raspuns.status_code == 200:
        soup = BeautifulSoup(raspuns.text,"html.parser")
        en = soup.find_all("a",class_="item-article_title")

        i_p=[]
        index = 0

        for ne in en:
            nume = ne.get_text(strip=True)
            i_p.append({"Title": nume})

            index += 1

            if index >= limita:
                return i_p
            
        return i_p
    else:
        print("Cererea HTTP a esuat.Cod de stare",raspuns.status_code)
        return None
def se(i_p,n_f="/home/tempus/lab/Map-py/t4/ex.xlsx"):
    if i_p:
        workout  = openpyxl.Workbook()
        sheet = workout.active
        sheet.title = "News titles"
        sheet["A1"] = "Ultimele stirii de pe PRO.TV"

        row = 2

        for produs in i_p:
            sheet[f"A{row}"] = f"{produs}"
            row += 1
        
        workout.save(n_f)
        print("{n_f} a fost scris cu succes")
    else:
        print("Nu s-au gasit informatii despre produse")

url = "https://stirileprotv.ro/"

i_p = aip(url,limita=6)

for i in i_p:
    n_p = i["Title"]
    print("Title:",n_p)
se(i_p)