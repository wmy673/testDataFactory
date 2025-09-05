import threading

class MachinePool:
    """
    机器池，用于管理和分配可用的测试/构建机器资源。
    支持线程安全的资源分配与回收。
    """

    def __init__(self, machines: list):
        """
        初始化机器池。

        :param machines: 机器列表，每个元素可为机器名、IP 或机器描述信息
        """
        self._machines = machines.copy()
        self._lock = threading.Lock()
        self._in_use = set()

    def acquire(self) -> str:
        """
        分配一台空闲机器。

        :return: 分配到的机器标识
        :raises RuntimeError: 如果没有可用机器
        """
        with self._lock:
            available = [m for m in self._machines if m not in self._in_use]
            if not available:
                raise RuntimeError("没有可用的机器资源")
            machine = available[0]
            self._in_use.add(machine)
            print(f"分配机器: {machine}")
            return machine

    def release(self, machine: str):
        """
        回收一台已分配的机器。

        :param machine: 要回收的机器标识
        """
        with self._lock:
            if machine in self._in_use:
                self._in_use.remove(machine)
                print(f"回收机器: {machine}")
            else:
                print(f"机器 {machine} 未被分配，无需回收")

    def available_count(self) -> int:
        """
        获取当前可用机器数量。

        :return: 可用机器数量
        """
        with self._lock:
            return len([m for m in self._machines if m not in self._in_use])

# 示例用法
if __name__ == "__main__":
    pool = MachinePool(["machine1", "machine2", "machine3"])
    m1 = pool.acquire()
    m2 = pool.acquire()
    print(f"剩余可用: {pool.available_count()}")
    pool.release(m1)
    print(f"剩余可用: {pool.available_count()}")
