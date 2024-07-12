from os import remove, getcwd
from core.constants import PRE_PUSH_HOOK_PATH, PRE_PUSH_SCRIPT_PATH


def delete_pre_push():
  try:
    remove(PRE_PUSH_HOOK_PATH)
    print("Pre-push hook removed successfully")
  except FileNotFoundError:
    project_path = getcwd()
    print(f"Pre-push hook not found on {project_path}/.git/hooks/")
  except Exception as e:
    print(e)
    exit(1)
    
  try:
    remove(PRE_PUSH_SCRIPT_PATH)
    print("Pre-push removed successfully")
  except FileNotFoundError:
    project_path = getcwd()
    print(f"Pre-push script not found on {project_path}")
  except Exception as e:
    print(e)
    exit(1)
  
  exit(0)