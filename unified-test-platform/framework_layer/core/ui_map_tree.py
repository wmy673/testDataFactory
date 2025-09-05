from typing import Dict, Any, Optional, List

class UIMapTree:
    """
    UI 映射树，用于管理和查找页面元素的层级结构映射关系。
    支持按路径查找元素信息，适合复杂页面对象的组织与维护。
    """

    def __init__(self, tree: Optional[Dict[str, Any]] = None):
        """
        初始化 UI 映射树。

        :param tree: UI 元素映射的嵌套字典结构
        """
        self.tree = tree or {}

    def add_path(self, path: List[str], value: Any):
        """
        向映射树中添加一个元素路径及其对应的值。

        :param path: 元素路径（如 ["登录页", "用户名输入框"]）
        :param value: 元素信息（如定位方式、描述等）
        """
        node = self.tree
        for key in path[:-1]:
            if key not in node:
                node[key] = {}
            node = node[key]
        node[path[-1]] = value

    def get(self, path: List[str]) -> Optional[Any]:
        """
        根据路径查找元素信息。

        :param path: 元素路径（如 ["登录页", "用户名输入框"]）
        :return: 元素信息或 None
        """
        node = self.tree
        for key in path:
            if key not in node:
                return None
            node = node[key]
        return node

    def remove(self, path: List[str]) -> bool:
        """
        移除指定路径的元素。

        :param path: 元素路径
        :return: 是否移除成功
        """
        node = self.tree
        parents = []
        for key in path[:-1]:
            if key not in node:
                return False
            parents.append((node, key))
            node = node[key]
        if path[-1] in node:
            del node[path[-1]]
            # 清理空的父节点
            for parent, key in reversed(parents):
                if not parent[key]:
                    del parent[key]
            return True
        return False

# 示例用法
if __name__ == "__main__":
    ui_tree = UIMapTree()
    ui_tree.add_path(["登录页", "用户名输入框"], {"by": "id", "value": "username"})
    ui_tree.add_path(["登录页", "密码输入框"], {"by": "id", "value": "password"})
    print("用户名输入框信息:", ui_tree.get(["登录页", "用户名输入框"]))
    print("密码输入框信息:", ui_tree.get(["登录页", "密码输入框"]))
    ui_tree.remove(["登录页", "用户名输入框"])
    print("移除后用户名输入框:", ui_tree.get(["登录页", "用户名输入框"]))
