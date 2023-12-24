
# https://stackoverflow.com/a/34482761/1705829

import os,sys
import time

iterations=2
mins=2

def progressbar(it):
    out=sys.stdout
    count = len(it)
    size=60
    start = time.time()
    def show(j):
        x = int(size*j/count)
        
        mins,sec = divmod(((time.time() - start) / j) * (count - j), 60)
        time_str = int(mins)
        
        print(f"[{u'█'*x}{('.'*(size-x))}] {j}/{count} Still {time_str} min", end='\r', file=out, flush=True)
        
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)


for i in progressbar(range(iterations)):
    time.sleep(mins*60)
    os.system(f'say "{i*mins} minutes passed"')

os.system(f'say "{iterations*mins} minutes passed"')