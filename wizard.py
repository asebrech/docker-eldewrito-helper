import questionary
from questionary import ValidationError, Validator
import sys

class NotEmptyValidator(Validator):
    def validate(self, document):
        if not document.text:
            raise ValidationError(
                message="Please enter a value",
                cursor_position=len(document.text))  # Move cursor to end

def wizard():
    steps = ['name', 'age', 'email']
    answers = {}
    i = 0

    while i < len(steps):
        answer = None
        if steps[i] == 'name':
            answer = questionary.text("Name of the server host that will appear in the server browser?", validate=NotEmptyValidator).ask()
        elif steps[i] == 'age':
            answer = questionary.text("Name of your server?", validate=NotEmptyValidator).ask()
        elif steps[i] == 'email':
            answer = questionary.text("RCON password?", validate=NotEmptyValidator).ask()

        if answer is None:
            print("\nWizard interrupted. Exiting...")
            sys.exit(0)

        answers[steps[i]] = answer

        if i != 0 and i == len(steps) and questionary.confirm("Do you want to review your answers?").ask():
            i -= 1
        else:
            i += 1

    print(f"Thank you {answers['name']}, you are {answers['age']} years old and your email is {answers['email']}")


wizard()