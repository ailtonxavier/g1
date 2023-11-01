from datetime import datetime
import pytz

def data():
    return datetime.today().strftime("%d/%m/%y")

def hora():
    return str(datetime.now(pytz.timezone('America/Fortaleza')).strftime("%H:%M:%S"))