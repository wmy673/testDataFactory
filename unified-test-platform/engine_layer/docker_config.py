import docker

def get_docker_client(base_url: str = "unix://var/run/docker.sock") -> docker.DockerClient:
    """
    获取 Docker 客户端对象。

    :param base_url: Docker 守护进程的连接地址（Windows 下可用 'npipe:////./pipe/docker_engine'）
    :return: DockerClient 实例
    """
    return docker.DockerClient(base_url=base_url)

def create_container(
    client: docker.DockerClient,
    image: str,
    name: str = None,
    command: str = None,
    ports: dict = None,
    volumes: dict = None,
    environment: dict = None,
    detach: bool = True
):
    """
    创建并启动一个 Docker 容器。

    :param client: DockerClient 实例
    :param image: 镜像名称
    :param name: 容器名称
    :param command: 容器启动命令
    :param ports: 端口映射，如 {"8080/tcp": 8080}
    :param volumes: 卷映射，如 {"/host/path": {"bind": "/container/path", "mode": "rw"}}
    :param environment: 环境变量字典
    :param detach: 是否以分离模式启动
    :return: 容器对象
    """
    container = client.containers.run(
        image=image,
        name=name,
        command=command,
        ports=ports,
        volumes=volumes,
        environment=environment,
        detach=detach
    )
    return container

def remove_container(client: docker.DockerClient, container_name: str, force: bool = True):
    """
    停止并删除指定名称的容器。

    :param client: DockerClient 实例
    :param container_name: 容器名称
    :param force: 是否强制删除
    """
    try:
        container = client.containers.get(container_name)
        container.remove(force=force)
        print(f"容器 {container_name} 已删除")
    except Exception as e:
        print(f"删除容器 {container_name} 失败: {e}")

# 示例用法
if __name__ == "__main__":
    # Windows 下建议 base_url="npipe:////./pipe/docker_engine"
    client = get_docker_client()
    # 拉取镜像并启动容器
    container = create_container(
        client,
        image="hello-world",
        name="test_hello",
        detach=True
    )
    print(f"已启动容器: {container.name}")
    # 删除容器
    remove_container(client, "test_hello")
