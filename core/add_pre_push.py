from core.constants import DEFAULT_SCRIPTS, PRE_PUSH_BASE_SCRIPT, PRE_PUSH_HOOK_PATH, PRE_PUSH_SCRIPT_PATH, TYPING_LANGUAGES
from os import remove

def add_pre_push(language: TYPING_LANGUAGES):
  try:
    file = open(PRE_PUSH_HOOK_PATH, "w")
    file.write(PRE_PUSH_BASE_SCRIPT)
    file.close()
  except Exception as e:
    print(e)
    exit(1)
  
  try:
    default_script = open(PRE_PUSH_SCRIPT_PATH, "w")
    default_script.write(DEFAULT_SCRIPTS[language])
    default_script.close()
  except Exception as e:
    remove(PRE_PUSH_HOOK_PATH)
    print(e)
    exit(1)