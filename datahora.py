from datetime import datetime

def data():
    return str(datetime.today().strftime("%d/%m/%y"))

def hora():
    return str(datetime.now().strftime("%H:%M:%S"))