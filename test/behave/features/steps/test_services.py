import requests

def prt(msg: any, test: str= None) -> None:
    """
    print to console, and server_log (see api/customize_api.py)
    """
    # print(msg)
    msg_url = f'http://localhost:5656/server_log?msg={msg}&test={test}&dir=test/behave/results'
    r = requests.get(msg_url)
