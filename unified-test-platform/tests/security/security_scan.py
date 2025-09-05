import os
import re
from typing import List, Dict

def scan_python_file_for_secrets(file_path: str) -> List[Dict]:
    """
    扫描单个 Python 文件，查找可能的敏感信息（如密码、密钥等）。

    :param file_path: 要扫描的 Python 文件路径
    :return: 发现的敏感信息列表，每项为字典
    """
    secrets = []
    # 常见敏感变量名正则
    patterns = [
        re.compile(r'(password|passwd|pwd|secret|token|key)\s*=\s*[\'"].+[\'"]', re.IGNORECASE),
        re.compile(r'(AKIA|ASIA)[A-Z0-9]{16,}', re.IGNORECASE),  # AWS Access Key
        re.compile(r'AIza[0-9A-Za-z\-_]{35}', re.IGNORECASE),    # Google API Key
    ]
    with open(file_path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            for pat in patterns:
                if pat.search(line):
                    secrets.append({
                        "file": file_path,
                        "line": lineno,
                        "content": line.strip()
                    })
    return secrets

def scan_directory_for_secrets(directory: str) -> List[Dict]:
    """
    扫描指定目录下所有 Python 文件，查找敏感信息。

    :param directory: 目录路径
    :return: 敏感信息列表
    """
    results = []
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith(".py"):
                file_path = os.path.join(root, fname)
                results.extend(scan_python_file_for_secrets(file_path))
    return results

# 示例用法
if __name__ == "__main__":
    # 扫描当前目录下所有 Python 文件
    scan_dir = os.path.dirname(__file__)
    findings = scan_directory_for_secrets(scan_dir)
    if findings:
        print("发现敏感信息：")
        for item in findings:
            print(f"{item['file']}:{item['line']} -> {item['content']}")
    else:
        print("未发现敏感信息。")
