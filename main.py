from selenium import webdriver  # Importa el controlador de Selenium
from selenium.webdriver.common.keys import Keys  # Permite simular teclas del teclado
from selenium.webdriver.common.by import By  # Usado para localizar elementos en la página
import time  # Importa time para manejar pausas
from concurrent.futures import ThreadPoolExecutor

def initialize_driver():
    return webdriver.Chrome()

def main():
    driver = initialize_driver()
    driver.get('https://forms.office.com/pages/responsepage.aspx?id=XcQUdIprU0yztAacSsuwyIPWwjG6cDtGpcYYxnbIIHpUMlBXNllURFhFVlNIRFA0M0tRVkhYN1M5US4u&route=shorturl')
    
    # Esperar unos segundos para que la página cargue completamente
    time.sleep(5)

    # firts element get element and write
    fullName = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/span/input")
    fullName.send_keys("Emanuel Restrepo")
    
    # Seleccionar los botones de opción (radio buttons)
    button1 = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/label/span[1]/input") # Suposición: Segundo botón del array
    button1.click() # type: ignore
    numberPhone = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/input")
    numberPhone.send_keys("1124048846")
    mail = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/span/input")
    mail.send_keys("emadavresgar@gmail.com")
    button2 = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[1]/div/label/span[1]/input") # Suposición: Segundo botón del array
    button2.click()
    
    submit = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[1]/div/label/span[1]/input") # Suposición: Segundo botón del array
    submit.click() # type: ignore
    driver.quit()
    
if __name__ == "__main__":
    for i in range(2000):
        main()
