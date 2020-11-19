import asyncio
import aiohttp
import time

# sem = asyncio.Semaphore(100)

query = 'Besson'
queryBytes = str.encode(query)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
url = 'https://contactout.com/people-directory/professional-profile/{}-2-{}'
urls = []

for letter in letters:
    for n in range(0, 12500):
        contactUrl = url.format(letter, n)
        urls.append(contactUrl)


async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                if (resp.find(queryBytes) > -1):
                    print('FOUND QUERY IN : {}'.format(url))
    except Exception as e:
        a = e
        # print("Unable to get url {} due to {}.".format(url, e))


async def main(urls):
    ret = await asyncio.gather(*[get(url) for url in urls])
    # print("Finished a batch: {} outputs.".format(len(ret)))

amount = len(urls)

urlsIndex = 0
batchSize = 250

start = time.time()

while urlsIndex < len(urls):
    asyncio.run(main(urls[urlsIndex:urlsIndex+batchSize]))
    urlsIndex += batchSize

end = time.time()

print("Took {} seconds to pull {} websites.".format(end - start, amount))
