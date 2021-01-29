def add_digit(digit):
    value = calc.get()  # Получаю последние данные, которые были введены
    if value == "0":
        value = value[1:]  # Беру всё, кроме первого символа
    calc.delete(0, END)  # Ощичаю ввод
    calc.insert(0, value + digit)  # Вставляю данные


def add_operation(operation):
    value = calc.get()
    if value[-1] in "+-/*":
        value = value[:-1]  # Вставляю всё, кроме последнего символа
    elif "+" in value or "-" in value or "/" in value or "*" in value:
        calculate()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + operation)


def clear():
    calc.delete(0, END)
    calc.insert(0, 0)


def calculate():
    value = calc.get()
    if value[-1] in "+-/*":
        value = value + value[:-1]  # Вставляю всё, кроме последнего символа
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        tk.messagebox.showinfo(
            title="Внимание",
            message="Нужно вводить только цифры. Вы ввели другие символы! ",
        )
        calc.insert(0, 0)
    except ZeroDivisionError:
        tk.messagebox.showinfo(title="Внимание", message="На 0 делить нельзя ! ")
        calc.insert(0, 0)


def make_digit_button(digit):
    return tk.Button(
        text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit)
    )


def make_operation_button(operation):
    return tk.Button(
        text=operation,
        bd=5,
        font=("Arial", 13),
        fg="red",
        command=lambda: add_operation(operation),
    )


def make_calc_button(operation):
    return tk.Button(
        text=operation, bd=5, font=("Arial", 13), fg="red", command=calculate
    )


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red", command=clear)


def press_key(event):
    # repr-
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-/*":
        add_operation(event.char)
    elif event.char == "\r":
        calculate()


def on_closing():  # Окно подвтреждения о закрытии
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        win.destroy()


# \r это символ Enter'а, когда я нажимаю на него