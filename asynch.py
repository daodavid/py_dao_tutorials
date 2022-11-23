import asyncio, time


async def say_after(delay, what):
    for i in range(10):
        print("say after",what)
        await asyncio.sleep(delay)


async def main():
    task1 = asyncio.create_task(
        say_after(4, 'hello'))

    task2 = asyncio.create_task(
        say_after(3, 'world'))

    #k = asyncio.run( say_after(4, 'dsadas'))

    #await say_after(4, 'dasd')

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    #await task1
    #await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
