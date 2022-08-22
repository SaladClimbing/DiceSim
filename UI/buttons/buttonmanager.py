from UI.buttons.button import Button
buttons = []


def add_button(name: str, tlc, size):
    buttons.append(Button(name, tlc, size))
    return len(buttons)  # Return index where button is found at


def click(mpos):
    if not buttons:
        return
    for button in buttons:
        if button.is_colliding(mpos):
            print("Clicked :", button.name)
