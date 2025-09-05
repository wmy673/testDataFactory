@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo.
echo ========================================
echo   ͳһ�Զ�������ƽ̨������ɹ���
echo ========================================
echo.

REM ������Ŀ��Ŀ¼
set "ROOT_DIR=unified-test-platform"
echo ���ڴ�����ĿĿ¼�ṹ...

REM ������Ŀ¼
if not exist "%ROOT_DIR%" mkdir "%ROOT_DIR%"
cd "%ROOT_DIR%"

REM ���������ļ�Ŀ¼
mkdir config
echo # ͳһ�Զ�������ƽ̨�����ļ� > config\config.yaml
echo # ��־�����ļ� > config\logging.conf

REM �����û���Ŀ¼���ļ�
mkdir user_layer
mkdir user_layer\test_cases
mkdir user_layer\test_cases\xml_cases
mkdir user_layer\test_cases\code_cases
mkdir user_layer\test_cases\bdd_cases
mkdir user_layer\test_cases\flowchart_cases
echo. > user_layer\upload_handler.py
echo. > user_layer\case_parser.py
echo. > user_layer\atc_interface.py

REM ������ܲ�Ŀ¼���ļ�
mkdir framework_layer
mkdir framework_layer\core
mkdir framework_layer\static

REM ��ܲ�����ļ�
echo. > framework_layer\core\ui_map_tree.py
echo. > framework_layer\core\po_factory.py
echo. > framework_layer\core\fun_helper.py
echo. > framework_layer\core\log.py
echo. > framework_layer\core\pci_generator.py
echo. > framework_layer\core\http_helper.py
echo. > framework_layer\core\config_file.py
echo. > framework_layer\core\io_helper.py
echo. > framework_layer\core\db_helper.py

REM ��ܲ㾲̬�ļ�
echo. > framework_layer\static\http_helper.py
echo. > framework_layer\static\xml_helper.py
echo. > framework_layer\static\db_helper.py
echo. > framework_layer\static\config_file.py
echo. > framework_layer\static\io_helper.py

REM ���������Ŀ¼���ļ�
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

REM ����������Ŀ¼���ļ�
mkdir auxiliary_layer
echo. > auxiliary_layer\performance_monitor.py
echo. > auxiliary_layer\dynamic_scanner.py
echo. > auxiliary_layer\defect_density.py
echo. > auxiliary_layer\sonar_integration.py
echo. > auxiliary_layer\findbugs_integration.py
echo. > auxiliary_layer\code_coverage.py

REM ������������Ŀ¼���ļ�
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

REM ��������Ŀ¼���ļ�
mkdir reports
mkdir reports\templates
echo. > reports\report_generator.py

REM ����������Ŀ¼���ļ�
mkdir utils
echo. > utils\common_utils.py
echo. > utils\file_utils.py

REM �������ļ��������ļ�
echo # ͳһ�Զ�������ƽ̨����� > main.py
echo # ��Ŀ�����ļ� > requirements.txt

REM ����README�ļ�
echo # ͳһ�Զ�������ƽ̨ > README.md
echo. >> README.md
echo ���ڼܹ�ͼ���ɵ��Զ������Կ�� >> README.md
echo. >> README.md
echo ## �������� >> README.md
echo - ���ʽ��������֧��(XML/Code/BDD/Flowchart) >> README.md
echo - ��ƽ̨����ִ��(Android/iOS/API/Web) >> README.md
echo - �ֲ�ʽ����ִ�� >> README.md
echo - �Զ����������� >> README.md
echo - �������ɼ��� >> README.md
echo. >> README.md
echo ## ���ٿ�ʼ >> README.md
echo 1. ��װ����: pip install -r requirements.txt >> README.md
echo 2. ���û���: �޸�config/config.yaml >> README.md
echo 3. ����ƽ̨: python main.py >> README.md

REM ������ʼ�������ļ�
(
echo # ͳһ�Զ�������ƽ̨����
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

REM �������������ļ�
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

REM �������������
(
echo #!/usr/bin/env python3
echo """
echo ͳһ�Զ�������ƽ̨�����
echo """
echo import logging
echo from config import load_config
echo from user_layer.atc_interface import ATCInterface
echo from engine_layer.jenkins_scheduler import JenkinsScheduler
echo from reports.report_generator import ReportGenerator
echo.
echo def setup_logging():
echo     """������־ϵͳ"""
echo     logging.config.fileConfig('config/logging.conf')
echo     return logging.getLogger(__name__)
echo.
echo def main():
echo     """������"""
echo     logger = setup_logging()
echo     logger.info("����ͳһ�Զ�������ƽ̨")
echo     
echo     # ��������
echo     config = load_config('config/config.yaml')
echo     
echo     # ��ʼ��ATC����
echo     atc_interface = ATCInterface(config)
echo     
echo     # ��ʼ��Jenkins������
echo     jenkins_scheduler = JenkinsScheduler(config)
echo     
echo     # ��ʼ������������
echo     report_generator = ReportGenerator(config)
echo     
echo     # ����ƽ̨
echo     try:
echo         atc_interface.start()
echo     except KeyboardInterrupt:
echo         logger.info("���յ��ж��źţ����ڹر�ƽ̨...")
echo     finally:
echo         logger.info("ͳһ�Զ�������ƽ̨�ѹر�")
echo.
echo if __name__ == "__main__":
echo     main()
) > main.py

echo.
echo ��Ŀ����Ѵ������!
echo Ŀ¼: %CD%
echo.
echo ��һ������:
echo 1. ��װ����: pip install -r requirements.txt
echo 2. ������Ҫ�޸������ļ�: config\config.yaml
echo 3. ��ʼ��������ģ��Ĺ���
echo.
pause