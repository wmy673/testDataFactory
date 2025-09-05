from appium import webdriver

def get_ios_driver(
    bundle_id: str,
    device_name: str = "iPhone Simulator",
    platform_version: str = "14.0",
    server_url: str = "http://localhost:4723/wd/hub",
    udid: str = None,
    no_reset: bool = True,
    automation_name: str = "XCUITest"
):
    """
    获取 iOS Appium WebDriver 实例。

    :param bundle_id: 应用的 bundle id
    :param device_name: 设备名称（默认 iPhone Simulator）
    :param platform_version: iOS 版本号
    :param server_url: Appium Server 地址
    :param udid: 设备唯一标识（真机必填）
    :param no_reset: 是否保留应用数据
    :param automation_name: 自动化引擎（默认 XCUITest）
    :return: Appium WebDriver 实例
    """
    desired_caps = {
        "platformName": "iOS",
        "platformVersion": platform_version,
        "deviceName": device_name,
        "bundleId": bundle_id,
        "noReset": no_reset,
        "automationName": automation_name
    }
    if udid:
        desired_caps["udid"] = udid
    driver = webdriver.Remote(server_url, desired_caps)
    return driver

# 示例用法
if __name__ == "__main__":
    # 请根据实际情况填写 bundle_id
    driver = get_ios_driver(
        bundle_id="com.example.demo"
    )
    print("当前 bundleId:", driver.capabilities.get("bundleId"))
    driver.quit()
