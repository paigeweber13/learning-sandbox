import requests
import time

DELAY = 0 # delay in seconds
ITERATIONS = 1000 # number of times to repeat
#ITERATIONS = 1# number of times to repeat

# url to test rate-limiting with
URL = 'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6x-pci-express-4-0-graphics-card/6439300.p?skuId=6439300'

# very common windows user-agent, seems to get blocked more frequently as a bot
#HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# my user-agent on this machine
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}

finished = True
start_time = time.time()
for i in range(ITERATIONS):
	r = requests.get(URL, headers=HEADERS)

	if not r.ok:
		print("FAILED ON ITERATION {:d}/{:d} WITH DELAY {:.2f}: Got error {:d}"
			" with reason '{}'. Body is printed below:\n{}"
			.format(i + 1, ITERATIONS, DELAY, r.status_code, r.reason, r.text))
		finished = False
		break

	elapsed_time = time.time() - start_time
	print("Completed iteration {:d}/{:d}. Request rate so far for this process"
		" is {.2f} requests per second"
		.format(i+1, ITERATIONS, i/elapsed_time))
	time.sleep(DELAY)

if finished:
	print("Completed all {:d} iterations!".format(ITERATIONS))
