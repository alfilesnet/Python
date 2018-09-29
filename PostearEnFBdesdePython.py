import sys
import dryscrape
from time import sleep
import re

def postear_en_facebook(message):

	#===================================================
	# PARTE 1: PREPARATIVOS
	#===================================================

	#----------------------------------------------------
	# Si se ejecuta en linux, debemos ejecutar la 
	# función start_xvfb()
	#----------------------------------------------------
	if 'linux' in sys.platform:
		dryscrape.start_xvfb()

	#----------------------------------------------------
	# Le decimos a que página queremos entrar
	#----------------------------------------------------
	sess = dryscrape.Session(base_url = 'https://www.facebook.com')
	#----------------------------------------------------
	# Se añade la cabecera que estamos usando un  
	# navegador, sino entrarás en twitter como un bot y 
	# seguramente no puedas acceder a él
	#----------------------------------------------------
	sess.set_header("User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0")
	#----------------------------------------------------
	# Ajusta si quieres que extraiga las imágenes al 
	# scrappear el contenido o no.
	#
	# Para este bot no hace falta, porque lo que va a 
	# hacer es enviar un mensaje
	#----------------------------------------------------	
	# True = muestra imágenes
	# False = oculta las imágenes
	sess.set_attribute('auto_load_images', False)


	#----------------------------------------------------
	# Escribe las credenciales para entrar a tu cuenta
	# de Twitter
	#----------------------------------------------------
	email='Escribe tu correo de facebook'         # Debes dejar las comillas
	password='Escribe tu contraseña de facebook'  # Debes dejar las comillas

	try:
		#===================================================
		# PARTE 2: LOGUEO
		#===================================================	
		#----------------------------------------------------
		# Visito https://www.facebook.com
		#----------------------------------------------------
		sess.visit('/')	
		#----------------------------------------------------
		# Me voy a la caja de texto de usuario
		#----------------------------------------------------
		q = sess.at_xpath('//*[@id="email"]')
		#----------------------------------------------------
		# Le digo que escriba el email que le he dicho antes
		#----------------------------------------------------
		q.set(email)
		#----------------------------------------------------
		# Me voy a la caja de texto de contraseña
		#----------------------------------------------------
		q = sess.at_xpath('//*[@id="pass"]')
		#----------------------------------------------------
		# Le digo que escriba el pass que le he dicho antes
		#----------------------------------------------------
		q.set(password)
		#----------------------------------------------------
		# Me voy al botón de Entrar
		#----------------------------------------------------
		login_button = sess.at_xpath('//*[@id="loginbutton"]')
		#----------------------------------------------------
		# Clickeo sobre él
		#----------------------------------------------------
		login_button.click()


		#===================================================
		# PARTE 3: ESCRIBIR MENSAJE
		#===================================================
		#----------------------------------------------------
		# Saco mediante regex el id de la ruta de la caja de
		# texto para poder escribir
		#----------------------------------------------------
		regex = r"autocomplete=\"off\"><div id=\"(.+?)\"><div class=\"clearfix[\w\W]+?\">"
		html=sess.body()
		ruta=re.search(regex, html).group(1)
		#----------------------------------------------------
		# Escribo el mensaje que le he pasado a la función
		#----------------------------------------------------
		q=sess.at_xpath('//*[@id="'+str(ruta)+'"]/div/div[2]/textarea')
		q.set(message)

		#----------------------------------------------------
		# Saco mediante regex el id de la ruta de la caja de
		# texto para poder clickearle en Compartir
		#----------------------------------------------------
		regex = r"action=\"/ajax/updatestatus\.php\?[\w\W]+?onsubmit=\"\" id=\"(.+?)\""		
		html=sess.body()		
		ruta=re.search(regex, html).group(1)
		#----------------------------------------------------
		# Clickeo en compartir para enviar el mensaje
		#----------------------------------------------------		
		q=sess.at_xpath('//*[@id="'+str(ruta)+'"]/div[3]/div/div/div/button')
		q.click()
		#----------------------------------------------------
		# Hago una pausa de 1 segundo
		#----------------------------------------------------				
		sleep(1)
	except Exception as e:
		print (e)			


postear_en_facebook('Probando a postear desde Python')
