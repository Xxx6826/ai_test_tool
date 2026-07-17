import requests
import json
from config import DEEPSEEK_API_KEY, DEEPSEEK_URL

def get_ai_test_cases():
    """调用 DeepSeek AI 生成测试用例"""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = """
你是一个资深的测试工程师。请为"创建新文章"接口设计测试用例。

接口信息：
- URL: https://jsonplaceholder.typicode.com/posts
- 方法: POST
- 请求体（JSON格式）:
{
    "title": "文章的标题",
    "body": "文章的内容",
    "userId": 1
}

要求：
1. 设计 5 条测试用例，覆盖正常和异常场景（例如：缺少必填字段、字段类型错误等）。
2. 每条用例必须包含：用例名称、预期HTTP状态码、以及对应的请求体数据（用于执行测试）。
3. 以 JSON 数组格式返回，格式如下：
[
    {"name": "用例名称", "expected_status": 200, "request_body": {"title": "xxx", "body": "xxx", "userId": 1}},
    ...
]
只返回 JSON 数组，不要其他内容。
"""

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个资深的软件测试专家，只返回JSON格式数据。"},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(DEEPSEEK_URL, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            ai_content = result['choices'][0]['message']['content']
            test_cases = json.loads(ai_content)
            print(f"✅ AI 成功生成 {len(test_cases)} 条测试用例")
            return test_cases
        else:
            print(f"❌ AI 请求失败: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ 调用 AI 时出错: {e}")
        return []