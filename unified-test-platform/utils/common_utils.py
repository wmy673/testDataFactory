"""
通用工具函数模块，包含常用的字符串、时间、文件等辅助方法。
"""

import os
import time
import random
import string
from typing import Any, Dict, List, Optional

def random_string(length: int = 8) -> str:
    """
    生成指定长度的随机字符串（包含大小写字母和数字）。

    :param length: 字符串长度
    :return: 随机字符串
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def timestamp(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    获取当前时间的格式化字符串。

    :param fmt: 时间格式
    :return: 格式化时间字符串
    """
    return time.strftime(fmt, time.localtime())

def ensure_dir(path: str) -> None:
    """
    确保目录存在，不存在则自动创建。

    :param path: 目录路径
    """
    if not os.path.exists(path):
        os.makedirs(path)

def file_size(file_path: str) -> int:
    """
    获取文件大小（字节）。

    :param file_path: 文件路径
    :return: 文件大小（字节）
    """
    return os.path.getsize(file_path) if os.path.isfile(file_path) else 0

def dict_to_str(d: Dict, sep: str = ", ") -> str:
    """
    将字典转换为字符串，格式为 key1=value1, key2=value2。

    :param d: 字典对象
    :param sep: 分隔符
    :return: 字符串
    """
    return sep.join(f"{k}={v}" for k, v in d.items())

def str_to_bool(s: str) -> bool:
    """
    将字符串转换为布尔值。

    :param s: 字符串
    :return: 布尔值
    """
    return str(s).strip().lower() in ("1", "true", "yes", "on")

# 示例用法
if __name__ == "__main__":
    print("随机字符串:", random_string(12))
    print("当前时间:", timestamp())
    ensure_dir("test_dir")
    print("test_dir 是否存在:", os.path.isdir("test_dir"))
    print("字符串转布尔:", str_to_bool("Yes"))
    print("字典转字符串:", dict_to_str({"a": 1, "b": 2})) 
