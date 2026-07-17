# 配置文件
import os

DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

# 被测接口
TARGET_URL = "https://jsonplaceholder.typicode.com/posts"