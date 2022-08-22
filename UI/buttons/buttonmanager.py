from UI.buttons.button import Button
buttons = []


def add_button(name: str, tlc, size, onclick):
    buttons.append(Button(name, tlc, size, onclick))
    return len(buttons)  # Return index where button is found at


def clicked(mpos):
    if not buttons:
        return
    for button in buttons:
        if button.is_colliding(mpos):
            button.onclick()
