# 2024-08-18 22:25:03.528854
# YYYY-MM-DD HH:MM:SS.milis
# DD/MM/YYYY
# 28/08/2024

from datetime import datetime

current_time = datetime.now()

format = "%d/%m/%Y %H:%M:%S"
formatted_time = current_time.strftime(format)

print(formatted_time)
