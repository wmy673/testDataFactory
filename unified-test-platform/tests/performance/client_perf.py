import time
import psutil

def measure_client_performance(duration: float = 10.0, interval: float = 1.0) -> dict:
    """
    测量本地客户端在指定时间内的 CPU 和内存使用率。

    :param duration: 测试总时长（秒）
    :param interval: 采样间隔（秒）
    :return: 包含平均/最大/最小 CPU 和内存使用率的统计字典
    """
    cpu_list = []
    mem_list = []
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory().percent
        cpu_list.append(cpu)
        mem_list.append(mem)
        print(f"采样: CPU={cpu:.2f}%, 内存={mem:.2f}%")
        time.sleep(interval)
    if cpu_list and mem_list:
        return {
            "cpu_avg": sum(cpu_list) / len(cpu_list),
            "cpu_max": max(cpu_list),
            "cpu_min": min(cpu_list),
            "mem_avg": sum(mem_list) / len(mem_list),
            "mem_max": max(mem_list),
            "mem_min": min(mem_list),
            "samples": len(cpu_list)
        }
    else:
        return {
            "cpu_avg": None,
            "cpu_max": None,
            "cpu_min": None,
            "mem_avg": None,
            "mem_max": None,
            "mem_min": None,
            "samples": 0
        }

# 示例用法
if __name__ == "__main__":
    result = measure_client_performance(duration=5, interval=1)
    print("客户端性能统计：", result)
