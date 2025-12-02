import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# --- CONFIGURACIÓN ---
URL_APP = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
SCREENSHOT_DIR = "reportes/capturas"

if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

@pytest.fixture(scope="module")
def driver():
    # CAMBIO: Usamos Selenium directo, sin gestores de descarga
    # Esto busca tu Edge instalado automáticamente
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Edge(options=options)
    except:
        # Si falla, intentamos sin opciones
        driver = webdriver.Edge()
        
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    try:
        timestamp = datetime.now().strftime("%H%M%S")
        safe_name = "".join([c for c in name if c.isalnum() or c in (' ', '_')]).strip()
        path = f"{SCREENSHOT_DIR}/{safe_name}_{timestamp}.png"
        driver.save_screenshot(path)
    except:
        pass

# --- PRUEBAS ---

def test_login_ok(driver):
    driver.get(URL_APP)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name")))
    take_screenshot(driver, "1_Login_Exitoso")
    assert "OrangeHRM" in driver.title

def test_crear_empleado(driver):
    driver.find_element(By.LINK_TEXT, "PIM").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add')]")))
    driver.find_element(By.XPATH, "//button[contains(., 'Add')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstName")))
    driver.find_element(By.NAME, "firstName").send_keys("Usuario")
    driver.find_element(By.NAME, "lastName").send_keys("Prueba")
    take_screenshot(driver, "2_Crear_Empleado_Lleno")
    assert driver.find_element(By.CSS_SELECTOR, "button[type='submit']").is_displayed()

def test_buscar_empleado(driver):
    driver.find_element(By.LINK_TEXT, "PIM").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")))
    caja_texto = driver.find_element(By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
    caja_texto.send_keys("Amelia")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    take_screenshot(driver, "3_Busqueda_Resultados")
    assert len(driver.find_elements(By.CLASS_NAME, "oxd-table-card")) > 0

def test_login_error(driver):
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("CLAVE_MALA")
    driver.find_element(By.TAG_NAME, "button").click()
    take_screenshot(driver, "4_Login_Error_Esperado")
    assert driver.find_element(By.CLASS_NAME, "oxd-alert-content").is_displayed()

def test_limites_vacios(driver):
    driver.get(URL_APP)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.TAG_NAME, "button").click()
    take_screenshot(driver, "5_Error_Campos_Vacios")
    assert len(driver.find_elements(By.CLASS_NAME, "oxd-input-field-error-message")) > 0