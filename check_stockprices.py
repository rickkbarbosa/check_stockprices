#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import requests
import urllib3
import json
from bs4 import BeautifulSoup

def getValor(acao):

    acao = acao.upper()
    url = "http://br.advfn.com/p.php?pid=qkquote&symbol=" + acao
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')
    span = soup.find("span", id="quoteElementPiece3")

    try:
        price = span.text.replace(",", ".")       
    except:
        prince = "N/A"

    return price


acoes = str(sys.argv[1])
acoes = acoes.split(',')
prices = list()

for i in range(len(acoes)):
    ac = acoes[i]
    ret = getValor(acao=ac)
    
    if ret is not None:     
        result = {'{#STOCK_BVMF}': ac,
             'STOCK_PRICE': ret
             }
        prices.append(result)

print(json.dumps(prices, indent=4))
