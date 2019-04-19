import inquirer
import string
from inquirer import themes
from inquirer.render.console import ConsoleRender, List
from readchar import key


class ExtendedConsoleRender(ConsoleRender):
    def render_factory(self, question_type):
        if question_type == "list":
            return ExtendedList
        return super().render_factory(question_type)


class ExtendedList(List):
    def process_input(self, pressed):
        # vi style
        if pressed in ("k"):
            pressed = key.UP
        elif pressed in ("j"):
            pressed = key.DOWN
        elif pressed == "q":
            pressed = key.CTRL_C

        # effect (rendering)
        super().process_input(pressed)


questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
        carousel=True,
    )
]

answers = inquirer.prompt(questions, render=ExtendedConsoleRender(theme=themes.Default()))
print(answers)
