import requests
from typing import Dict, Any, Optional

class APISDK:
    """
    API SDK 示例类，用于封装常用的 HTTP 接口调用方法。
    """

    def __init__(self, base_url: str, token: Optional[str] = None):
        """
        初始化 API SDK。

        :param base_url: API 基础地址
        :param token: 可选的认证 Token
        """
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """
        构造请求头。

        :param extra: 额外的请求头字典
        :return: 完整请求头
        """
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if extra:
            headers.update(extra)
        return headers

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        发送 GET 请求。

        :param path: API 路径（如 /users）
        :param params: 查询参数
        :param headers: 额外请求头
        :return: requests.Response 对象
        """
        url = f"{self.base_url}{path}"
        return requests.get(url, params=params, headers=self._headers(headers))

    def post(self, path: str, data: Any = None, json: Any = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        发送 POST 请求。

        :param path: API 路径
        :param data: 表单数据
        :param json: JSON 数据
        :param headers: 额外请求头
        :return: requests.Response 对象
        """
        url = f"{self.base_url}{path}"
        return requests.post(url, data=data, json=json, headers=self._headers(headers))

    def put(self, path: str, data: Any = None, json: Any = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        发送 PUT 请求。

        :param path: API 路径
        :param data: 表单数据
        :param json: JSON 数据
        :param headers: 额外请求头
        :return: requests.Response 对象
        """
        url = f"{self.base_url}{path}"
        return requests.put(url, data=data, json=json, headers=self._headers(headers))

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        发送 DELETE 请求。

        :param path: API 路径
        :param headers: 额外请求头
        :return: requests.Response 对象
        """
        url = f"{self.base_url}{path}"
        return requests.delete(url, headers=self._headers(headers))

# 示例用法
if __name__ == "__main__":
    sdk = APISDK(base_url="https://httpbin.org")
    resp = sdk.get("/get", params={"foo": "bar"})
    print("GET 响应：", resp.json())
    resp = sdk.post("/post", json={"name": "Alice"})
    print("POST 响应：", resp.json())
