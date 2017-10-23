import asyncio
import aiohttp
from time import time
from urllib.request import urlopen


def logging_execution_time(func):
    async def wrapper(*args, **kwargs):
        st = time()
        result = await func(*args, **kwargs)
        print("Execution time: {:.03} seconds.\n Argruments: {}".format(
            time() - st, *args    
            ))
        return result
    return wrapper


@logging_execution_time
async def open_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res: 
            print("Executing url: %s" % url)
            return await res.text()


async def main():
    urls = [
            'http://www.naver.com',
            'http://forfree.tistory.com',
            'https://selo77.github.io',
            'https://www.google.com',
            'http://www.daum.net'
            ]
    test_urls = urls * 100
    tasks = [open_url(u) for u in test_urls]
    r = await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    st = time()
    loop.run_until_complete(main())
    print("\n\n Total of Runtime : {:.03}".format(time()-st))
