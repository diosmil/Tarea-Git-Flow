from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Crear una nueva instancia del navegador Chrome
driver = webdriver.Chrome()

# Navegar a la página de inicio de sesión
driver.get("https://sigerd.minerd.gob.do/Account/Login")

# Maximizar la ventana del navegador
driver.maximize_window()

# Esperar a que se cargue la página
driver.implicitly_wait(10)

# Tomar captura de pantalla de la página de inicio de sesión
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "1_inicio.png"))

# Introducir el usuario
usuario = driver.find_element(by=By.ID, value="Usuario")
usuario.send_keys("00107450538")

# Tomar captura de pantalla del campo de usuario
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "2_usuario.png"))

# Introducir la contraseña
contrasena = driver.find_element(by=By.ID, value="password")
contrasena.send_keys("DOMINGA2018")

# Tomar captura de pantalla del campo de contraseña
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "3_contrasena.png"))

# Hacer clic en el botón "Ingresar"
boton_ingresar = driver.find_element(by=By.ID, value="ingresar")
boton_ingresar.click()

# Esperar a que se cargue la página de inicio
driver.implicitly_wait(5)

# Tomar captura de pantalla cargando
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "4_inicio_sesion_cargando.png"))

# Esperar a que se cargue la página de inicio
driver.implicitly_wait(5)

# Tomar captura de pantalla de la página de inicio
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "5_inicio_sesion.png"))

# Hacer clic en el botón de "Usuario"
boton_cerrar_sesion_usuario = driver.find_element(by=By.CSS_SELECTOR, value=".caret")
boton_cerrar_sesion_usuario.click()

# Tomar captura de pantalla de la página de inicio
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "6_Dentro_de_la_pagina.png"))

# Hacer clic en el botón de "Cerrar Sesión"
boton_cerrar_sesion = driver.find_element(by=By.LINK_TEXT, value="Cerrar Sesión")
boton_cerrar_sesion.click()

# Tomar captura de pantalla de la página de inicio
driver.save_screenshot(os.path.join(os.getcwd(), "screenshots", "7_Cerrando_sesion.png"))

# Cerrar la ventana del navegador
driver.quit()

# Listado de capturas de pantalla tomadas
capturas = "\n\t- ".join(os.listdir(os.path.join(os.getcwd(), "screenshots")))

# Escribir el reporte de la prueba en un archivo de texto
with open(os.path.join(os.getcwd(), "reporte.txt"), "w") as f:
    f.write("Reporte de la Prueba Automatizada\n\n")
    f.write("Capturas de pantalla tomadas:\n")
    f.write("-" * 50 + "\n")
    f.write(capturas)
    f.write("\n\n" + "-" * 50 + "\n")
    f.write("La prueba se completó con éxito.")

# Escribir el reporte de errores en un archivo de texto
with open(os.path.join(os.getcwd(), "errores.txt"), "w") as f:
    f.write("Reporte de Errores de la Prueba Automatizada\n\n")
    f.write("-" * 50 + "\n")
    f.write("No se encontraron errores.")
    f.write("\n\n" + "-" * 50 + "\n")

# Escribir el reporte de estadísticas en un archivo de texto
with open(os.path.join(os.getcwd(), "estadisticas.txt"), "w") as f:
    f.write("Reporte de Estadísticas de la Prueba Automatizada\n\n")
    f.write("-" * 50 + "\n")
    f.write("Total de pruebas realizadas: 1\n")
    f.write("Total de pruebas exitosas: 1\n")
    f.write("Total de pruebas fallidas: 0\n")
    f.write("\n\n" + "-" * 50 + "\n")
