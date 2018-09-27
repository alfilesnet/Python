import dryscrape
from time import sleep
import sys

def postear_en_twitter(mensaje):

	if 'linux' in sys.platform:
		dryscrape.start_xvfb()
    
	sess = dryscrape.Session(base_url = 'https://www.twitter.com')
	sess.set_header("User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0")
	# True = muestra imágenes
	# False = oculta las imágenes
	sess.set_attribute('auto_load_images', False)

	email='Escribe tu correo de twitter'         # Debe de ir entrecomillado
	password='Escribe tu contraseña de twitter'  # Debe de ir entrecomillado

	try:		
		sess.visit('/')
		q = sess.at_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[1]/form/div[1]/input')
		q.set(email)
		q = sess.at_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[1]/form/div[2]/input')
		q.set(password)
		q.form().submit()	

		q=sess.at_xpath('//*[@id="tweet-box-home-timeline"]')
		q.click()
		q=sess.at_xpath('/html/body/div[2]/div[3]/div/div[2]/div[2]/div/form/div[2]/textarea')
		q.set(mensaje)		
		q = sess.at_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button')		
		q.click()
		sleep(1)
		# sess.render('twitter.png')
	except Exception as e:
		print (e)			


postear_en_twitter('Probando a postear desde Python')

#Twitter no admite que se escriban dos frases iguales seguidas, así que para probarlo más de una vez, deberás cambiar el mensaje
