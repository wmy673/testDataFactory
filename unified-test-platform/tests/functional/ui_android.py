from appium import webdriver

def get_android_driver(
    app_package: str,
    app_activity: str,
    device_name: str = "Android Emulator",
    platform_version: str = "10",
    server_url: str = "http://localhost:4723/wd/hub",
    no_reset: bool = True,
    automation_name: str = "UiAutomator2"
):
    """
    获取 Android Appium WebDriver 实例。

    :param app_package: 应用包名
    :param app_activity: 启动 Activity
    :param device_name: 设备名称（默认 Android Emulator）
    :param platform_version: Android 版本号
    :param server_url: Appium Server 地址
    :param no_reset: 是否保留应用数据
    :param automation_name: 自动化引擎
    :return: Appium WebDriver 实例
    """
    desired_caps = {
        "platformName": "Android",
        "platformVersion": platform_version,
        "deviceName": device_name,
        "appPackage": app_package,
        "appActivity": app_activity,
        "noReset": no_reset,
        "automationName": automation_name
    }
    driver = webdriver.Remote(server_url, desired_caps)
    return driver

# 示例用法
if __name__ == "__main__":
    # 请根据实际情况填写包名和启动 Activity
    driver = get_android_driver(
        app_package="com.example.demo",
        app_activity=".MainActivity"
    )
    print("当前 Activity:", driver.current_activity)
    driver.quit() 
