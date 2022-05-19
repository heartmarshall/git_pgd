import pyautogui
import time
import os


PICS_DIR = os.path.join(os.getcwd(), "pics")
SEND_TO_GIT_SCRIPT = os.path.join(os.getcwd(), "send.sh")
os.makedirs(PICS_DIR, exist_ok=True)

DELAY = 0  # Задержка перед тем, как программа начёнет делать скриншоты
LOOPS_NUM = 4  # Сколько раз будет сделан скриншот
SLEEP_TIME = 1  # Промежуток в секундах между скриншотами

time.sleep(DELAY)

for screenshot_num in range(LOOPS_NUM):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(os.path.join(PICS_DIR, str(screenshot_num) + '.png'))
    time.sleep(SLEEP_TIME)

os.system(SEND_TO_GIT_SCRIPT)
