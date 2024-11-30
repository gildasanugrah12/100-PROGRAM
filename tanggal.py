from datetime import datetime

sekarang = datetime.now()

data = sekarang.strftime("%A,%d of %B on %Y,%I:%M:%S %p")
print(data)