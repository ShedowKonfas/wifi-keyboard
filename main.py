from pywebio import start_server
from pywebio.output import put_button, put_row, put_text, put_markdown
from pywebio.session import run_js
import pyautogui

def refresh():
    put_button("↻", onclick=lambda: run_js('window.location.reload()'))


def on_up():
    pyautogui.press('up')
    put_text("Нажата стрелка вверх")  # визуальная обратная связь

def on_down():
    pyautogui.press('down')
    put_text("Нажата стрелка вниз")

def on_left():
    pyautogui.press('left')
    put_text("Нажата стрелка влево")

def on_right():
    pyautogui.press('right')
    put_text("Нажата стрелка вправо")

def on_pause():
    pyautogui.press('playpause')
    put_text("Нажата стрелка пауза")

def on_esc():
    pyautogui.press('escape')
    put_text("Нажата стрелка esc")

def on_enter():
    pyautogui.press('Enter')
    put_text("Нажата стрелка enter")

def on_space():
    pyautogui.press('space')
    put_text("Нажата стрелка enter")

def on_lkm():
    pyautogui.click(button="left")

def strelki():
    put_markdown("## Управление стрелками")
    # Размещаем кнопки в виде крестовины
    put_row([
        None,  # пустота в левом верхнем углу
        put_button("↑", onclick=on_up),
        None
    ], size="50px 50px 50px")  # размеры колонок

    put_row([
        put_button("←", onclick=on_left),
        put_button("⏯", onclick=on_pause),  # можно любую кнопку
        put_button("→", onclick=on_right)
    ], size="50px 50px 50px")

    put_row([
        None,
        put_button("↓", onclick=on_down),
        None
    ], size="50px 50px 50px")

    put_row([
        None,
        put_button("↻", onclick=lambda: run_js('window.location.reload()')),
        None
    ], size="50px 50px 50px")
    
    

def main():   
    put_row([
            put_button("strelki", onclick=strelki),
            put_button("esc", onclick=on_esc),
            put_button("space", onclick=on_space),
            put_button("LMOUSE", onclick=on_lkm),
            put_button("enter", onclick=on_enter)
        ], size="50px 69px 67px")
    put_text("Нажимайте кнопки – они эмулируют нажатие клавиш на вашем компьютере.")

if __name__ == '__main__':
    start_server(main, port=1337)  # передаём функцию, а не результат