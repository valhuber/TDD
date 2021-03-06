import requests

def prt(msg: any, test: str= None) -> None:
    """
    print to console, and logic_logger / server_log (see api/customize_api.py)
    """
    # print(msg)
    test_val = test
    if test is not None and len(test) >= 26:
        test_val = test[0:25]
    msg_url = f'http://localhost:5656/server_log?msg={msg}&test={test}&dir=test/api_logic_server_behave/scenario_logic_logs'
    r = requests.get(msg_url)

if __name__ == "__main__":
    print(f'\n test_services.py, starting')
