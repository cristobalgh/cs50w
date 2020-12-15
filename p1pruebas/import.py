import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE books (id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year VARCHAR NOT NULL)")

    f = open("books.csv")
    reader = csv.reader(f)
    i=0
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        i+=1
        if i % 200 == 0:
            print(f"Libro {title} agregado, con isbn {isbn}, autor {author} y del año {year}.")
            print(f"{i} entradas ya en la bd.")
    db.commit()
    print("Termine, todo agregado.")

if __name__ == "__main__":
    main()