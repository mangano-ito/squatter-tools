import time, asyncio, json

# command = ("adb", "logcat", "-s", "squatter-sensor-events", "-v", "raw")
command = ("adb", "logcat", "-s", "squatter-debug", "-v", "raw")

class Logcat:
    def __init__(self):
        self.proc = None

    async def open(self):
        self.proc = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
        )

    async def listen(self):
        while True:
            line = await self.proc.stdout.readline()
            try:
                yield json.loads(line)
            except Exception as _:
                pass

    async def listen_a(self):
        while True:
            line = await self.proc.stdout.readline()
            try:
                yield float(line)
            except Exception as _:
                pass
