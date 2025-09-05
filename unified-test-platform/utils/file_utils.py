"""
文件操作工具函数模块，提供常用的文件读写、复制、删除等辅助方法。
"""

import os
import shutil
from typing import List

def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    读取文本文件内容。

    :param file_path: 文件路径
    :param encoding: 文件编码，默认 utf-8
    :return: 文件内容字符串
    """
    with open(file_path, "r", encoding=encoding) as f:
        return f.read()

def write_file(file_path: str, content: str, encoding: str = "utf-8") -> None:
    """
    写入文本内容到文件。

    :param file_path: 文件路径
    :param content: 要写入的内容
    :param encoding: 文件编码，默认 utf-8
    """
    with open(file_path, "w", encoding=encoding) as f:
        f.write(content)

def copy_file(src: str, dst: str) -> None:
    """
    复制文件到目标路径。

    :param src: 源文件路径
    :param dst: 目标文件路径
    """
    shutil.copy2(src, dst)

def remove_file(file_path: str) -> None:
    """
    删除指定文件。

    :param file_path: 文件路径
    """
    if os.path.isfile(file_path):
        os.remove(file_path)

def list_files(directory: str, ext: str = None) -> List[str]:
    """
    列出目录下所有文件，可按扩展名过滤。

    :param directory: 目录路径
    :param ext: 指定扩展名（如 ".txt"），不指定则返回所有文件
    :return: 文件路径列表
    """
    files = []
    for fname in os.listdir(directory):
        full_path = os.path.join(directory, fname)
        if os.path.isfile(full_path):
            if ext is None or fname.lower().endswith(ext.lower()):
                files.append(full_path)
    return files

# 示例用法
if __name__ == "__main__":
    write_file("demo.txt", "Hello, file utils!")
    print("文件内容：", read_file("demo.txt"))
    copy_file("demo.txt", "demo_copy.txt")
    print("复制后内容：", read_file("demo_copy.txt"))
    print("当前目录下所有txt文件：", list_files(".", ".txt"))
    remove_file("demo.txt")
    remove_file("demo_copy.txt")
