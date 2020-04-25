#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import urllib3
import json
from bs4 import BeautifulSoup

def getValor(acao):

    acao = acao.upper()
    url = "http://br.advfn.com/p.php?pid=qkquote&symbol=" + acao
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    span = soup.find("span", id="quoteElementPiece1")

    if (span > -1):
        price = span.text.replace(",", ".")
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