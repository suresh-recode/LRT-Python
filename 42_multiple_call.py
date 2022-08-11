import random
import requests
import datetime
import aiohttp
import asyncio

# print(datetime.datetime.now())


# def normal_approach():
#     list_of_url = ["https://www.google.com/", "https://www.bing.com/",
#                    "https://www.youtube.com/",
#                    "https://www.amazon.com/", "https://www.flipkart.com/"]
#     list_of_url = list_of_url * 5
#     print(f"Number of URL: {len(list_of_url)}")
#
#     for url in list_of_url:
#         r = requests.get(url)
#         print(r.status_code)
#
#
# normal_approach()
# print(datetime.datetime.now())


async def fetch(session, url):
    async with session.get(url) as response:
        return str(response.status)


async def main():
    list_of_url = ["https://www.google.com/", "https://www.bing.com/",
                   "https://www.youtube.com/",
                   "https://www.amazon.com/", "https://www.flipkart.com/"]
    list_of_url = list_of_url * 5
    print(f"Number of URL: {len(list_of_url)}")
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in list_of_url:
            # print(url)
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        # print(htmls)
        # for html in htmls:
        #     print(html[:100])


def async_approach():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


print(datetime.datetime.now())
async_approach()
print(datetime.datetime.now())
