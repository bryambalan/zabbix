#!/usr/bin/env python

from lxml import html
import requests
import re
import sys

def convertTuple(tup):
    str =  ''.join(tup)
    return str

if len(sys.argv) < 2:
    print("erro, informe o site a ser testado\n")
    sys.exit(1)
site = sys.argv[1]

url = 'https://downdetector.com.br/fora-do-ar/' + site + '/'

page = requests.get(url)
if page.status_code != 200:
    #print("ERROR-404")
    print("0")
    sys.exit(1)

tree = html.fromstring(page.content)
status = tree.xpath('//*[@id="chart-row"]/div/div/script[1]/text()')
#print(status)

for x in range(len(status)):
    data = status[x]
    #print(data)
    teste = re.compile(".*status: '(.*)',.*", re.MULTILINE)
    for match in teste.finditer(data):
        status = match.groups()
        status = convertTuple(status)
	      #print(status)
  	    #Conventendo String para Valor numerico
        if(status == 'success'):
            status = 10
        if(status == 'warning'):
            status = 20
        if(status == 'danger'):
            status = 30
        print(status)
