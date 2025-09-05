import threading
import queue
from typing import Callable, Any

class JobQueue:
    """
    简单的作业队列，支持多线程安全的任务入队和出队，并可自动调度执行。
    """

    def __init__(self, worker_num: int = 1):
        """
        初始化作业队列。

        :param worker_num: 工作线程数量
        """
        self.job_queue = queue.Queue()
        self.worker_num = worker_num
        self.workers = []
        self._running = False

    def add_job(self, func: Callable, *args, **kwargs):
        """
        添加一个作业到队列。

        :param func: 要执行的函数
        :param args: 函数的位置参数
        :param kwargs: 函数的关键字参数
        """
        self.job_queue.put((func, args, kwargs))

    def _worker(self):
        """
        工作线程方法，循环处理队列中的作业。
        """
        while self._running:
            try:
                func, args, kwargs = self.job_queue.get(timeout=1)
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print(f"作业执行异常: {e}")
                self.job_queue.task_done()
            except queue.Empty:
                continue

    def start(self):
        """
        启动所有工作线程，开始处理作业队列。
        """
        if not self._running:
            self._running = True
            for _ in range(self.worker_num):
                t = threading.Thread(target=self._worker, daemon=True)
                t.start()
                self.workers.append(t)
            print(f"作业队列已启动，工作线程数: {self.worker_num}")

    def stop(self):
        """
        停止所有工作线程，等待当前作业完成。
        """
        self._running = False
        for t in self.workers:
            t.join()
        print("作业队列已停止")

    def wait_all(self):
        """
        阻塞直到所有作业处理完成。
        """
        self.job_queue.join()

# 示例用法
if __name__ == "__main__":
    import time

    def example_job(x):
        print(f"处理作业: {x}")
        time.sleep(1)

    jq = JobQueue(worker_num=2)
    jq.start()
    for i in range(5):
        jq.add_job(example_job, i)
    jq.wait_all()
    jq.stop()
