import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "pIE93ut7872nrDatDk7ThQ", "isbns": "9781632168146"})
print(res.json())
