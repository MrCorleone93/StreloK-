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


# ####################### V.1.0 ###############################

# def timer(f): ### це є декоратор до функції fetc_url!
#     @functools.wraps(f)
#     def started_timer_funk(*args, **kwargs): ### функція приймає два параметри!
#         start = time.time() ## перша мітка часу
#         result = f(*args, **kwargs) ## запуск батьківської функції!
#         end = time.time() ## друга мітка часу
#         print(f'\n{end - start}') ## вивід різниці часу!
#         return result ## повертаемо результат роботи батьківської функції!
#     return started_timer_funk ## так само повертає результат!
#
# def cahce(f): ### це декоратор який кешуе данні функції fetc_url!
#     @functools.wraps(f)
#     def wrapper(*args,**kwargs): ### функція приймає параметри з fetc_url! (*args,**kwargs)
#         wrapper._cahce = {} ### словник для кешування даних! (ключ:значення)
#         if args in wrapper._cahce: ### умова яка перевіряє чи є ключ в словнику!
#             return wrapper._cahce[args] ### якщо ключ є повертає його!
#         result = f(*args,**kwargs) ### запуск функції яка надходить з параметрами!
#         wrapper._cahce[args] = result ### кешує данні!
#         return result and print(wrapper._cahce) ### повертає данні з функції!
#     return wrapper ### повертає кеш данні у вигляді словника!
#
# @timer
# @cahce

# with open('test.py','w+') as f: ### це створюється та записується файл!
#     f.write(str(cahce(fetc_url('https://lms.ithillel.ua/groups/6580b6b1f1d84d874064f209/lessons/'
#                                '6580b6b2f1d84d874064f219',40))))
#
# def cache(max_limit=64):
#     def internal(f):
#         @functools.wraps(f)
#         def deco(*args, **kwargs):
#             cache_key = (args, tuple(kwargs.items()))
#             if cache_key in deco._cache:
#                 # переносимо в кінець списку
#                 deco._cache.move_to_end(cache_key, last=True)
#                 return deco._cache[cache_key]
#             result = f(*args, **kwargs)
#             # видаляємо якшо досягли ліміта
#             if len(deco._cache) >= max_limit:
#                  # видаляємо перший елемент
#                 deco._cache.popitem(last=False)
#             deco._cache[cache_key] = result
#             return result
#         deco._cache = OrderedDict()
#         return deco
#     return internal
# @cache(max_limit=64)
# def fetch_url(url, first_n=100):
#     """Fetch a given url"""
#     res = requests.get(url)
#     return res.content[:first_n] if first_n else res.content
# fetch_url('https://lms.ithillel.ua/groups/6580b6b1f1d84d874064f209/lessons/6580b6b2f1d84d874064f219', 40)
# fetch_url('https://lms.ithillel.ua/groups/6580b6b1f1d84d874064f209/lessons/6580b6b2f1d84d874064f219', 40)


# def fetch_url(url, sin=None):
#     res = requests.get(url)
#     status_code = res.status_code
#     content = res.content[:sin] if sin else res.content
#     return (f'{status_code}status_code,\n{content} content')



# url= 'https://lms.ithillel.ua/groups/6580b6b1f1d84d874064f209/lessons/6580b6b2f1d84d874064f219'
# sin = 5
# def cahce_profile(max_limit=5):
#     def cahce(f):
#         @functools.wraps(f)
#         def cehce_wrapper(*args, **kwargs):
#             cahce_key = (args, tuple(kwargs))
#             if cahce_key in _cahce:
#                 _cahce.move_to_end(cahce_key)
#                 return _cahce[cahce_key]
#             result = f(*args, **kwargs)
#             if len(_cahce) >= max_limit:
#                 _cahce.popitem(last=False)
#             _cahce[cahce_key] = result
#             return result
#         return cehce_wrapper
#
#     _cahce = OrderedDict() ### не записуються ключ та значення!
#     print(_cahce)
#
#     return cahce
#
# @cahce_profile()
# def fetch_url(url,sin=None):
#     res = requests.get(url)
#     status_code = res.status_code
#     content = res.content[:sin]
#     print(f'from {url}:\tcontent>>> {content}\nfrom {url}: status_code>>> {status_code}')
#     return url, content
#
# fetch_url(url, sin)
# cache = OrderedDict()
def cache(limit=3):
    def wrapper(f):
        @functools.wraps(f)
        def cached(*args, **kwargs):
            key = args,tuple(kwargs.items())
            if key in _cache:
                _cache.move_to_end(key)
                result = _cache[key]
                print('return content from cache:', result)
                return result
            result = f(*args, **kwargs)
            if len(_cache) > limit:
                _cache.popitem(last=False)
            _cache[key]=result
            print('\tadd content in _cache from func_url')
            return result and print('cache content:', _cache)
        return cached
    _cache = OrderedDict()
    return wrapper




@cache(limit=3)
def func_url(url,sin=None):
    res = requests.get(url)
    status = res.status_code
    content = res.content[:sin]
    print('\nstatus:', status,'\tfrom\t',url)

    return url,content
# text_list=OrderedDict()
# text_list=func_url(url,sin)
# print(text_list)
func_url('https://sky.pro/media/modul-requests-v-python/',5)
func_url('https://sky.pro/media/modul-requests-v-python/',10)
func_url("https://pythonim.ru/moduli/ordereddict-v-python",10)

func_url('https://sky.pro/media/modul-requests-v-python/',5)
func_url('https://sky.pro/media/modul-requests-v-python/',10)
func_url("https://pythonim.ru/moduli/ordereddict-v-python",10)

