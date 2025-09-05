from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_remote_driver(
    grid_url: str = "http://localhost:4444/wd/hub",
    browser: str = "chrome",
    options=None
):
    """
    获取 Selenium Grid 远程 WebDriver 实例。

    :param grid_url: Selenium Grid Hub 地址
    :param browser: 浏览器类型（如 "chrome"、"firefox"）
    :param options: 浏览器启动参数（可选）
    :return: 远程 WebDriver 实例
    """
    if browser.lower() == "chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
    elif browser.lower() == "firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
    else:
        raise ValueError("暂不支持的浏览器类型: " + browser)
    return webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities, options=options)

# 示例用法
if __name__ == "__main__":
    # 启动远程 Chrome 浏览器
    driver = get_remote_driver(grid_url="http://localhost:4444/wd/hub", browser="chrome")
    driver.get("https://www.example.com")
    print("页面标题:", driver.title)
    driver.quit()
