import os
from typing import List

def read_text_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    读取文本文件内容。

    :param file_path: 文件路径
    :param encoding: 文件编码，默认 utf-8
    :return: 文件内容字符串
    """
    with open(file_path, "r", encoding=encoding) as f:
        return f.read()

def write_text_file(file_path: str, content: str, encoding: str = "utf-8") -> None:
    """
    写入文本内容到文件。

    :param file_path: 文件路径
    :param content: 要写入的内容
    :param encoding: 文件编码，默认 utf-8
    """
    with open(file_path, "w", encoding=encoding) as f:
        f.write(content)

def read_lines(file_path: str, encoding: str = "utf-8") -> List[str]:
    """
    按行读取文本文件内容。

    :param file_path: 文件路径
    :param encoding: 文件编码，默认 utf-8
    :return: 行内容列表
    """
    with open(file_path, "r", encoding=encoding) as f:
        return f.readlines()

def write_lines(file_path: str, lines: List[str], encoding: str = "utf-8") -> None:
    """
    按行写入内容到文本文件。

    :param file_path: 文件路径
    :param lines: 行内容列表
    :param encoding: 文件编码，默认 utf-8
    """
    with open(file_path, "w", encoding=encoding) as f:
        f.writelines(lines)

def file_exists(file_path: str) -> bool:
    """
    判断文件是否存在。

    :param file_path: 文件路径
    :return: 是否存在
    """
    return os.path.isfile(file_path)

def remove_file(file_path: str) -> None:
    """
    删除指定文件。

    :param file_path: 文件路径
    """
    if os.path.isfile(file_path):
        os.remove(file_path)

# 示例用法
if __name__ == "__main__":
    test_path = "test.txt"
    write_text_file(test_path, "Hello, world!\n第二行")
    print("文件内容：", read_text_file(test_path))
    print("文件是否存在：", file_exists(test_path))
    lines = read_lines(test_path)
    print("按行读取：", lines)
    write_lines(test_path, ["新的一行\n", "再来一行\n"])
    print("修改后内容：", read_text_file(test_path))
    remove_file(test_path)
    print("删除后是否存在：", file_exists(test_path))
