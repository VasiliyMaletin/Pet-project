import operations
import logger as log

def distribution(data):
    data = data.replace(' ','')
    if 'i' or 'j' in data:
        data = data.replace('i','j')
        data = data.replace('+j','+1j')
        data = data.replace('-j','-1j')
        data = data.replace('/j','/1j')
        data = data.replace('*j','*1j')
        data = data.replace('(j','(1j')
        if data[0] == 'j': data = '1' + data
        result = operations.complex_calc(data)
    else:
        result = operations.rational_calc(data)
    log.expression_logger(data)
    log.result_logger(result)
    return result