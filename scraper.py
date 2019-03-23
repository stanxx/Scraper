import requests 
from bs4 import BeautifulSoup
import random
import webbrowser

def Checkstock(variant):
	url = 'https://www.off---white.com/en/GB/men/products/' + str(variant)
	res = requests.get(url)
	page = BeautifulSoup(res.text, 'lxml')
	variants_all = page.findAll("input", {"class": "js-change-quantity"})
	for variant_single in variants_all:
		varid = variant_single["value"]
		stock = variant_single["data-count-on-hand"]
		varidforsize = variant_single["id"]
		varlabel = page.findAll("label", {"for":str(varidforsize)})
		size = varlabel[0].text
		print("varid :" + varid)
		print("stock :" + stock)
		print("size :" + size)
	print(variants_all)
	
#'omye026s19c300018500'
variant = Input()
Checkstock(variant)