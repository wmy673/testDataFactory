@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo.
echo ========================================
echo   统一自动化测试平台框架生成工具
echo ========================================
echo.

REM 设置项目根目录
set "ROOT_DIR=unified-test-platform"
echo 正在创建项目目录结构...

REM 创建主目录
if not exist "%ROOT_DIR%" mkdir "%ROOT_DIR%"
cd "%ROOT_DIR%"

REM 创建配置文件目录
mkdir config
echo # 统一自动化测试平台配置文件 > config\config.yaml
echo # 日志配置文件 > config\logging.conf

REM 创建用户层目录和文件
mkdir user_layer
mkdir user_layer\test_cases
mkdir user_layer\test_cases\xml_cases
mkdir user_layer\test_cases\code_cases
mkdir user_layer\test_cases\bdd_cases
mkdir user_layer\test_cases\flowchart_cases
echo. > user_layer\upload_handler.py
echo. > user_layer\case_parser.py
echo. > user_layer\atc_interface.py

REM 创建框架层目录和文件
mkdir framework_layer
mkdir framework_layer\core
mkdir framework_layer\static

REM 框架层核心文件
echo. > framework_layer\core\ui_map_tree.py
echo. > framework_layer\core\po_factory.py
echo. > framework_layer\core\fun_helper.py
echo. > framework_layer\core\log.py
echo. > framework_layer\core\pci_generator.py
echo. > framework_layer\core\http_helper.py
echo. > framework_layer\core\config_file.py
echo. > framework_layer\core\io_helper.py
echo. > framework_layer\core\db_helper.py

REM 框架层静态文件
echo. > framework_layer\static\http_helper.py
echo. > framework_layer\static\xml_helper.py
echo. > framework_layer\static\db_helper.py
echo. > framework_layer\static\config_file.py
echo. > framework_layer\static\io_helper.py

REM 创建引擎层目录和文件
mkdir engine_layer
echo. > engine_layer\jenkins_scheduler.py
echo. > engine_layer\testng_listener.py
echo. > engine_layer\selenium_grid.py
echo. > engine_layer\machine_pool.py
echo. > engine_layer\docker_config.py
echo. > engine_layer\perf_agent.py
echo. > engine_layer\job_queue.py
echo. > engine_layer\heartbeat_monitor.py
echo. > engine_layer\mock_server.py

REM 创建辅助层目录和文件
mkdir auxiliary_layer
echo. > auxiliary_layer\performance_monitor.py
echo. > auxiliary_layer\dynamic_scanner.py
echo. > auxiliary_layer\defect_density.py
echo. > auxiliary_layer\sonar_integration.py
echo. > auxiliary_layer\findbugs_integration.py
echo. > auxiliary_layer\code_coverage.py

REM 创建测试类型目录和文件
mkdir tests
mkdir tests\functional
mkdir tests\performance
mkdir tests\security
mkdir tests\unit

echo. > tests\functional\ui_android.py
echo. > tests\functional\ui_ios.py
echo. > tests\functional\api_sdk.py
echo. > tests\performance\client_perf.py
echo. > tests\performance\api_perf.py
echo. > tests\security\security_scan.py
echo. > tests\unit\unit_test.py

REM 创建报告目录和文件
mkdir reports
mkdir reports\templates
echo. > reports\report_generator.py

REM 创建工具类目录和文件
mkdir utils
echo. > utils\common_utils.py
echo. > utils\file_utils.py

REM 创建主文件和需求文件
echo # 统一自动化测试平台主入口 > main.py
echo # 项目依赖文件 > requirements.txt

REM 创建README文件
echo # 统一自动化测试平台 > README.md
echo. >> README.md
echo 基于架构图生成的自动化测试框架 >> README.md
echo. >> README.md
echo ## 功能特性 >> README.md
echo - 多格式测试用例支持(XML/Code/BDD/Flowchart) >> README.md
echo - 跨平台测试执行(Android/iOS/API/Web) >> README.md
echo - 分布式测试执行 >> README.md
echo - 自动化报告生成 >> README.md
echo - 持续集成集成 >> README.md
echo. >> README.md
echo ## 快速开始 >> README.md
echo 1. 安装依赖: pip install -r requirements.txt >> README.md
echo 2. 配置环境: 修改config/config.yaml >> README.md
echo 3. 运行平台: python main.py >> README.md

REM 创建初始化配置文件
(
echo # 统一自动化测试平台配置
echo.
echo appium:
echo   url: http://localhost:4723/wd/hub
echo.
echo jenkins:
echo   url: http://jenkins.example.com:8080
echo   username: admin
echo   password: password
echo.
echo selenium_grid:
echo   hub_url: http://selenium-hub.example.com:4444/wd/hub
echo.
echo database:
echo   test_results:
echo     host: localhost
echo     port: 5432
echo     database: test_results
echo     username: tester
echo     password: password
echo.
echo logging:
echo   level: INFO
echo   file: logs/platform.log
echo.
echo report:
echo   output_dir: reports/
echo   formats: [html, json]
) > config\config.yaml

REM 创建基础需求文件
(
echo requests==2.28.1
echo selenium==4.7.2
echo appium-python-client==2.1.0
echo jinja2==3.1.2
echo pyyaml==6.0
echo pytest==7.2.0
echo pytest-html==3.2.0
echo allure-pytest==2.9.45
echo paramiko==2.12.0
echo docker==6.0.1
echo jenkinsapi==0.3.13
) > requirements.txt

REM 创建主程序入口
(
echo #!/usr/bin/env python3
echo """
echo 统一自动化测试平台主入口
echo """
echo import logging
echo from config import load_config
echo from user_layer.atc_interface import ATCInterface
echo from engine_layer.jenkins_scheduler import JenkinsScheduler
echo from reports.report_generator import ReportGenerator
echo.
echo def setup_logging():
echo     """配置日志系统"""
echo     logging.config.fileConfig('config/logging.conf')
echo     return logging.getLogger(__name__)
echo.
echo def main():
echo     """主函数"""
echo     logger = setup_logging()
echo     logger.info("启动统一自动化测试平台")
echo     
echo     # 加载配置
echo     config = load_config('config/config.yaml')
echo     
echo     # 初始化ATC界面
echo     atc_interface = ATCInterface(config)
echo     
echo     # 初始化Jenkins调度器
echo     jenkins_scheduler = JenkinsScheduler(config)
echo     
echo     # 初始化报告生成器
echo     report_generator = ReportGenerator(config)
echo     
echo     # 启动平台
echo     try:
echo         atc_interface.start()
echo     except KeyboardInterrupt:
echo         logger.info("接收到中断信号，正在关闭平台...")
echo     finally:
echo         logger.info("统一自动化测试平台已关闭")
echo.
echo if __name__ == "__main__":
echo     main()
) > main.py

echo.
echo 项目框架已创建完成!
echo 目录: %CD%
echo.
echo 下一步操作:
echo 1. 安装依赖: pip install -r requirements.txt
echo 2. 根据需要修改配置文件: config\config.yaml
echo 3. 开始开发各个模块的功能
echo.
pause