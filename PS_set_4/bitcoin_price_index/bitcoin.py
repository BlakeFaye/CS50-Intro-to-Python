import requests
import sys


try:
    user_btc = float(input("How much of BTC? "))

    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    resp = requests.get(url=url)
    data = resp.json()
    btc_total = round(float((str(data["bpi"]["USD"]["rate"])).replace(",", "")),4) * user_btc
    print (f"Ceci équivaut à : {btc_total:,}")


except requests.RequestException: 
    #print("Erreur de requête")
    pass
'''
except ValueError:
    print("La valeur entrée n'est pas un float")
    sys.exit(0)
'''