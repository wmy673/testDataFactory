from typing import Callable, Any, Tuple, Dict

def safe_call(func: Callable, *args, **kwargs) -> Tuple[bool, Any]:
    """
    安全调用函数，捕获异常并返回执行结果。

    :param func: 要调用的函数
    :param args: 位置参数
    :param kwargs: 关键字参数
    :return: (是否成功, 返回值或异常对象)
    """
    try:
        result = func(*args, **kwargs)
        return True, result
    except Exception as e:
        return False, e

def retry(func: Callable, retries: int = 3, exceptions: Tuple = (Exception,), **kwargs) -> Any:
    """
    带重试机制的函数调用。

    :param func: 要调用的函数
    :param retries: 最大重试次数
    :param exceptions: 需要捕获重试的异常类型
    :param kwargs: 传递给函数的关键字参数
    :return: 函数返回值
    :raises Exception: 超过重试次数仍失败时抛出最后一次异常
    """
    last_exc = None
    for attempt in range(retries):
        try:
            return func(**kwargs)
        except exceptions as e:
            last_exc = e
    raise last_exc

def dict_merge(a: Dict, b: Dict) -> Dict:
    """
    合并两个字典，b 的内容会覆盖 a 的同名键。

    :param a: 字典 a
    :param b: 字典 b
    :return: 合并后的新字典
    """
    result = a.copy()
    result.update(b)
    return result

# 示例用法
if __name__ == "__main__":
    def div(x, y):
        return x / y

    # 安全调用
    ok, res = safe_call(div, 4, 2)
    print("调用成功:", ok, "结果:", res)
    ok, res = safe_call(div, 4, 0)
    print("调用成功:", ok, "结果:", res)

    # 重试机制
    def fail_once(x=[0]):
        if x[0] == 0:
            x[0] = 1
            raise ValueError("fail first")
        return "ok"
    print("重试结果:", retry(fail_once, retries=2))

    # 字典合并
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    print("合并字典:", dict_merge(d1, d2))
