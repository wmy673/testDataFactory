import time
import psutil

def monitor_performance(interval: float = 1.0, duration: float = 10.0) -> list:
    """
    监控系统的 CPU 和内存使用率。

    :param interval: 采样间隔（秒）
    :param duration: 监控总时长（秒）
    :return: 性能数据列表，每项为字典，包含时间戳、CPU 和内存使用率
    """
    performance_data = []
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_percent = psutil.cpu_percent(interval=None)
        mem_percent = psutil.virtual_memory().percent
        timestamp = time.time()
        performance_data.append({
            "timestamp": timestamp,
            "cpu_percent": cpu_percent,
            "mem_percent": mem_percent
        })
        time.sleep(interval)
    return performance_data

# 示例用法
if __name__ == "__main__":
    data = monitor_performance(interval=1.0, duration=5.0)
    for entry in data:
        print(f"时间戳: {entry['timestamp']:.2f}, CPU: {entry['cpu_percent']}%, 内存: {entry['mem_percent']}%")
