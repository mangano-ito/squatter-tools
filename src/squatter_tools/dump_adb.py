import sys, asyncio
from .logcat import Logcat

def main1():
    for line in (buffer.rstrip('\r\n') for buffer in sys.stdin):
        print(line)

# adb logcat -s "squatter-debug" -v raw

async def tail():
    logcat = Logcat()
    await logcat.open()
    async for data in logcat.listen2():
        print(data)

def main():
    asyncio.run(tail())