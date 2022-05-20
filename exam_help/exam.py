import pyautogui
import time
import os
import subprocess

PICS_DIR = os.path.join(os.getcwd(), "pics")
SEND_TO_GIT_SCRIPT = os.path.join(os.getcwd(), "send.sh")
os.makedirs(PICS_DIR, exist_ok=True)

DELAY = 0  # Задержка перед тем, как программа начёнет делать скриншоты
LOOPS_NUM = 20  # Сколько раз будет сделан скриншот
SLEEP_TIME = 1  # Промежуток в секундах между скриншотами

time.sleep(DELAY)

dir_num = 0

for screenshot_num in range(1, LOOPS_NUM+1):
    cur_dir = os.path.join(PICS_DIR, str(dir_num))
    os.makedirs(cur_dir, exist_ok=True)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(os.path.join(cur_dir, str(screenshot_num) + '.png'))
    time.sleep(SLEEP_TIME)
    if screenshot_num % 5 == 0:
        dir_num += 1
        # subprocess.run(args=[SEND_TO_GIT_SCRIPT, str(dir_num)], shell=True)
        os.system(SEND_TO_GIT_SCRIPT + ' ' + str(dir_num))

os.system(SEND_TO_GIT_SCRIPT)
