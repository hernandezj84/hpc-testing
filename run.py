import src.max_number as max_number
import src.crack_password as crack_password
from datetime import datetime as dt


# epoch = datetime.datetime.utcfromtimestamp(0)

start = dt.now()
print(f"Process started: {start}")
crack_password.crack_password('abcde')
final = dt.now()
print(f"Process finished: {final}")
print(f"Result in seconds {int(final.timestamp()) - int(start.timestamp())}")
