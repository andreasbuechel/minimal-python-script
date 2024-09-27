import asyncio

import aiohttp


def get_secret() -> str:
    ## This should come from a secret manager
    return "123abc"


async def main():
    secret = get_secret()

    async with (aiohttp.ClientSession() as session):
        async with session.post(
                f"https://echo.free.beeceptor.com", params={"s": secret, "p1": [1, 2, 3]}, json={"k1": {"k2": "v2"}}
        ) as response:
            if 200 <= response.status < 300:
                print(await response.json())
            else:
                text = await response.text()
                raise RuntimeError(f"{response.status} - {text}")


if __name__ == '__main__':
    asyncio.run(main())
