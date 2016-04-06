# pyecmc - A Python module that wraps python-memcached with AWS Elasticache autodiscovery.

[![Build Status](https://travis-ci.org/saebyn/pyecmc.svg?branch=master)](https://travis-ci.org/saebyn/pyecmc)

## Introduction
Provides a `ecmc.MemcacheClient` class that uses AWS Elasticache autodiscovery
to find all servers in the Elasticache cluster, proxy's `memcache.Client` from
[python-memcached](https://pypi.python.org/pypi/python-memcached), and uses
[hash_ring](https://pypi.python.org/pypi/hash_ring/) to provide consistent
hashing to determine the correct server within the cluster for a given key
even when servers are added or removed.

For detail on AWS Elasticache autodiscovery, please reference:

http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/AutoDiscovery.html



## Installation

```bash
    $ pip install ecmc
```


## Code example

```python
    >>> from ecmc import MemcacheClient
    >>> mc = MemcacheClient('test.lwgyhw.cfg.usw2.cache.amazonaws.com:11211')
    >>> mc.set('foo', 'bar')
    True
    >>> mc.get('foo')
    'bar'
```

All methods available for `memcached.Client` from python-memcached are
available on the `MemcacheClient` instance.


## License

GNU LGPL v3. See the `LICENSE` file.
