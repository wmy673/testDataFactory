import jenkins

class JenkinsScheduler:
    """
    Jenkins 调度器，用于触发 Jenkins 任务并监控其执行状态。
    """

    def __init__(self, url: str, username: str, password: str):
        """
        初始化 Jenkins 调度器。

        :param url: Jenkins 服务器地址
        :param username: Jenkins 用户名
        :param password: Jenkins 用户密码或 API Token
        """
        self.server = jenkins.Jenkins(url, username=username, password=password)

    def trigger_job(self, job_name: str, parameters: dict = None) -> int:
        """
        触发 Jenkins 任务。

        :param job_name: Jenkins 任务名称
        :param parameters: 任务参数（可选）
        :return: 本次构建的编号
        """
        if parameters:
            queue_number = self.server.build_job(job_name, parameters)
        else:
            queue_number = self.server.build_job(job_name)
        print(f"已触发 Jenkins 任务：{job_name}，队列号：{queue_number}")
        # 获取构建编号
        build_number = self._wait_for_build_number(job_name, queue_number)
        print(f"任务 {job_name} 的构建编号为：{build_number}")
        return build_number

    def _wait_for_build_number(self, job_name: str, queue_number: int, timeout: int = 60) -> int:
        """
        等待 Jenkins 队列任务分配到构建编号。

        :param job_name: Jenkins 任务名称
        :param queue_number: 队列号
        :param timeout: 超时时间（秒）
        :return: 构建编号
        """
        import time
        start = time.time()
        while time.time() - start < timeout:
            try:
                item = self.server.get_queue_item(queue_number)
                if 'executable' in item and 'number' in item['executable']:
                    return item['executable']['number']
            except Exception:
                pass
            time.sleep(2)
        raise TimeoutError("等待 Jenkins 分配构建编号超时")

    def get_build_info(self, job_name: str, build_number: int) -> dict:
        """
        获取 Jenkins 构建信息。

        :param job_name: Jenkins 任务名称
        :param build_number: 构建编号
        :return: 构建信息字典
        """
        info = self.server.get_build_info(job_name, build_number)
        return info

    def wait_for_build_complete(self, job_name: str, build_number: int, timeout: int = 600) -> dict:
        """
        等待 Jenkins 构建完成并返回结果。

        :param job_name: Jenkins 任务名称
        :param build_number: 构建编号
        :param timeout: 超时时间（秒）
        :return: 构建信息字典
        """
        import time
        start = time.time()
        while time.time() - start < timeout:
            info = self.get_build_info(job_name, build_number)
            if not info.get('building', False):
                print(f"任务 {job_name} 构建完成，结果：{info.get('result')}")
                return info
            time.sleep(5)
        raise TimeoutError("等待 Jenkins 构建完成超时")


if __name__ == "__main__":
    
    jenkins_url = "http://localhost:8080"
    username = "admin"
    password = "your_api_token"
    job_name = "example-job"

    scheduler = JenkinsScheduler(jenkins_url, username, password)
    build_number = scheduler.trigger_job(job_name)
    build_info = scheduler.wait_for_build_complete(job_name, build_number)
    print("构建信息：", build_info)
