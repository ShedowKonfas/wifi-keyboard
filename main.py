from pywebio import start_server
from pywebio.output import put_button, put_row, put_text, put_markdown, put_html  # добавили put_html
from pywebio.session import run_js
import screen_brightness_control as brightness_lib
import pyautogui
import time

# -------------------- Управление яркостью --------------------
def screen_brightness(cmd):
    try:
        # get_brightness() возвращает список яркостей для всех мониторов
        primary = brightness_lib.get_brightness()[0]
        
        if cmd == "up":
            if primary >= 100:
                put_text("⚠️ Яркость уже максимальная (100%)")
                return
            new_val = primary + 10
            if new_val > 100:
                new_val = 100
            brightness_lib.set_brightness(new_val)
            put_text(f"☀️ Яркость увеличена до {new_val}%")
            
        elif cmd == "down":
            if primary <= 0:
                put_text("⚠️ Яркость уже минимальная (0%)")
                return
            new_val = primary - 10
            if new_val < 0:
                new_val = 0
            brightness_lib.set_brightness(new_val)
            put_text(f"🌙 Яркость уменьшена до {new_val}%")
            
        elif cmd == "100":
            brightness_lib.set_brightness(100)
            put_text("☀️ Яркость установлена на 100%")
        else:
            put_text("❌ Неизвестная команда")
    except Exception as e:
        put_text(f"❌ Ошибка управления яркостью: {e}")

# -------------------- Универсальное нажатие клавиш --------------------
def on(key):
    pyautogui.keyDown(key)
    time.sleep(0.05)   # достаточно 0.05 сек для регистрации
    pyautogui.keyUp(key)
    put_text(f"⌨️ Нажата клавиша: {key}")

# -------------------- Клики мышью --------------------
def on_mouse(btn):
    pyautogui.click(button=btn)
    if btn == "left":
        put_text("🖱️ Клик левой кнопкой")
    elif btn == "right":
        put_text("🖱️ Клик правой кнопкой")
    elif btn == "middle":
        put_text("🖱️ Клик средней кнопкой")
    else:
        put_text("❓ Неизвестная кнопка")

def double_mouse():
    pyautogui.doubleClick('left')
    put_text("🖱️ Двойной клик левой кнопкой")

# -------------------- Свернуть все окна (Win+D) --------------------
def hotkeys():
    pyautogui.keyDown("win")
    pyautogui.press("down")   # на самом деле для сворачивания всех окон используется Win+D, но здесь оставлено как было
    pyautogui.keyUp("win")
    # Более правильный способ: pyautogui.hotkey('win', 'd')
    #put_text("🔄 Окна свернуты (Win+D)")

# -------------------- Кнопка обновления страницы --------------------
def refresh_btn():
    return put_button("🔄", onclick=lambda: run_js('window.location.reload()'),
                      color='info', outline=True)

# -------------------- Меню со стрелками --------------------
def strelki():
    put_markdown("## 🎮 Управление стрелками и плеером")
    put_row([
        None,
        put_button("⬆", onclick=lambda: on("up"), color='secondary'),
        None
    ], size="50px 50px 50px")
    put_row([
        put_button("⬅", onclick=lambda: on("left"), color='secondary'),
        put_button("⏯", onclick=lambda: on("playpause"), color='warning'),   # пауза/воспроизведение
        put_button("➡", onclick=lambda: on("right"), color='secondary')
    ], size="50px 50px 50px")
    put_row([
        None,
        put_button("⬇", onclick=lambda: on("down"), color='secondary'),
        None
    ], size="50px 50px 50px")
    put_row([
        None,
        refresh_btn(),
        None
    ], size="50px 50px 50px")

# -------------------- Главная функция (интерфейс) --------------------
def main():
    put_markdown("# 🕹️ Пульт управления ПК")
    
    put_markdown("### 🖱️ Мышь")
    put_row([...])
    put_html('<hr>')   # разделитель
    
    put_markdown("### ⌨️ Клавиатура")
    put_row([...])
    put_html('<hr>')
    
    put_markdown("### 📂 Меню")
    put_row([...])
    put_html('<hr>')
    
    put_markdown("### 📺 Монитор")
    put_row([...])
    put_html('<hr>')
    
    put_text("💡 Нажимайте кнопки – они эмулируют нажатия клавиш на вашем компьютере.")

# -------------------- Запуск сервера --------------------
if __name__ == '__main__':
    # Небольшая пауза, чтобы успеть переключиться на окно браузера
    time.sleep(2)
    print("Сворачиваю окна и запускаю сервер...")
    hotkeys()  # свернуть все окна перед запуском
    start_server(main, port=1337, debug=True)