import time

import mss.tools
import pyautogui

# 准备工作时间
time.sleep(10)

flag = False

for i in range(50):
    if flag:
        # 按键翻页
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')

    i = "%02d" % i

    with mss.mss() as sct:
        # 截取屏幕部分（分辨率：1920 x 1080）
        monitor = {"top": 70, "left": 620, "width": 680, "height": 1000}
        output = "./images/{0}page.png".format(i, **monitor)

        # 抓取数据
        sct_img = sct.grab(monitor)

        # 保存图像
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    flag = True
    time.sleep(0.05)


# for i in range(1, 10):
#     # Turn page
#     pyautogui.keyDown('right')
#     pyautogui.keyUp('right')
#     # Take and save a screenshot
#     pyautogui.screenshot('images/page_%d.png' % i, region=(500, 200, 500, 800))
#     time.sleep(0.05)
