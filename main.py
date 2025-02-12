from selenium import webdriver  # Importa el controlador de Selenium
from selenium.webdriver.common.keys import Keys  # Permite simular teclas del teclado
from selenium.webdriver.common.by import By  # Usado para localizar elementos en la página
import time  # Importa time para manejar pausas
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options  # Importa opciones para modificar Chrome

def initialize_driver():
    
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1280,720")
    return webdriver.Chrome(options=chrome_options)

def main():  # sourcery skip: do-not-use-bare-except
    driver = initialize_driver()
    driver.get('https://forms.office.com/pages/responsepage.aspx?id=XcQUdIprU0yztAacSsuwyIPWwjG6cDtGpcYYxnbIIHpUMlBXNllURFhFVlNIRFA0M0tRVkhYN1M5US4u&route=shorturl')
    
    # Esperar unos segundos para que la página cargue completamente
    time.sleep(3)

    # firts element get element and write
    fullName = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/span/input")
    fullName.send_keys("Emanuel Restrepo")
    
    # Seleccionar los botones de opción (radio buttons)
    button1 = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/label/span[1]/input") # Suposición: Segundo botón del array
    button1.click() # type: ignore
    numberPhone = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/input")
    numberPhone.send_keys("1124048846")
    mail = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/span/input")
    mail.send_keys("emadavresgar@gmail.com")
    button2 = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[1]/div/label/span[1]/input") # Suposición: Segundo botón del array
    button2.click()
    
    submit = driver.find_element(By.CLASS_NAME, "css-198") # Suposición: Segundo botón del array
    submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "css-198"))
    )
    submit.click() # type: ignore
    time.sleep(3)
    driver.quit()
    
if __name__ == "__main__":
    #for i in range(100):
        main()
