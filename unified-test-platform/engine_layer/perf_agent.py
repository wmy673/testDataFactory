import psutil
import time
import threading
from typing import Callable, List, Dict

class PerfAgent:
    """
    性能采集代理，用于定时采集本机的 CPU、内存等资源使用情况。
    支持自定义采集回调和多线程安全。
    """

    def __init__(self, interval: float = 1.0):
        """
        初始化性能采集代理。

        :param interval: 采样间隔（秒）
        """
        self.interval = interval
        self._running = False
        self._thread = None
        self.data: List[Dict] = []
        self.callback: Callable[[Dict], None] = None

    def _collect(self):
        """
        内部线程方法，定时采集性能数据。
        """
        while self._running:
            info = {
                "timestamp": time.time(),
                "cpu_percent": psutil.cpu_percent(interval=None),
                "mem_percent": psutil.virtual_memory().percent
            }
            self.data.append(info)
            if self.callback:
                self.callback(info)
            time.sleep(self.interval)

    def start(self, callback: Callable[[Dict], None] = None):
        """
        启动性能采集。

        :param callback: 每次采集后调用的回调函数，参数为采集到的数据字典
        """
        if not self._running:
            self._running = True
            self.callback = callback
            self._thread = threading.Thread(target=self._collect, daemon=True)
            self._thread.start()
            print("性能采集代理已启动")

    def stop(self):
        """
        停止性能采集。
        """
        self._running = False
        if self._thread:
            self._thread.join()
            print("性能采集代理已停止")

    def get_data(self) -> List[Dict]:
        """
        获取采集到的所有性能数据。

        :return: 性能数据列表
        """
        return self.data

# 示例用法
if __name__ == "__main__":
    agent = PerfAgent(interval=1.0)
    agent.start()
    try:
        time.sleep(5)
    finally:
        agent.stop()
        for entry in agent.get_data():
            print(f"时间戳: {entry['timestamp']:.2f}, CPU: {entry['cpu_percent']}%, 内存: {entry['mem_percent']}%")
