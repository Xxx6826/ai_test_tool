import pytest
import requests
from config import TARGET_URL
from ai_client import get_ai_test_cases

# 在模块加载时获取 AI 生成的用例（只调用一次）
test_cases = get_ai_test_cases()

# 如果 AI 生成失败，给出提示
if not test_cases:
    pytest.skip("AI 未能生成测试用例，跳过所有测试", allow_module_level=True)


# 这个装饰器让 pytest 为每条用例执行一次测试
@pytest.mark.parametrize("case", test_cases)
def test_api_with_ai_case(case):
    """用 AI 生成的用例执行测试"""
    # 1. 从 AI 生成的用例中提取信息
    case_name = case.get('name', '未命名用例')
    expected_status = case.get('expected_status', 200)

    # 2. 提取 AI 生成的请求体，如果没有则用空字典作为默认值
    request_body = case.get('request_body', {})  # 改成这行，更清晰

    # 3. 发送 POST 请求，并把请求体数据作为 JSON 传过去
    response = requests.post(TARGET_URL, json=request_body)

    # 4. 记录实际状态码
    actual_status = response.status_code

    # 5. pytest 断言：对比实际结果和 AI 的预期
    assert actual_status == expected_status, (
        f"用例 '{case_name}' 失败：预期状态码 {expected_status}，实际 {actual_status}"
    )