import requests

def prt(msg: any, test: str= None) -> None:
    """
    print to console, and logic_logger / server_log (see api/customize_api.py)
    """
    # print(msg)
    msg_url = f'http://localhost:5656/server_log?msg={msg}&test={test}&dir=test/api_logic_server_behave/results_when'
    r = requests.get(msg_url)

if __name__ == "__main__":
    print(f'\n test_services.py, starting')
