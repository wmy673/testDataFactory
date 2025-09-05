import configparser
from typing import Dict

class ConfigFile:
    """
    配置文件读取工具类，支持读取 INI 格式的配置文件。
    """

    def __init__(self, file_path: str):
        """
        初始化配置文件对象。

        :param file_path: 配置文件路径
        """
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(file_path, encoding="utf-8")

    def get(self, section: str, option: str, fallback=None) -> str:
        """
        获取指定 section 下的 option 配置值。

        :param section: 配置节名称
        :param option: 配置项名称
        :param fallback: 获取失败时的默认值
        :return: 配置值字符串
        """
        return self.config.get(section, option, fallback=fallback)

    def get_section(self, section: str) -> Dict[str, str]:
        """
        获取指定 section 下所有配置项（字典形式）。

        :param section: 配置节名称
        :return: 配置项字典
        """
        if section in self.config:
            return dict(self.config[section])
        else:
            return {}

# 示例用法
if __name__ == "__main__":
    # 假设有一个 config.ini 文件
    cfg = ConfigFile("config.ini")
    db_host = cfg.get("database", "host", fallback="localhost")
    print("数据库主机:", db_host)
    print("database 配置:", cfg.get_section("database"))
