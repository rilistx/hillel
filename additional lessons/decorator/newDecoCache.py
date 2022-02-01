import time
from functools import wraps
import requests


def profile(msg="Elapsed time for function"):
    def internal(f):
        @wraps(f)
        def deco(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            print(msg, f'{f.__name__}{args}: {time.time() - start}s')
            return result
        return deco

    return internal


def cache(max_limit=64):
    def internal(f):
        @wraps(f)
        def deco(url, **kwargs):

            # Если такое значение уже существует то просто его вывожу!
            if url in deco._cache:
                deco._cache[url]['counter'] += 1
                return deco._cache[url]

            # Если мой лимит меньше то добавляю значение
            if len(deco._cache) < max_limit:
                # Если такое значения ещё нет то выполняю функцию и и добавляю его в список
                result = f(url, **kwargs)
                # Инфо содержит три параметра во вложеном списаке (URL, Совершоное действие, Регулярность переходов)
                deco._cache[url] = {'result': result, 'counter': 1}
                return result

            # Если мой лимит привышен
            else:
                del_url = None

                # Нахожу менее посещаемый сайт или давно забытый если есть одинакое количество посещений
                del_url = min(deco._cache, key=lambda elem: deco._cache[elem]['counter'])

                # Удаляю этот элемент
                del deco._cache[del_url]

                # Ну и конечно записываю новый элемент по схеме выше
                result = f(url, **kwargs)
                # Инфо содержит три параметра во вложеном списаке (URL, Совершоное действие, Регулярность переходов)
                deco._cache[url] = {'result': result, 'counter': 1}
                return result

        deco._cache = {}
        return deco
    return internal


@profile(msg='Elapsed time')
@cache(max_limit=5)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
fetch_url('https://ain.ua')
fetch_url('https://youtube.com')
fetch_url('https://reddit.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://youtube.com')
fetch_url('https://reddit.com')
fetch_url('https://google.com')
fetch_url('https://google.com')


print(fetch_url._cache)
