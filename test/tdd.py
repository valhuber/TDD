import os
import sys
import pathlib
from pathlib import Path

def print_sys_path(message: str):
    """
    :return: readable, multi-line output of Python Path
    """
    sys_path = ""
    for each_node in sys.path:
        sys_path += str(each_node) + "\n"
    print(f'\n{message}\n{sys_path}')
    return sys_path

print(f'\n\n*** TDD with os.getcwd() = {os.getcwd()} ***\n')
"""
current_path = os.path.abspath(os.path.dirname(__file__))
current_path = Path(__file__)
project_dir = current_path.parent.parent
print(f'project_dir: {project_dir}')
sys.path.append(project_dir)
"""
print_sys_path("initial path")
sys.path.append("..")
print_sys_path("after sys.path append ..")
# project_dir = str(current_path)
# os.chdir(project_dir)  # so admin app can find images, code

logic_server_imports = False  # => ModuleNotFoundError: No module named 'logic'

if logic_server_imports:
    from logic_bank.logic_bank import LogicBank
    from logic_bank.exec_row_logic.logic_row import LogicRow
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import Session

from logic import declare_logic as rules
# from logic import declare_logic

rules()
rules_obj = rules.__globals__['declared_rules']
for each_rule in rules_obj:
    print(f'each_rule: {each_rule}')
print ("ha! {str(rules_obj)}")