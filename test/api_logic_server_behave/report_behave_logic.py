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
debug_scenario = "Custom Service: add_order - good"


def remove_trailer(line: str) -> str:
    """ remove everything after the ## """
    end_here = line.find("\t\t##")
    result = line[0:end_here]
    return result


def show_logic(scenario: str):
    """ insert scenario.log into wiki_data as disclosure area """
    scenario_trunc = scenario
    if scenario_trunc is not None and len(scenario_trunc) >= 26:
        scenario_trunc = scenario[0:25]
    scenario_trunc = f'{str(scenario_trunc).replace(" ", "_")}'
    logic_file_name = f'results_when/{scenario_trunc}.log'
    logic_file_name_path = Path(logic_file_name)
    if not logic_file_name_path.is_file():
        wiki_data.append(f'unable to find LogicLog file: {logic_file_name}')
        if scenario == debug_scenario:
            print(f'RELATIVE: {logic_file_name} in {os.getcwd()}')
            full_name = f'{os.getcwd()}/{logic_file_name}'
            print(f'..FULL: {os.getcwd()}/{logic_file_name}')
            logic_file_name = 'results_when/test.log'
            with open(logic_file_name) as logic:
                logic_lines = logic.readlines()
            # finder:  /Users/val/dev/TDD/test/api_logic_server_behave/results_when
            # seeking: /Users/val/dev/TDD/test/api_logic_server_behave/results_when/Custom Service: add_order - good.log
    else:
        logic_log = []
        rules_used = []
        is_logic_log = True
        wiki_data.append("<details>")
        wiki_data.append("<summary>Tests - and their logic - are transparent.. click to see Logic</summary>")
        wiki_data.append("\n")
        wiki_data.append("&nbsp;")
        wiki_data.append("&nbsp;")
        wiki_data.append("\n")
        wiki_data.append(f'**Rules Used** in Scenario: {scenario}')
        wiki_data.append("```")
        with open(logic_file_name) as logic:
            logic_lines = logic.readlines()
        for each_logic_line in logic_lines:
            if is_logic_log:
                if "Rules Fired" in each_logic_line:
                    is_logic_log = False
                    continue
                else:
                    logic_log.append(each_logic_line)
            else:
                each_logic_line = remove_trailer(each_logic_line)
                wiki_data.append(each_logic_line + "  ")
        wiki_data.append("```")
        wiki_data.append(f'**Logic Log** in Scenario: {scenario}')
        wiki_data.append("```")
        for each_logic_log in logic_log:
            wiki_data.append(each_logic_log[0:-1])
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

    with open('report_behave_logic.txt', 'w') as rpt:
        rpt.write('\n'.join(wiki_data))
    print(f'* Output: report_behave_logic.txt\n***\n\n')

if __name__ == "__main__":
    print(f'\n***\n* Begin:  starting Behave Logic Report.py, at {os.getcwd()}')
    main(file = 'behave.log')
