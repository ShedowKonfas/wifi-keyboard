from pywebio import start_server
from pywebio.output import put_button, put_row, put_text, put_markdown
from pywebio.session import run_js
import pyautogui
import time

# Универсальная функция для нажатия клавиш
def on(key):
    pyautogui.keyDown(key)
    time.sleep(0.5)
    pyautogui.keyUp(key)
    put_text(f"Нажата клавиша: {key}")

# Отдельно для клика мышью (т.к. это не press)
def on_mouse(btn):
    pyautogui.click(button=btn)
    if btn == "left":
        put_text("Клик левой кнопкой мыши")
    elif btn == "right":
        put_text("Клик правой кнопкой мыши")
    elif btn == "middle":
        put_text("Клик средней кнопкой мыши")
    else :
        put_text("Ты че вообще жмешь?")
   

# Кнопка обновления страницы (вынесена для повторного использования)
def refresh_btn():
    return put_button("↻", onclick=lambda: run_js('window.location.reload()'))

def strelki():
    put_markdown("## Управление стрелками")
    # Крестовина стрелок + кнопка паузы и обновления
    put_row([
        None,
        put_button("↑", onclick=lambda: on("up")),
        None
    ], size="50px 50px 50px")

    put_row([
        put_button("←", onclick=lambda: on("left")),
        put_button("⏯", onclick=lambda: on("playpause")),   # пауза/воспроизведение
        put_button("→", onclick=lambda: on("right"))
    ], size="50px 50px 50px")

    put_row([
        None,
        put_button("↓", onclick=lambda: on("down")),
        None
    ], size="50px 50px 50px")

    put_row([
        None,
        refresh_btn(),   # кнопка обновления
        None
    ], size="50px 50px 50px")

#def player():


def main():
    # Главная панель с кнопками
    put_row([
         ### MOUSE ###
        put_text("MOUSE"),
        put_button("ЛКМ", onclick=lambda: on_mouse("left")),
        put_button("ПКМ", onclick=lambda: on_mouse("right")),
        put_button("СКМ", onclick=lambda: on_mouse("middle"))
    ], size="auto")
    put_row([
        ### KEYBOARD ###
        put_text("KEYBOARD"),
        put_button("Esc", onclick=lambda: on("esc")),
        put_button("Space", onclick=lambda: on("space")),
        put_button("Enter", onclick=lambda: on("enter"))
    ], size="auto")
    put_row([
        ### MENU ###
        put_text("MENU"),
        put_button("Стрелки", onclick=strelki),
        #put_button("Управление плеером", onclick=player),
        put_button("Refresh", onclick=refresh_btn)   # можно и сюда добавить обновление
    ], size="auto")

    put_text("Нажимайте кнопки – они эмулируют нажатие клавиш на вашем компьютере.")

if __name__ == '__main__':
    start_server(main, port=1337)