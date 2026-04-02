import asyncio

async def task1():
    print("Fun 1 started")
    await asyncio.sleep(2)
    print("Task 1 done dona done done done....")

async def task2():
    print("Fun 2 started")
    await asyncio.sleep(2)
    print("Task 2 done dona done done done....")

async def main():
    await asyncio.gather(task1(), task2())
    

asyncio.run(main())