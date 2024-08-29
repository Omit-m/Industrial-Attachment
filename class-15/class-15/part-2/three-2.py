from datetime import datetime, timedelta

prev_10 = datetime.now() - timedelta(days=10)
print(prev_10)

next_10 = datetime.now() + timedelta(days=10)
print(next_10)
