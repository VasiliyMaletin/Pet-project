from os.path import exists
from tkinter import Tk, messagebox, Entry, Label, Listbox, Scrollbar, Button, NORMAL, LEFT, CENTER, END

# Добавление нового элемента
def add():
    new_task = text_box.get()
    if new_task != "":
        list_box.insert(END, text_box.get())
    else:
        messagebox.showwarning("warning", "Please enter some task.")
    text_box_clear()
    save_list_tasks()

# Удаление выделенного элемента
def delete():
    selection = list_box.curselection()
    list_box.delete(selection[0])
    save_list_tasks()

# Отчистка содержимого textbox'а
def text_box_clear():
    text_box.delete(0, "end")

# Загрузка данных из файла
def load_list_tasks():
    list_data = []
    if not exists('tasks.txt'):
        save_list_tasks()
    else:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            for item in file:
                list_data.append(item.strip()) 
 
    return list_data

# Сохранение данных в файл
def save_list_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for item in list_box.get(0, "end"):
            file.write("%s\n" % item) 

# Инициализация программы
def window_init():
    global text_box
    global list_box

    # Задаём стиль и размер шрифта
    common_font = ("Arial", 14)
    bold_font = ("Arial", 20, "bold")
 
    # Задание начальных данных по окну 
    window_app = Tk()
    window_app.title("To-Do List")
    window_app_width = 800
    window_app_height = 450
    window_app.columnconfigure(1, weight=1)
    window_app.columnconfigure(2, weight=1)

    # Расчет координат окна, чтобы при выводе оно оказалось по центру экрана
    sw = window_app.winfo_screenwidth()
    sh = window_app.winfo_screenheight()
    x = (sw - window_app_width) / 2
    y = (sh - window_app_height) / 2

    # Задание размеров окна и его начального положения при выводе   
    window_app.geometry(f"{window_app_width}x{window_app_height}+{int(x)}+{int(y)}")

    # Создание подписи и текстового поля для ввода данных
    text_box = Entry(window_app, state=NORMAL , font=common_font)
    text_box.grid(row=1, column=0, columnspan=3, sticky="news", padx=15, pady=5)
    label_window = Label(window_app, text="Daily Tasks", justify=CENTER, font=bold_font)
    label_window.grid(row=0, column=0, columnspan=4, sticky="ewns", padx=5, pady=5)

    # Создание Listbox со ScrollBar для вывода информации
    scrollbar = Scrollbar(window_app)
    scrollbar.grid(row=2, column=2, rowspan=6, sticky="ens")
    list_box = Listbox(window_app, justify=LEFT, font=common_font)
    list_box.config(yscrollcommand=scrollbar.set, width=50)
    scrollbar.config(command=list_box.yview)
    list_box.grid(row=2, column=0, rowspan=6, columnspan=3, sticky="news", padx=15, pady=5)
    
    # Добавляем в Listbox начальные элементы
    list_tasks = load_list_tasks()
    for item in list_tasks:
        list_box.insert(END, item)
 
    # Создание управляющих кнопок
    add_button = Button(window_app, font=common_font, text='Add', command=add)
    add_button.configure(bg='DodgerBlue3', fg='White')
    add_button.grid(column=0, row=8, columnspan=3, sticky="ew", padx=15, pady=5)

    delete_button = Button(window_app, font=common_font, text='Delete', command=delete)
    delete_button.configure(bg='DodgerBlue3', fg='White')
    delete_button.grid(column=0, row=9, columnspan=3, sticky="ew", padx=15, pady=5)
 
    # Цикл для постоянной работы программы
    window_app.mainloop()


if __name__ == '__main__':
    window_init()
