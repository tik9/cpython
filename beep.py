
# https://stackoverflow.com/a/34482761/1705829

import os,sys
import time

iterations=2
mins=1
secs=5


def progressbar(it):
    count = len(it)
    size=60
    start = time.time()
    def show(j):
        x = int(size*j/count)
        
        mins,sec = divmod(((time.time() - start) / j) * (count - j), 60)
        time_str = int(mins)
        
        print(f"[{u'█'*x}{('.'*(size-x))}] {j}/{count} Still {time_str} min")
        # os.system(f'say "still {time_str} minutes"')
        os.system(f'say "hallo"')
        
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n")


for i in progressbar(range(iterations)):
    time.sleep(mins*secs)


def another_progress():
        toolbar_width = 10

        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

        for i in range(toolbar_width):
            time.sleep(1) 
            sys.stdout.write("-")

        sys.stdout.write("]\n")
