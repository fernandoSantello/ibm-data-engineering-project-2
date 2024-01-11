from datetime import datetime

def log_process(message: str) -> None:
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open("./files/code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')
        