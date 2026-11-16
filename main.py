from pywebio import *
from pywebio.output import *
from pywebio.session import *
import screen_brightness_control as brightness_lib
import pyautogui
import time

# -------------------- Управление яркостью --------------------
def screen_brightness(cmd):
    try:
        primary = brightness_lib.get_brightness()[0]
        
        if cmd == "up":
            if primary >= 100:
                put_text("⚠️ Яркость уже максимальная (100%)")
                return
            new_val = min(primary + 10, 100)
            brightness_lib.set_brightness(new_val)
            put_text(f"☀️ Яркость увеличена до {new_val}%")
            
        elif cmd == "down":
            if primary <= 0:
                put_text("⚠️ Яркость уже минимальная (0%)")
                return
            new_val = max(primary - 10, 0)
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
    time.sleep(0.05)
    pyautogui.keyUp(key)
    put_text(f"⌨️ Нажата клавиша: {key}")

# -------------------- Клики мышью --------------------
def on_mouse(btn):
    pyautogui.click(button=btn)
    names = {"left": "левой", "right": "правой", "middle": "средней"}
    put_text(f"🖱️ Клик {names.get(btn, btn)} кнопкой")

def double_mouse():
    pyautogui.doubleClick('left')
    put_text("🖱️ Двойной клик левой кнопкой")

# -------------------- Свернуть все окна (Win+D) --------------------
def hotkeys():
    pyautogui.hotkey('win', 'd')
    put_text("🔄 Все окна свернуты (Win+D)")

# -------------------- Кнопка обновления страницы --------------------
def refresh_btn():
    return put_button("🔄", onclick=lambda: run_js('window.location.reload()'),
                      color='info', outline=True)

# -------------------- Меню со стрелками (для плеера) --------------------
def strelki():
    return put_column([
        put_row([put_button("↑", onclick=lambda: on("up"))], size="50px"),
        put_row([put_button("↓", onclick=lambda: on("down"))], size="50px"),
        put_row([put_button("←", onclick=lambda: on("left")),
                 put_button("→", onclick=lambda: on("right"))], size="50px 50px")
    ])

# -------------------- Главная функция (интерфейс) --------------------
def main():
    put_markdown("# 🕹️ Пульт управления ПК")
    
    # ---------- Мышь ----------
    put_markdown("### 🖱️ Мышь")
    put_row([
        put_button("ЛКМ", onclick=lambda: on_mouse("left"), color='primary'),
        put_button("ПКМ", onclick=lambda: on_mouse("right"), color='secondary'),
        put_button("Средняя", onclick=lambda: on_mouse("middle"), color='warning'),
        put_button("Двойной", onclick=double_mouse, color='success')
    ], size="auto auto auto auto")
    put_html('<hr>')
    
    # ---------- Клавиатура ----------
    put_markdown("### ⌨️ Клавиатура")
    put_row([
        put_button("Enter", onclick=lambda: on("enter"), color='primary'),
        put_button("Space", onclick=lambda: on("space"), color='secondary'),
        put_button("Backspace", onclick=lambda: on("backspace"), color='warning'),
        put_button("Tab", onclick=lambda: on("tab"), color='info'),
        put_button("Esc", onclick=lambda: on("escape"), color='danger')
    ], size="auto auto auto auto auto")
    put_html('<hr>')
    
    # ---------- Меню (системные команды) ----------
    put_markdown("### 📂 Меню")
    put_row([
        put_button("Свернуть всё", onclick=hotkeys, color='primary'),
        put_button("Диспетчер задач", onclick=lambda: pyautogui.hotkey('ctrl', 'shift', 'esc'), color='warning'),
        put_button("Обновить страницу", onclick=lambda: run_js('window.location.reload()'), color='info', outline=True)
    ], size="auto auto auto")
    put_html('<hr>')
    
    # ---------- Монитор (яркость) ----------
    put_markdown("### 📺 Монитор")
    put_row([
        put_button("🔆 +", onclick=lambda: screen_brightness("up"), color='success'),
        put_button("🔅 -", onclick=lambda: screen_brightness("down"), color='danger'),
        put_button("100%", onclick=lambda: screen_brightness("100"), color='primary')
    ], size="auto auto auto")
    put_html('<hr>')
    
    # ---------- Дополнительно: стрелки для плеера ----------
    put_markdown("### 🎮 Управление плеером (стрелки)")
    put_row([strelki()])   # теперь strelki() возвращает Output, можно вставлять как элемент
    
    put_text("💡 Нажимайте кнопки – они эмулируют нажатия клавиш на вашем компьютере.")

# -------------------- Запуск сервера --------------------
if __name__ == '__main__':
    time.sleep(2)
    print("Сворачиваю окна и запускаю сервер...")
    pyautogui.hotkey('win', 'd')   # сразу свернуть все окна
    start_server(main, port=1337, debug=True)