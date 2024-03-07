import os
import pathlib
import random
import time
import timeit
import functools
import sys
import requests
from functools import lru_cache
from collections import OrderedDict
import functools
from memory_profiler import profile


# ####################### V.1.0 ###############################



def cache(limit=3):
    def wrapper(f):
        @functools.wraps(f)
        def cached(*args, **kwargs):
            key = args,tuple(kwargs.items())
            if key in _cache:
                _cache.move_to_end(key)
                result = _cache[key]
                print('[return content from cache content Dict]:', result)
                return result
            result = f(*args, **kwargs)
            if len(_cache) >= limit:
                _cache.popitem(last=False)
            _cache[key]=result
            print('\t[add content in _cache from func_url]')
            return result and print('[cache content from Dict]:', _cache)
        return cached
    _cache = OrderedDict()
    return wrapper



@profile
@cache(limit=2)
@profile
def func_url(url,sin=None):
    res = requests.get(url)
    status = res.status_code
    content = res.content[:sin]
    print('\nstatus:', status,'\tfrom\t',url)

    return url,content

func_url('https://sky.pro/media/modul-requests-v-python/',5)
func_url('https://sky.pro/media/modul-requests-v-python/',17)
func_url("https://pythonim.ru/moduli/ordereddict-v-python",10)

func_url('https://sky.pro/media/modul-requests-v-python/',5)
func_url('https://sky.pro/media/modul-requests-v-python/',10)
func_url("https://pythonim.ru/moduli/ordereddict-v-python",18)
func_url('https://sky.pro/media/modul-requests-v-python/',5)
func_url('https://sky.pro/media/modul-requests-v-python/',5)
func_url('https://sky.pro/media/modul-requests-v-python/',10)
func_url("https://pythonim.ru/moduli/ordereddict-v-python",18)
func_url('https://sky.pro/media/modul-requests-v-python/',5)




