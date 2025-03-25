from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#screenshot
from PIL import ImageGrab
#imagem para texto
import pytesseract
import cv2
#abrir navegador
browser = webdriver.Chrome()
#selecionar url com a minutagem do video
browser.get("https://youtu.be/Uo_1cK8X_wM?si=U9ECGZGGOUAFyhva&t=520")
#espera do navegador e botão
WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@aria-label='Play']"))).click()
#printscreen
image = ImageGrab.grab()
#image.save("tp.jpg")

imagem = cv2.imread("tp.jpg")
caminho = "C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + "\tesseract.exe"
text = pytesseract.image_to_string(imagem)

print(text)