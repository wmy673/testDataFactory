from typing import Any, Dict

class ATCInterface:
    """
    ATC（自动化测试用例）接口示例类。
    用于定义自动化测试用例的标准接口，便于统一管理和调用。
    """

    def setup(self, context: Dict[str, Any]) -> None:
        """
        用例前置步骤（如环境准备、数据初始化等）。

        :param context: 测试上下文信息字典
        """
        pass

    def run(self, context: Dict[str, Any]) -> Any:
        """
        用例执行步骤。

        :param context: 测试上下文信息字典
        :return: 用例执行结果
        """
        pass

    def teardown(self, context: Dict[str, Any]) -> None:
        """
        用例后置步骤（如资源清理、数据恢复等）。

        :param context: 测试上下文信息字典
        """
        pass

# 示例用法
if __name__ == "__main__":
    class DemoATC(ATCInterface):
        def setup(self, context):
            print("环境准备")
        def run(self, context):
            print("执行测试用例")
            return "success"
        def teardown(self, context):
            print("清理环境")

    context = {}
    atc = DemoATC()
    atc.setup(context)
    result = atc.run(context)
    print("用例结果：", result)
    atc.teardown(context)
