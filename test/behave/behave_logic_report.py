import requests
from pathlib import Path
import os

"""
Creates wiki file from test/behave/behave.log, with rule use.

Tips
* use 2 spaces (at end) for newline
* for tab: & emsp;

"""

tab = "&emsp;"
debug_info = "# features"
wiki_data = []

def show_logic(scenario: str):
    wiki_data.append("<details>")
    wiki_data.append("<summary>Tests - *and their logic* are transparent.. click to see Logic</summary>")
    wiki_data.append("\n")
    wiki_data.append("```")
    logic_file_name = f'test/behave/results/{scenario}.log'
    logic_file_name_path = Path(logic_file_name)
    if not logic_file_name_path.is_file():
        wiki_data.append(f'unable to find logic file: {logic_file_name}')
    else:
        wiki_data.append(f'*** here is the logic for: {scenario} ***')
        with open(logic_file_name) as logic:
            logic_lines = logic.readlines()
        for each_logic_line in logic_lines:
            wiki_data.append(each_logic_line[:-1] + "  ")
    wiki_data.append("```")
    wiki_data.append("</details>")




def main(file: str):
    contents = None
    with open(file) as f:
        contents = f.readlines()

    just_saw_then = False
    current_scenario = ""
    for each_line in contents:
        if just_saw_then and each_line == "\n":
            show_logic(current_scenario)
        just_saw_then = False
        if each_line.startswith("Feature"):
            wiki_data.append("&nbsp;")
            wiki_data.append("&nbsp;")
            each_line = "# " + each_line
        if each_line.startswith("  Scenario"):
            each_line = tab + each_line
        if each_line.startswith("    Given") or \
                each_line.startswith("    When") or \
                each_line.startswith("    Then"):
            if each_line.startswith("    Then"):
                just_saw_then = True
            each_line = tab + tab + each_line

        each_line = each_line[:-1]
        debug_loc = each_line.find(debug_info)
        if debug_loc > 0:
            each_line = each_line[0 : debug_loc]
        each_line = each_line.rstrip()
        if "Scenario" in each_line:
            current_scenario = each_line[18:]
            wiki_data.append("&nbsp;")
            wiki_data.append("&nbsp;")
            wiki_data.append("## " + each_line[8:])

        each_line = each_line + "  "  # wiki for "new line"
        
        wiki_data.append(each_line)

    with open(r'test/behave/behave_logic_report.txt', 'w') as rpt:
        rpt.write('\n'.join(wiki_data))

if __name__ == "__main__":
    print(f'\n Behave Logic Report.py, starting at {os.getcwd()}')
    main(file = 'test/behave/behave.log')
