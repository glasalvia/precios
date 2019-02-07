import config
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

#Selenium Chrome Driver
##############################################

driver = webdriver.Chrome(executable_path=config.chromedriver_path)
sin_valor = ['00,00']

##############################################

def scraper_coto():
	valores = []

	Datos_1 = driver.find_elements_by_xpath("//span[@class='atg_store_newPrice']")

	for Precio in Datos_1:
		Precio_Oferta = Precio.text
		Precio_Oferta = Precio_Oferta.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','').replace('.',',')

		if Precio_Oferta == '':
			'nada'
		else:
			valores.append(Precio_Oferta)


	Datos_2 = driver.find_elements_by_xpath("//span[@class='price_regular_precio']")

	for Precio in Datos_2:
		Precio_Regular = Precio.text
		Precio_Regular = Precio_Regular.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','').replace('.',',')

		if Precio_Regular == '':
			'nada'
		else:
			valores.append(Precio_Regular)

	sin_valor = ['00,00']

	if len(valores) == 1:
		valores = sin_valor+valores

	return valores
	
##############################################

def scraper_wallmart():

	valores = []
	Datos_1 = driver.find_elements_by_xpath("//strong[@class='skuBestPrice']")

	for Precio in Datos_1:
		Precio_Oferta = Precio.text
		Precio_Oferta = Precio_Oferta.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','')


		if Precio_Oferta == '':
			'nada'
		else:
			Precio_Oferta = Precio_Oferta[:2]+','+Precio_Oferta[2:]
			valores.append(Precio_Oferta)


	Datos_2 = driver.find_elements_by_xpath("//strong[@class='skuListPrice']")

	for Precio in Datos_2:
		Precio_Regular = Precio.text
		Precio_Regular = Precio_Regular.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','')

		if Precio_Regular == '':
			'nada'
		else:
			valores.append(Precio_Regular)

	sin_valor = ['00,00']

	if len(valores) == 1:
		valores = sin_valor+valores

	return valores

##############################################

def scraper_jumbo():
	valores = []

	Datos_1 = driver.find_elements_by_xpath("//strong[@class='skuBestPrice']")

	for Precio in Datos_1:
		Precio_Oferta = Precio.text
		Precio_Oferta = Precio_Oferta.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','').replace('.',',')

		if Precio_Oferta == '':
			'nada'
		else:
			valores.append(Precio_Oferta)

	if len(valores) == 1:
		valores = sin_valor+valores

	return valores
	
##############################################

def scraper_dia():
	valores = []

	Datos_1 = driver.find_elements_by_xpath("//strong[@class='skuBestPrice']")

	for Precio in Datos_1:
		Precio_Oferta = Precio.text
		Precio_Oferta = Precio_Oferta.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','').replace('.',',')

		if Precio_Oferta == '':
			'nada'
		else:
			valores.append(Precio_Oferta)


	Datos_2 = driver.find_elements_by_xpath("//strong[@class='skuListPrice']")

	for Precio in Datos_2:
		Precio_Regular = Precio.text
		Precio_Regular = Precio_Regular.replace('PRECIO CONTADO\n\n','').replace('\r','').replace('$','').replace('.',',')

		if Precio_Regular == '':
			'nada'
		else:
			valores.append(Precio_Regular)

	sin_valor = ['00,00']

	if len(valores) == 1:
		valores = sin_valor+valores

	return valores
	
##############################################