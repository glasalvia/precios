#Variables del proyecto

chromedriver_path = 'D:\\Python27\\Proyectos\\scraper\\chromedriver.exe'


Enlaces_Coto = ['https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-entera-la-serenisima-e-calcio-vit-a-c-d-b9-sch-1-lt/_/A-00251050-00251050-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-espagueti-matarazzo----paquete-500-gr/_/A-00263801-00263801-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-largo-fino-dos-hermanos----paquete-1-kg/_/A-00053908-00053908-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-manteca-calext-la-serenisi-paq-100-grm/_/A-00003817-00003817-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-azucar-ledesma----comun-tipo-a-paquete-1-kg/_/A-00053132-00053132-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-yerba-mate-amanda----paquete-500-gr/_/A-00251288-00251288-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-girasol--natura---botella-15-l/_/A-00014076-00014076-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-dulce-de-leche-la-serenisima-fuente-de-calcio-pot-400-grm/_/A-00251874-00251874-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-caldo-en-cubos--knorr-verduras-----caja-x-12-cubos/_/A-00258798-00258798-200',
			 	'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-agua-mineral--villa-del-sur----botella-225-l/_/A-00101784-00101784-200']


Enlaces_Wallmart = ['https://www.walmart.com.ar/leche-ent-ultr-sachet-la-serenisima-1-lt/p',
	 			    'https://www.walmart.com.ar/fideos-spagheti-matarazzo-500gr/p',
	 			    'https://www.walmart.com.ar/arroz-largo-fino-dos-hermanos-1-kg/p',
	 			    'https://www.walmart.com.ar/manteca-la-serenisima-100-gr/p',
	 			    'https://www.walmart.com.ar/azucar-clasica-ledesma-1-kg/p',
	 			    'https://www.walmart.com.ar/yerba-tradicional-amanda-500gr/p',
	 			    'https://www.walmart.com.ar/aceite-de-girasol-natura-1-5-lt/p',
	 			    'https://www.walmart.com.ar/dulce-de-leche-clasico-la-serenisima-400gr/p',
	 			    'https://www.walmart.com.ar/caldo-verdura-knorr-12u/p',
	 			    'https://www.walmart.com.ar/agua-mineral-sin-gas-villa-del-sur-2-25-lt/p']


Enlaces_Jumbo = ['https://www.jumbo.com.ar/leche-entera-la-serenisima-x-1-lt/p',
				 'https://www.jumbo.com.ar/fideos-matarazzo-7/p',
				 'https://www.jumbo.com.ar/arroz-dos-hermanos-largo-fino-1kg/p',
				 'https://www.jumbo.com.ar/manteca-la-serenisima/p',
				 'https://www.jumbo.com.ar/azucar-ledesma-molida-clasica/p',
				 'https://www.jumbo.com.ar/yerba-amanda-con-palo-2/p',
				 'https://www.jumbo.com.ar/aceite-natura-de-girasol/p',
				 'https://www.jumbo.com.ar/dulce-de-leche-la-serenisima-fuente-de-calcio/p',
				 'https://www.jumbo.com.ar/caldo-knorr-verdura/p',
				 'https://www.jumbo.com.ar/agua-mineral-sin-gas-villa-del-sur-2-25-l/p']



Enlaces_Dia = ['https://diaonline.supermercadosdia.com.ar/leche-ent-sachet-la-serenisima-1-l-20498/p',
			   'https://diaonline.supermercadosdia.com.ar/fideo-spaghetti-matarazzo-500gr-38834/p',
			   'https://diaonline.supermercadosdia.com.ar/arroz-largo-fino-00000-dos-hermanos-1kg-179860/p',
			   'https://diaonline.supermercadosdia.com.ar/manteca-cal-extra-la-serenisima-100-gr-60589/p',
			   'https://diaonline.supermercadosdia.com.ar/azucar-ledesma-clasica-1kg-107879/p',
			   'https://diaonline.supermercadosdia.com.ar/yerba-tradicional-amanda-500gr-164681/p',
			   'https://diaonline.supermercadosdia.com.ar/aceite-girasol-natura-15l-78856/p',
			   'https://diaonline.supermercadosdia.com.ar/dulce-de-leche-la-serenisima-400-gr-165752/p',
			   'https://diaonline.supermercadosdia.com.ar/caldo-verdura-knorr-12-ud-15000/p',
			   'https://diaonline.supermercadosdia.com.ar/agua-mineral-sin-gas-villa-del-sur-250-l-54155/p']



Productos = [{'Producto':'Leche Entera','Marca':'La Serenisima','Unidad':'LT','Cantidad':'1','Imagen_URL':''},
			 {'Producto':'Fideos Spagethi','Marca':'Matarazzo','Unidad':'GR','Cantidad':'500','Imagen_URL':''},
			 {'Producto':'Arroz Largo Fino','Marca':'Dos Hermanos','Unidad':'KL','Cantidad':'1','Imagen_URL':''},
			 {'Producto':'Manteca','Marca':'La Serenisima','Unidad':'GR','Cantidad':'100','Imagen_URL':'',},
			 {'Producto':'Azucar','Marca':'Ledesna','Unidad':'KL','Cantidad':'1','Imagen_URL':'',},
			 {'Producto':'yerba','Marca':'Amanda','Unidad':'GR','Cantidad':'500','Imagen_URL':'',},
			 {'Producto':'Aceite','Marca':'Natura','Unidad':'LT','Cantidad':'1,5','Imagen_URL':'',},
			 {'Producto':'Dulce de Leche','Marca':'La Serenisima','Unidad':'GR','Cantidad':'400','Imagen_URL':'',},
			 {'Producto':'Caldo','Marca':'Knorr','Unidad':'GR','Cantidad':'114','Imagen_URL':'',},
			 {'Producto':'Agua Mineral','Marca':'Villa del sur','Unidad':'LT','Cantidad':'2,25','Imagen_URL':'',}
			]