import subprocess
from typing import List

def run_findbugs(jar_path: str, output_xml: str, findbugs_home: str = "C:\\FindBugs") -> int:
    """
    调用 FindBugs 工具对指定的 jar 包进行静态分析，并生成 XML 格式的报告。

    :param jar_path: 需要分析的 jar 文件路径
    :param output_xml: 分析结果输出的 XML 文件路径
    :param findbugs_home: FindBugs 安装目录（默认 C:\\FindBugs）
    :return: FindBugs 进程的返回码
    """
    findbugs_cmd = [
        f"{findbugs_home}\\bin\\findbugs.bat",
        "-textui",
        "-xml",
        "-output", output_xml,
        jar_path
    ]
    try:
        result = subprocess.run(findbugs_cmd, check=True, capture_output=True, text=True)
        print("FindBugs 执行输出：", result.stdout)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print("FindBugs 执行失败：", e.stderr)
        return e.returncode

def parse_findbugs_xml(xml_path: str) -> List[dict]:
    """
    解析 FindBugs 生成的 XML 报告，提取缺陷信息。

    :param xml_path: FindBugs XML 报告路径
    :return: 缺陷信息列表，每个元素为字典
    """
    import xml.etree.ElementTree as ET
    bugs = []
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for bug_instance in root.findall(".//BugInstance"):
            bug = {
                "type": bug_instance.get("type"),
                "priority": bug_instance.get("priority"),
                "category": bug_instance.get("category"),
                "message": bug_instance.findtext("LongMessage"),
                "class": bug_instance.find(".//Class").get("classname") if bug_instance.find(".//Class") is not None else None,
                "method": bug_instance.find(".//Method").get("name") if bug_instance.find(".//Method") is not None else None,
            }
            bugs.append(bug)
    except Exception as e:
        print(f"解析 FindBugs XML 报告失败: {e}")
    return bugs

# 示例用法
if __name__ == "__main__":
    jar_file = "example.jar"
    xml_report = "findbugs_report.xml"
    # 运行 FindBugs 分析
    run_findbugs(jar_file, xml_report)
    # 解析分析结果
    bug_list = parse_findbugs_xml(xml_report)
    print("发现的缺陷：")
    for bug in bug_list:
        print(bug)
