import time
import threading

class HeartbeatMonitor:
    """
    心跳监控器，用于定期检测目标服务或进程的存活状态。
    """

    def __init__(self, check_func, interval: float = 5.0):
        """
        初始化心跳监控器。

        :param check_func: 检查目标存活状态的函数，应返回 True（存活）或 False（异常）
        :param interval: 心跳检测间隔（秒）
        """
        self.check_func = check_func
        self.interval = interval
        self._running = False
        self._thread = None

    def _monitor(self):
        """
        内部线程方法，定期调用检查函数。
        """
        while self._running:
            alive = self.check_func()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if alive:
                print(f"[{timestamp}] 心跳正常")
            else:
                print(f"[{timestamp}] 心跳异常，目标未响应！")
            time.sleep(self.interval)

    def start(self):
        """
        启动心跳监控线程。
        """
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._monitor, daemon=True)
            self._thread.start()
            print("心跳监控已启动")

    def stop(self):
        """
        停止心跳监控线程。
        """
        self._running = False
        if self._thread:
            self._thread.join()
            print("心跳监控已停止")

# 示例用法
if __name__ == "__main__":
    # 示例检查函数：模拟目标每次都存活
    def mock_check():
        return True

    monitor = HeartbeatMonitor(check_func=mock_check, interval=2.0)
    monitor.start()
    try:
        time.sleep(10)  # 运行 10 秒
    finally:
        monitor.stop()
