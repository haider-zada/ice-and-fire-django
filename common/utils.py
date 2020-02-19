"""This py file will contain all common functions"""

def create_response(status_code, status, data):

    result = {
        "status_code": status_code,
        "status": status,
        "data": data
    }
    return result
