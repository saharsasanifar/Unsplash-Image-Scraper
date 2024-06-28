import concurrent.futures
import threading
from wbs import *
import time

#getting img data single threaded-------------------------------------------

t1 = time.perf_counter()
get_photos_data(URL)
t2 = time.perf_counter()

print(f"single threaded code time: {t2-t1}")

#2 threads------------------------------------------------------------------

t3 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(3) as executer:
    executer.map(get_photos_data, URL)
t4 = time.perf_counter()

print(f"multithreaded code with 2 threads time: {t4-t3}")


