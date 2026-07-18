# AI 驱动的接口自动化测试工具

## 项目简介
本项目使用 **Python + Pytest + DeepSeek AI** 实现了一个智能化的接口自动化测试工具。通过调用 DeepSeek 大模型自动生成测试用例，并自动执行测试，大大提高了测试用例的编写效率。

## 核心功能
- **AI 自动生成测试用例**：只需提供接口信息，AI 即可自动生成覆盖正常和异常场景的测试用例
- **支持多种请求方法**：已实现 GET 和 POST 请求的自动化测试
- **自动化测试执行**：基于 Pytest 框架，自动执行 AI 生成的用例并输出报告
- **HTML 测试报告**：自动生成可视化测试报告，方便查看结果

## 技术栈
- Python 3.11
- Pytest（测试框架）
- Requests（HTTP 请求）
- DeepSeek API（AI 生成用例）

## 项目结构
```

ai_test_tool/
├── config.py          # 配置文件（API Key 从环境变量读取）
├── ai_client.py       # AI 调用逻辑（与 DeepSeek 交互）
├── test_runner.py     # 测试执行文件（Pytest 用例）
├── reports/           # 测试报告存放目录
└── README.md          # 项目说明文档

```

## 快速开始
1. 克隆项目到本地
2. 安装依赖：`pip install requests pytest pytest-html`
3. 设置环境变量 `DEEPSEEK_API_KEY`
4. 运行测试：`pytest test_runner.py -v`

## 作者
- 谢宝乐
- GitHub: [XXX6826](https://github.com/XXX6826)
```
