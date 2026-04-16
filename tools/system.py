import psutil
import platform
from datetime import datetime


def get_system_info() -> dict:
    """Returns current system stats from the laptop."""
    battery = psutil.sensors_battery()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "os": platform.system(),
        "pc_name": platform.node(),
        "processor": platform.processor(),
        "cpu_usage": f"{psutil.cpu_percent(interval=1)}%",
        "cpu_cores": psutil.cpu_count(),
        "ram_total": f"{round(memory.total / 1e9, 1)} GB",
        "ram_used": f"{memory.percent}%",
        "disk_total": f"{round(disk.total / 1e9, 1)} GB",
        "disk_used": f"{disk.percent}%",
        "battery": f"{round(battery.percent)}%" if battery else "No battery",
        "charging": battery.power_plugged if battery else None,
    }


def get_current_time() -> str:
    """Returns the current time and date as a readable string."""
    return datetime.now().strftime("%A, %d %B %Y at %I:%M %p")
