import importlib
import os
import sys
from typing import List, Type

def scan_and_import_modules(directory: str, base_class: type = None) -> List[Type]:
    """
    动态扫描指定目录下的所有 Python 文件并导入模块。
    如果指定了 base_class，则返回该基类的所有子类类型列表。

    :param directory: 要扫描的目录路径
    :param base_class: （可选）需要筛选的基类
    :return: 模块中所有类（或指定基类的子类）组成的列表
    """
    modules = []
    classes = []

    # 将目录添加到 sys.path，便于导入
    sys.path.insert(0, directory)

    for filename in os.listdir(directory):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(module_name)
                modules.append(module)
            except Exception as e:
                print(f"导入模块 {module_name} 时出错: {e}")

    for module in modules:
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type):
                if base_class is None or (issubclass(attr, base_class) and attr is not base_class):
                    classes.append(attr)

    # 移除 sys.path 中添加的目录
    sys.path.pop(0)
    return classes

# 示例用法
if __name__ == "__main__":
    # 假设要扫描当前目录下所有继承自 BaseClass 的类
    class BaseClass:
        pass

    found_classes = scan_and_import_modules(os.path.dirname(__file__), BaseClass)
    print("找到的类：", [cls.__name__ for cls in found_classes])
