import dryscrape
import sys

if 'linux' in sys.platform:
    # start xvfb in case no X is running. Make sure xvfb 
    # is installed, otherwise this won't work!
    dryscrape.start_xvfb()
    
sess = dryscrape.Session(base_url = 'https://www.facebook.com')
sess.set_header("User-Agent", "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0")
# True = muestra imágenes
# False = oculta las imágenes
sess.set_attribute('auto_load_images', True)

email='Escribe tu correo de FB'
password='Escribe tu contraseña de FB'

sess.visit('/')
q = sess.at_xpath('//*[@id="email"]')
q.set(email)
q = sess.at_xpath('//*[@id="pass"]')
q.set(password)
login_button = sess.at_xpath('//*[@id="loginbutton"]')
login_button.click()

sess.render('facebook.png')
print("Captura de pantalla guardada en 'facebook.png'")
