import time 
import sys 

spinner = ['|', '/', '-', '\\']

for i in range(20):
    time.sleep(0.1)
    sys.stdout.write('\rLoading... ' + spinner[i % len(spinner)])
    sys.stdout.flush()
sys.stdout.write('\rLoading... Done!     \n')

time.sleep(0.1)

