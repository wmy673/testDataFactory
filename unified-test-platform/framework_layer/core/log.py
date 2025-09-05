import logging
import os

def get_logger(name: str = "unified_test_platform", log_file: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    获取或创建一个日志记录器。

    :param name: 日志记录器名称
    :param log_file: 日志文件路径（如为 None 则只输出到控制台）
    :param level: 日志级别，默认 logging.INFO
    :return: logging.Logger 实例
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 防止重复添加 handler
    if not logger.handlers:
        # 控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 文件输出（可选）
        if log_file:
            # 自动创建日志目录
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger

# 示例用法
if __name__ == "__main__":
    logger = get_logger(log_file="logs/test.log", level=logging.DEBUG)
    logger.info("这是一条 info 日志")
    logger.debug("这是一条 debug 日志")
    logger.error("这是一条 error 日志") 
