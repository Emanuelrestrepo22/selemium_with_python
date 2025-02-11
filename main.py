from selenium import webdriver  # Importa el controlador de Selenium
from selenium.webdriver.common.keys import Keys  # Permite simular teclas del teclado
from selenium.webdriver.common.by import By  # Usado para localizar elementos en la página
import time  # Importa time para manejar pausas

def initialize_driver():
    """
    Inicializa el navegador Chrome y devuelve el objeto del controlador.
    """
    driver = webdriver.Chrome()
    return driver

def main():
    """
    Función principal que realiza la automatización.
    """
    driver = initialize_driver()
    driver.get('https://forms.office.com/pages/responsepage.aspx?id=XcQUdIprU0yztAacSsuwyIPWwjG6cDtGpcYYxnbIIHpUMlBXNllURFhFVlNIRFA0M0tRVkhYN1M5US4u&route=shorturl')
    
    # Esperar unos segundos para que la página cargue completamente
    time.sleep(3)



if __name__ == "__main__":
    main()