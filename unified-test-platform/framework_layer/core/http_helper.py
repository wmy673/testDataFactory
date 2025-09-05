import requests
from typing import Dict, Any, Optional

def http_get(url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> requests.Response:
    """
    发送 HTTP GET 请求。

    :param url: 请求地址
    :param params: 查询参数字典
    :param headers: 请求头字典
    :param timeout: 超时时间（秒）
    :return: requests.Response 对象
    """
    response = requests.get(url, params=params, headers=headers, timeout=timeout)
    return response

def http_post(url: str, data: Any = None, json: Any = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> requests.Response:
    """
    发送 HTTP POST 请求。

    :param url: 请求地址
    :param data: 表单数据
    :param json: JSON 数据
    :param headers: 请求头字典
    :param timeout: 超时时间（秒）
    :return: requests.Response 对象
    """
    response = requests.post(url, data=data, json=json, headers=headers, timeout=timeout)
    return response

def http_put(url: str, data: Any = None, json: Any = None, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> requests.Response:
    """
    发送 HTTP PUT 请求。

    :param url: 请求地址
    :param data: 表单数据
    :param json: JSON 数据
    :param headers: 请求头字典
    :param timeout: 超时时间（秒）
    :return: requests.Response 对象
    """
    response = requests.put(url, data=data, json=json, headers=headers, timeout=timeout)
    return response

def http_delete(url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 10) -> requests.Response:
    """
    发送 HTTP DELETE 请求。

    :param url: 请求地址
    :param headers: 请求头字典
    :param timeout: 超时时间（秒）
    :return: requests.Response 对象
    """
    response = requests.delete(url, headers=headers, timeout=timeout)
    return response

# 示例用法
if __name__ == "__main__":
    # GET 请求示例
    resp = http_get("https://httpbin.org/get", params={"a": 1})
    print("GET 响应:", resp.json())

    # POST 请求示例
    resp = http_post("https://httpbin.org/post", json={"foo": "bar"})
    print("POST 响应:", resp.json())
