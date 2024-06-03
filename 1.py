import asyncio
from switchbot.discovery import GetSwitchbotDevices
from switchbot.devices import lock_pro


async def main():
    wolock = await GetSwitchbotDevices().get_locks()
    print(wolock)
    lock = lock_pro.SwitchbotLockPro(wolock['CA:8C:7F:79:F5:25'].device, "cb", "498b377f92b3a0f4ce3246e63151ab50")
    await lock.get_device_data()
    print(lock.get_lock_status())

asyncio.run(main())
