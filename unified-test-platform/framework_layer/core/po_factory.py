from typing import Type, Dict, Any

class POFactory:
    """
    页面对象工厂类，用于统一创建和管理页面对象（Page Object）。
    支持缓存已创建的对象，避免重复实例化。
    """

    def __init__(self):
        """
        初始化工厂，创建对象缓存字典。
        """
        self._cache: Dict[str, Any] = {}

    def get(self, po_cls: Type, *args, **kwargs) -> Any:
        """
        获取指定页面对象实例，若已存在则直接返回，否则创建新实例并缓存。

        :param po_cls: 页面对象类
        :param args: 初始化参数
        :param kwargs: 初始化关键字参数
        :return: 页面对象实例
        """
        key = po_cls.__name__
        if key not in self._cache:
            self._cache[key] = po_cls(*args, **kwargs)
        return self._cache[key]

    def clear(self):
        """
        清空所有已缓存的页面对象。
        """
        self._cache.clear()

# 示例用法
if __name__ == "__main__":
    # 示例页面对象类
    class LoginPage:
        def __init__(self, url):
            self.url = url

    factory = POFactory()
    login_page1 = factory.get(LoginPage, url="http://example.com/login")
    login_page2 = factory.get(LoginPage, url="http://example.com/login")
    print("是否同一对象:", login_page1 is login_page2)
    print("登录页URL:", login_page1.url)
    factory.clear()
