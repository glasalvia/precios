import config
import scrapers
import time
import notificaciones
from scrapers import scraper_coto, scraper_wallmart, scraper_jumbo, scraper_dia
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

#Variables
##############################################

Enlaces_Coto = config.Enlaces_Coto
Enlaces_Wallmart = config.Enlaces_Wallmart
Enlaces_Jumbo = config.Enlaces_Jumbo
Enlaces_Dia = config.Enlaces_Dia

driver = scrapers.driver

Precios_Coto = []
Precios_Wallmart = []
Precios_Jumbo = []
Precios_Dia = []

##############################################
#Recorrida COTO

for Enlace in Enlaces_Coto:

	driver.get(Enlace)
	print(Enlace)

	resultado = scraper_coto()
	Precios_Coto.append(resultado)
	driver.delete_all_cookies()


print(Precios_Coto)

##############################################
#Recorrida WALLMART

for Enlace in Enlaces_Wallmart:

	try:
		driver.get(Enlace)
		print(Enlace)

		resultado = scraper_wallmart()
		Precios_Wallmart.append(resultado)
		driver.delete_all_cookies()

	except UnexpectedAlertPresentException:
		alerta = driver.switch_to_alert()
		alerta.accept()

		resultado = scraper_wallmart()
		Precios_Wallmart.append(resultado)
		driver.delete_all_cookies()

print(Precios_Wallmart)
##############################################
#Recorrida JUMBO

for Enlace in Enlaces_Jumbo:

	driver.get(Enlace)
	print(Enlace)

	resultado = scraper_jumbo()
	Precios_Jumbo.append(resultado)
	driver.delete_all_cookies()


print(Precios_Jumbo)

##############################################
#Recorrida DIA

for Enlace in Enlaces_Dia:

	driver.get(Enlace)
	print(Enlace)

	resultado = scraper_dia()
	Precios_Dia.append(resultado)
	driver.delete_all_cookies()


print(Precios_Dia)




driver.quit()