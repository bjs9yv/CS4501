Improve the look of search results, create listing, logout pages
Add listings to a shopping cart if logged in
Add listings to a shopping cart without being loged in (using cookies)
Remove listings if you are the owner of them
Add pictures of development process from iphone
Clean up the codebase

# Spark 

- '''https://github.com/thomaspinckney3/cs4501/blob/master/Project7.md'''

# Load Balancing

- Run multiple instances of your app tiers with a load balancer in front to distribute the load across all the instances. For example, if you have two copies of your web front end the load balance will sit in front of it, receive connections from browsers, and forward them on to one or the other of the web front end instances. 'pen' is a common and relatively simple one and is available as a Docker image at '''https://hub.docker.com/r/galexrt/pen/''' .

# Caching

- Redis
- Install the Python Redis client '''https://pypi.python.org/pypi/redis''' with pip and start a Redis docker image such as '''https://hub.docker.com/_/redis/''' .

You can't use Django's caching interfaces to configure whole page caching with Redis without using additonal packages. Instead just directly call the Redis python client to store pages and later look them up. Think about how and when to invalidate the cache'd content (after a certain amount of time? when the DB changes? something else?). 

# Bitcoin payments

- check out ```https://hub.docker.com/r/checkoutcrypto/bitcoin/ ``` for using docker to build a bitcoin container
  - aborted because Blockchain is 40Gb and I didn't have time in the class I was in to copy the whole thing  
- check out ```http://python-bitcoinlib.readthedocs.org/en/latest/started.html``` for installing a python bitcoin API
- check out ```http://bitcoin.stackexchange.com/questions/24571/how-to-make-a-simple-payment-with-the-python-bitcoinlib``` for example code for making a payment with python-bitcoinlib
