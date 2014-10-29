from __future__ import print_function, unicode_literals, absolute_import

import toga


def button_handler(widget):
    print("Hello KA Lite!")


def build(app):
    container = toga.Container()

    button = toga.Button('Hello KA Lite', on_press=button_handler)

    container.add(button)

    container.constrain(button.TOP == container.TOP + 50)
    container.constrain(button.LEADING == container.LEADING + 50)
    container.constrain(button.TRAILING + 50 == container.TRAILING)
    container.constrain(button.BOTTOM + 50 < container.BOTTOM)

    return container


if __name__ == '__main__':
    app = toga.App('KA Lite Setup', 'test', startup=build)

    app.main_loop()
