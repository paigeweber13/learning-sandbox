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

- ran 5 instances of `ratelimit-test.py` for an 
  simultaneously: All of them completed 
  all 1000 requests. This amounts to approximately 5 requests per second for 
  1000 seconds.