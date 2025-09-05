class TestNGListener:
    """
    TestNG 监听器，用于在测试执行过程中监听测试用例的开始、结束、失败等事件。
    可用于自定义测试报告、日志收集等扩展功能。
    """

    def on_test_start(self, test_name: str):
        """
        测试用例开始时调用。

        :param test_name: 测试用例名称
        """
        print(f"测试开始: {test_name}")

    def on_test_success(self, test_name: str):
        """
        测试用例成功时调用。

        :param test_name: 测试用例名称
        """
        print(f"测试成功: {test_name}")

    def on_test_failure(self, test_name: str, exception: Exception):
        """
        测试用例失败时调用。

        :param test_name: 测试用例名称
        :param exception: 失败异常信息
        """
        print(f"测试失败: {test_name}，异常: {exception}")

    def on_test_finish(self, test_name: str):
        """
        测试用例结束时调用（无论成功或失败）。

        :param test_name: 测试用例名称
        """
        print(f"测试结束: {test_name}")

# 示例用法
if __name__ == "__main__":
    listener = TestNGListener()
    test_name = "test_example"
    try:
        listener.on_test_start(test_name)
        # 模拟测试逻辑
        # raise Exception("模拟失败")  # 取消注释以模拟失败
        listener.on_test_success(test_name)
    except Exception as e:
        listener.on_test_failure(test_name, e)
    finally:
        listener.on_test_finish(test_name) 
