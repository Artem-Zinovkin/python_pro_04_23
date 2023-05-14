import asyncio
from pprint import pprint as print

import httpx


async def _fetch_from_api(url):
    async with httpx.AsyncClient() as client:
        response = (await client.get(url=url)).json()
        return response


async def main():
    url1 = (
        "https://www.alphavantage."
        "co/query?function=CURRENCY_EXCHANGE_RATE&"
        "from_currency=USD&to_currency=UAH"
        "&apikey=SFMIOG4S7VVMK9JL "
    )
    url2 = (
        "https://www.alphavantage."
        "co/query?function=CURRENCY_EXCHANGE_RATE&"
        "from_currency=EUR&to_currency=UAH"
        "&apikey=SFMIOG4S7VVMK9JL "
    )
    url3 = (
        "https://www.alphavantage."
        "co/query?function=CURRENCY_EXCHANGE_RATE&"
        "from_currency=EUR&to_currency=USD"
        "&apikey=SFMIOG4S7VVMK9JL "
    )
    url4 = (
        "https://www.alphavantage."
        "co/query?function=CURRENCY_EXCHANGE_RATE&"
        "from_currency=USD&to_currency=EUR"
        "&apikey=SFMIOG4S7VVMK9JL "
    )

    url5 = (
        "https://www.alphavantage."
        "co/query?function=CURRENCY_EXCHANGE_RATE&"
        "from_currency=GBP&to_currency=EUR"
        "&apikey=SFMIOG4S7VVMK9JL "
    )

    task = [
        _fetch_from_api(url1),
        _fetch_from_api(url2),
        _fetch_from_api(url3),
        _fetch_from_api(url4),
        _fetch_from_api(url5),
    ]
    print(await asyncio.gather(*task))


if __name__ == "__main__":
    asyncio.run(main())
