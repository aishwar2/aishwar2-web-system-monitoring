import psutil
import datetime
import platform
from flask import Flask, render_template

app = Flask(__name__)

def get_system_info():
    # Retrieve CPU, memory, and storage information
    cpu_load = psutil.cpu_percent()
    mem_load = psutil.virtual_memory().percent
    storage_info = psutil.disk_usage('/')
    os_info = platform.uname()

    # Calculate uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    current_time = datetime.datetime.now()
    uptime = current_time - boot_time

    # Get CPU temperature
    temperature_info = psutil.sensors_temperatures()
    cpu_temp_celsius = temperature_info.get('coretemp')[0].current

    return cpu_load, mem_load, storage_info, uptime, os_info, cpu_temp_celsius

@app.route('/')
def index():
    cpu_load, mem_load, storage_info, uptime, os_info, cpu_temp_celsius = get_system_info()

    # Determine system status message
    if cpu_load > 70:
        status_message = "CPU Load is high"
    elif mem_load > 70:
        status_message = "Memory Load is high"
    elif storage_info.percent > 70:
        status_message = "Storage Load is high"
    elif uptime.total_seconds() < 120:  # 2 minutes
        status_message = "System is starting up"
    elif cpu_load > 60 and mem_load > 40 and storage_info.percent > 40:
        status_message = "System is overloading"
    elif cpu_temp_celsius > 80:
        status_message = "CPU temperature is high"
    elif cpu_temp_celsius > 60:
        status_message = "CPU temperature is heating"
    else:
        status_message = "System is normal"

    # Format uptime for display
    uptime_str = str(uptime).split('.')[0]  # Remove microseconds

    return render_template('index.html', cpu_load=cpu_load, mem_load=mem_load,
                           storage_used_gb=storage_info.used / (1024 ** 3),
                           uptime_str=uptime_str, os_system=os_info.system,
                           os_release=os_info.release, status_message=status_message,
                           cpu_temp_celsius=cpu_temp_celsius)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)