from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Driver del navegador
service = Service("driver/chromedriver.exe")
clave = "José María Cordova (MDE"

# mazimiza la ventana
driver = webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(1)

#Ingresa a la página de viajes del exito
driver.get("https://www.viajesexito.com")
time.sleep(1)


#selecciona la opción de paquetes
paquetes = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a')
time.sleep(1)
paquetes.click()
time.sleep(5)

#Cierra la el que no quiero mas elementos
origen = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/div/div[2]/a[2]')
time.sleep(1)
origen.click()
time.sleep(1)

#Selecciona la opción del aeropuerto
aeropuerto = driver.find_element(By.NAME, "CityPredictiveFrom_netactica_airhotel")
time.sleep(1)
aeropuerto.click()
time.sleep(1)

#EN el campo aeropuerto seleciona escribe Jose Maria Cordoba
aa = driver.find_element(By.NAME, "popUpCityPredictiveFrom_netactica_airhotel")
time.sleep(1)
aa.click()
time.sleep(1)
aa.send_keys(clave)
aa.click()
time.sleep(1)


# Hace clic en el campo de origen
buscar = driver.find_element(By.XPATH,'/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div/div[2]')
buscar.click()
time.sleep(10)

# Finalizar la ejecución del WebDriver
driver.quit()




