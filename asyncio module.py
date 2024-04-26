import asyncio

async def greet():
    print('first')
    await asyncio.sleep(10)
    print('second')

asyncio.run(greet())