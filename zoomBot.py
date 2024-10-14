import cv2
import numpy as np
import pyautogui
import pytesseract
import time

# Configura el número mínimo de participantes
MIN_PARTICIPANTS = 25

def check_participants():
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    reference_image = cv2.imread('participants.png', cv2.IMREAD_GRAYSCALE)
    result = cv2.matchTemplate(screenshot_gray, reference_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        participants_count = get_participant_count(screenshot_np)
        if participants_count < MIN_PARTICIPANTS:
            exit_zoom_meeting()

def exit_zoom_meeting():
    pyautogui.hotkey('alt', 'q')

def get_participant_count(screenshot):
    # Usa pytesseract para leer el número de participantes
    text = pytesseract.image_to_string(screenshot)
    # Procesa el texto para extraer el número de participantes
    # Asegúrate de implementar la lógica adecuada aquí
    return int(text) if text.isdigit() else 0

# Ciclo principal
while True:
    check_participants()
    time.sleep(5)
