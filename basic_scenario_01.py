import pytest
import allure
import requests
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

@pytest.fixture(scope="class")
def driver_setup(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14.0"
    options.device_name = "SM-S928N"
    options.app_package = "com.datau.eventu"
    options.app_activity = "com.datau.eventu.MainActivity"
    options.automation_name = "UiAutomator2"
    options.autoGrantPermissions = True

    driver = webdriver.Remote('http://localhost:4723', options=options)
    driver.implicitly_wait(30)

    request.cls.driver = driver
    yield
    driver.quit()

def send_slack_message(message):
    webhook_url = "https://hooks.slack.com/services/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"  # 본인 Webhook URL
    headers = {"Content-Type": "application/json"}
    payload = {"text": message}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print(f"Slack 전송 실패: {response.status_code} {response.text}")

@pytest.mark.usefixtures("driver_setup")
class TestAppium:

    @allure.title("앱 실행 및 권한 허용")
    def test_EA_LG_001(self):
        # 예: 권한 허용 UI 처리 코드
        pass

    @allure.title("로그인 화면 이동")
    def test_EA_LG_002(self):
        pass

    @allure.title("카카오톡 로그인 및 혜택 화면 확인")
    def test_EA_LG_003(self):
        # 예: assert문 예시
        assert True

# -- 여기에 테스트 추가
