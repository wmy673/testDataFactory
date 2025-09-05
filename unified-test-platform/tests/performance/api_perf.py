import time
import requests

def measure_api_performance(
    url: str,
    method: str = "GET",
    params: dict = None,
    data: dict = None,
    json: dict = None,
    headers: dict = None,
    repeat: int = 10,
    timeout: int = 10
) -> dict:
    """
    测量指定 API 接口的性能（响应时间统计）。

    :param url: 接口地址
    :param method: 请求方法（GET、POST、PUT、DELETE等）
    :param params: 查询参数
    :param data: 表单数据
    :param json: JSON 数据
    :param headers: 请求头
    :param repeat: 测试次数
    :param timeout: 超时时间（秒）
    :return: 性能统计结果字典
    """
    times = []
    for i in range(repeat):
        start = time.time()
        try:
            resp = requests.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=timeout
            )
            resp.raise_for_status()
        except Exception as e:
            print(f"第{i+1}次请求失败: {e}")
            continue
        elapsed = time.time() - start
        times.append(elapsed)
        print(f"第{i+1}次响应时间: {elapsed:.3f} 秒")
    if times:
        return {
            "count": len(times),
            "min": min(times),
            "max": max(times),
            "avg": sum(times) / len(times)
        }
    else:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "avg": None
        }

# 示例用法
if __name__ == "__main__":
    url = "https://httpbin.org/get"
    result = measure_api_performance(url, method="GET", repeat=5)
    print("API 性能统计：", result)
