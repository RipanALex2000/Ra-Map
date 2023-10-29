import requests
from bs4 import BeautifulSoup
import openpyxl

def aip(url,limita=5):
    raspuns = requests.get(url)
    if raspuns.status_code == 200:
        soup = BeautifulSoup(raspuns.text,"html.parser")
        en = soup.find_all("a",class_="font-bold d-block mt-md-2 mb-1")
        ep = soup.find_all("div",class_="real-price font-bold")

        i_p=[]
        index = 0

        for ne,pe in zip(en,ep):
            nume = ne.get_text(strip=True)
            pret = pe.find("span").get_text(strip=True)
            i_p.append({"nume": nume,"pret": pret})

            index += 1

            if index >= limita:
                return i_p
            
        return i_p
    else:
        print("Cererea HTTP a esuat.Cod de stare",raspuns.status_code)
        return None

url = "https://flip.ro/magazin/apple/iphone-14/"

i_p = aip(url,limita=5)

for i in i_p:
    n_p = i["nume"]
    pret=format(round(float(i["pret"])*1000))
    print("Nume produs:",n_p)
    print("Pret",pret)
    print()
