import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

htmlicerigi = response.content

soup = BeautifulSoup(htmlicerigi, "html.parser")

basliklar = soup.findAll("td", {"class": "titleColumn"})
ratingler = soup.findAll("td", {"class": "ratingColumn imdbRating"})

while True:
    altdeger = float(input("Alt rating girin (0-10): "))
    ustdeger = float(input("Alt degerin üzerinde deger girininz ust rating girin (0-10): "))

    if altdeger < ustdeger:
        for baslik, rating in zip(basliklar, ratingler):
            baslik = baslik.text.strip().replace("\n", "")
            rating = rating.text.strip().replace("\n", "")

            if float(rating) > altdeger and float(rating) < ustdeger:
                print("Film ismi: {} | Film rating: {}".format(baslik, rating))
        print("\n")
    else:
        print("Tekrar deneyin")
