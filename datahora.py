from datetime import datetime
import pytz

def data():
    return str(datetime.today(pytz.timezone('America/Fortaleza')).strftime("%d/%m/%y"))

def hora():
    return str(datetime.now().strftime("%H:%M:%S"))