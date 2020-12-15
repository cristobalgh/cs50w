import requests

def main():
    kei = "69ab08da369ee3ee081960f4cb34e2c5"
    res = requests.get("http://data.fixer.io/api/latest?access_key=69ab08da369ee3ee081960f4cb34e2c5&base=EUR&symbols=CLP")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["CLP"]
    print(f"1 EUR is equal to {round(rate)} CLP")

if __name__ == "__main__":
    main()
