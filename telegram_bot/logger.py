from datetime import datetime

def expression_logger(data):
    time = datetime.now().strftime('%H:%M:%S') 
    with open('log.csv', 'a') as log:
        log.write('{} Expression: {}\n'
                    .format(time, data))

def result_logger(data):
    time = datetime.now().strftime('%H:%M:%S')
    with open('log.csv', 'a') as log:
        log.write('{} Result = {}\n'
                    .format(time, data))