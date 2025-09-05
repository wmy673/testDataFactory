import xml.etree.ElementTree as ET
from typing import Any, Dict, Optional, List

def read_xml(file_path: str, encoding: str = "utf-8") -> ET.ElementTree:
    """
    读取 XML 文件并返回 ElementTree 对象。

    :param file_path: XML 文件路径
    :param encoding: 文件编码，默认 utf-8
    :return: ElementTree 对象
    """
    tree = ET.parse(file_path)
    return tree

def write_xml(file_path: str, root: ET.Element, encoding: str = "utf-8") -> None:
    """
    将 ElementTree 的根节点写入 XML 文件。

    :param file_path: XML 文件路径
    :param root: 根节点 Element
    :param encoding: 文件编码，默认 utf-8
    """
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding=encoding, xml_declaration=True)

def find_element(tree: ET.ElementTree, path: str) -> Optional[ET.Element]:
    """
    根据 XPath 查找第一个匹配的元素。

    :param tree: ElementTree 对象
    :param path: XPath 路径
    :return: 匹配的 Element 或 None
    """
    return tree.find(path)

def find_elements(tree: ET.ElementTree, path: str) -> List[ET.Element]:
    """
    根据 XPath 查找所有匹配的元素。

    :param tree: ElementTree 对象
    :param path: XPath 路径
    :return: 匹配的 Element 列表
    """
    return tree.findall(path)

def element_to_dict(element: ET.Element) -> Dict[str, Any]:
    """
    将 Element 节点及其子节点转换为字典。

    :param element: Element 节点
    :return: 字典表示
    """
    def _to_dict(elem):
        d = {**elem.attrib}
        # 如果有子节点
        children = list(elem)
        if children:
            for child in children:
                d[child.tag] = _to_dict(child)
        else:
            d["text"] = elem.text
        return d
    return {element.tag: _to_dict(element)}

# 示例用法
if __name__ == "__main__":
    # 假设有一个 test.xml 文件
    root = ET.Element("root")
    child = ET.SubElement(root, "child", attrib={"name": "foo"})
    child.text = "bar"
    write_xml("test.xml", root)
    tree = read_xml("test.xml")
    elem = find_element(tree, "./child")
    print("查找到的元素：", elem.tag, elem.attrib, elem.text)
    print("转为字典：", element_to_dict(elem))
