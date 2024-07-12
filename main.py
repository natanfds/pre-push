from core.constants import LANGUAGES
import inquirer
from os import getcwd
from core.delete_pre_push import delete_pre_push
from core.add_pre_push import add_pre_push

def main():
  questions_lang = [
      inquirer.List('choice',
                    message="Select the current project programming language",
                    choices=[*LANGUAGES, "REMOVE PRE-PUSH"],
                    ),
  ]

  answers_lang = inquirer.prompt(questions_lang)

  current_path = getcwd()
  questions_confirm = [
      inquirer.Confirm('confirm',
                        message="Are you sure you want add a pre-push to this project?\n" + 
                        f"PATH: {current_path}\n" +
                        f"LANGUAGE: {answers_lang['choice']}\n",
                        default=True,
                        ),
  ]

  answers_confirm = inquirer.prompt(questions_confirm)

  if not answers_confirm['confirm']:
      exit(0)

  if answers_lang['choice'] == "REMOVE PRE-PUSH":
      delete_pre_push()
  else:
      add_pre_push(answers_lang['choice'])
      print("Pre-push added successfully")

if __name__ == "__main__":
  main()