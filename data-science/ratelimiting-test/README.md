# Usage
This folder contains only two simple scripts, not engineered for re-use by
other software.

- `ratelimit-test.py`: just sends requests to a url and reports when a request
  fails. URL and number of iterations are specified in-code
- `ratelimit-multithreaded.sh`: A wrapper around the python script intended to
  spawn multiple copies so that high request rates may be attempted regardless
  of the time needed to complete a single request.


# Test results
## EVGA RTX 3080 on BestBuy.com
Ran tests for [this gpu](https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6x-pci-express-4-0-graphics-card/6439300.p?skuId=6439300)

- ran 5 instances of `ratelimit-test.py` simultaneously: All of them completed
  all 1000 requests. This amounts to approximately 5 requests per second for 
  1000 seconds.
- ran 10 instances of `ratelimit-test.py` simultaneously: All of them completed
  all 1000 requests. This amounts to approximately 10 requests per second for 
  1000 seconds.
- ran 100 instances... It was very sluggish and many failed before the full 
  1000 requests were made. This seems to be more of a problem with opening 100
  terminal windows than having 100 python processes. I don't think this is
  worth the time to add python multipcrocessing so I'm just going to record
  these results and leave them here.
  - Fails: 80
  - Successes: 20
  - it's worth noting that the fails seemed to have broken connections (server
    refused the connection or ended it prematurely). This means that even if
    the requests did run smootly, bestbuy would have likely limited them.
  - rates were slower, following are some rates observed from successful runs
    - 0.64 r/s
    - 0.62 r/s
    - 0.61 r/s
  - assuming 0.6 requests per second and only counting the 20 successful runs,
    this test represents about 12 requests a second... not much more than the
    last test. 

Best buy seems to have very lax ratelimiting... So much for "taking every 
effort to combat scalpers and bots".

Conclusion: shoot for around 10 requests per second.
