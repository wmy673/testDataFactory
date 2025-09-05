import subprocess
import requests
from typing import List, Dict

def run_sonar_scanner(project_dir: str, sonar_scanner_path: str = "sonar-scanner") -> int:
    """
    调用 SonarQube Scanner 对指定项目目录进行代码质量分析。

    :param project_dir: 需要分析的项目目录
    :param sonar_scanner_path: sonar-scanner 命令路径（默认已加入环境变量）
    :return: SonarQube Scanner 进程的返回码
    """
    cmd = [sonar_scanner_path, f"-Dsonar.projectBaseDir={project_dir}"]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=project_dir)
        print("SonarQube Scanner 执行输出：", result.stdout)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print("SonarQube Scanner 执行失败：", e.stderr)
        return e.returncode

def get_sonar_issues(sonar_url: str, project_key: str, token: str) -> List[Dict]:
    """
    通过 SonarQube Web API 获取指定项目的代码问题列表。

    :param sonar_url: SonarQube 服务器地址（如 http://localhost:9000）
    :param project_key: 项目在 SonarQube 中的唯一标识
    :param token: 用于认证的 SonarQube Token
    :return: 问题列表，每项为字典
    """
    api_url = f"{sonar_url}/api/issues/search"
    headers = {"Authorization": f"Basic {token}:".encode("ascii").decode("ascii")}
    params = {"componentKeys": project_key, "ps": 500}
    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        issues = response.json().get("issues", [])
        return issues
    except Exception as e:
        print(f"获取 SonarQube 问题失败: {e}")
        return []

# 示例用法
if __name__ == "__main__":
    # 运行 SonarQube 扫描
    run_sonar_scanner(project_dir=".")
    # 获取分析结果（需替换为实际参数）
    issues = get_sonar_issues(
        sonar_url="http://localhost:9000",
        project_key="your_project_key",
        token="your_sonarqube_token"
    )
    print("发现的问题：")
    for issue in issues:
        print(issue)
