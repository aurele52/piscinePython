import time as time
from time import gmtime, strftime
since = time.time()
print(f"Seconds since January 1, 1970: {since:,.4f} or {since:.2E} in scientific notation")
print(strftime("%b %d %Y", gmtime()))
