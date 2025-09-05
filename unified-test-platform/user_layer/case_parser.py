from typing import List, Dict, Any
import yaml
import json
import os

class CaseParser:
    """
    用例解析器，用于解析 YAML/JSON 格式的自动化测试用例文件。
    支持将用例文件内容解析为统一的用例字典列表，便于后续执行和管理。
    """

    def __init__(self, file_path: str):
        """
        初始化用例解析器。

        :param file_path: 用例文件路径（支持 .yaml/.yml/.json）
        """
        self.file_path = file_path

    def parse(self) -> List[Dict[str, Any]]:
        """
        解析用例文件，返回用例字典列表。

        :return: 用例字典列表
        :raises ValueError: 文件格式不支持或解析失败
        """
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"用例文件不存在: {self.file_path}")
        ext = os.path.splitext(self.file_path)[1].lower()
        with open(self.file_path, "r", encoding="utf-8") as f:
            if ext in [".yaml", ".yml"]:
                try:
                    cases = yaml.safe_load(f)
                except Exception as e:
                    raise ValueError(f"YAML 解析失败: {e}")
            elif ext == ".json":
                try:
                    cases = json.load(f)
                except Exception as e:
                    raise ValueError(f"JSON 解析失败: {e}")
            else:
                raise ValueError("不支持的用例文件格式，仅支持 .yaml/.yml/.json")
        # 保证返回列表
        if isinstance(cases, dict):
            return [cases]
        elif isinstance(cases, list):
            return cases
        else:
            raise ValueError("用例文件内容格式错误，需为列表或字典")

# 示例用法
if __name__ == "__main__":
    # 假设有一个 case.yaml 或 case.json 文件
    parser = CaseParser("case.yaml")
    try:
        cases = parser.parse()
        print("解析到的用例：", cases)
    except Exception as e:
        print("用例解析失败：", e)
