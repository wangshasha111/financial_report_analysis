# 📊 财务报告分析 AI

智能网页应用，使用 AI 分析财务文档，为您的专业角色提供定制化的洞察。

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ 功能特性

- 🤖 **双AI支持**: OpenAI (GPT-4o, GPT-4o Mini) 和 Google Gemini (1.5 Pro, 1.5 Flash)
- 👥 **角色定制**: 投资者、分析师、审计师或自定义角色
- 📊 **分析类型**: 综合、风险、增长、盈利能力分析
- 📄 **PDF导出**: 专业格式化报告
- 🧪 **调试模式**: 无需 API 成本即可测试
- ✏️ **自定义提示词**: 编辑或创建您自己的提示词

## 🚀 快速开始

### 1. 环境设置

```bash
# 创建虚拟环境（仅第一次需要）
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 获取 API 密钥

选择一个或两个都用：
- **OpenAI**: https://platform.openai.com/api-keys
- **Gemini**: https://makersuite.google.com/app/apikey

### 3. 运行应用

```bash
# 简便方式（macOS）
./run.command

# 或手动运行
streamlit run app.py
```

应用将在浏览器中打开：`http://localhost:8501`

## 📖 使用说明

### 基本流程

1. **启用调试模式**（可选，用于测试）
   - 在侧边栏勾选 "Enable Debug Mode"
   - 无需 API 密钥，使用示例数据

2. **配置 AI**（用于真实分析）
   - 选择 AI 提供商（OpenAI 或 Gemini）
   - 选择模型
   - 输入 API 密钥

3. **选择角色**
   - 投资者、分析师、审计师或自定义

4. **上传文档**
   - 拖放财务报告图片（PNG, JPG, JPEG）
   - 每个文件最大 10MB

5. **选择分析类型**
   - 点击：Overall, Risk, Growth 或 Profitability
   - 根据需要自定义提示词

6. **分析和导出**
   - 点击 "Analyze Documents"
   - 从结果标题处下载 PDF

## 💡 使用技巧

### 最佳实践
- 从**调试模式**开始测试界面
- 使用 **GPT-4o** 或 **Gemini 1.5 Pro** 进行复杂分析
- 上传清晰、高分辨率的图片
- 根据特定需求自定义提示词

### 成本优化
- 使用**调试模式**进行测试（免费）
- **GPT-4o Mini** 或 **Gemini 1.5 Flash** 更快更便宜
- 在一次分析中合并多页

### 常见问题

**Gemini 404 错误**
- 应用使用 Gemini 1.5 Pro/Flash 模型
- 确保您的 API 密钥已启用 Gemini API
- 如果一个模型不工作，尝试其他模型

**PDF 格式**
- 项目符号格式正确
- Markdown 转换为干净文本
- 标题有适当的样式

## 🔧 配置

### 支持的模型

**OpenAI:**
- GPT-4 Vision（旧版）
- GPT-4o（推荐）
- GPT-4o Mini（快速且便宜）

**Gemini:**
- Gemini 1.5 Pro（强大）
- Gemini 1.5 Flash（快速）
- Gemini Pro（基础）

### 文件支持
- 格式：PNG, JPG, JPEG
- 最大大小：每个文件 10MB
- 多文件：支持

## 📁 项目结构

```
project_financial_report_analysis/
├── app.py                 # 主 Streamlit 应用
├── requirements.txt       # Python 依赖
├── run.command           # macOS 启动脚本
├── src/
│   ├── config.py         # 配置常量
│   ├── prompts.py        # 分析提示词模板（16个）
│   ├── ai_handler.py     # OpenAI 和 Gemini 集成
│   ├── mock_data.py      # 调试模式示例数据
│   └── utils/
│       ├── pdf_generator.py    # PDF 导出
│       └── image_utils.py      # 图片处理
├── test_image/           # 测试图片样例
└── .gitignore            # Git 忽略规则
```

**注意**: 请自行创建虚拟环境（`venv/`）- 项目中不包含。

## 🎯 分析类型说明

### 综合分析（Overall Analysis）
全面审查，包括：
- 关键财务指标及同比/环比
- 损益表、资产负债表、现金流量表
- 战略举措和市场展望
- 投资建议

### 风险分析（Risk Analysis）
聚焦于：
- 财务风险和危险信号
- 市场和运营风险
- 风险缓解策略
- 合规问题

### 增长分析（Growth Analysis）
评估：
- 收入增长趋势
- 市场机会
- 竞争定位
- 扩张策略

### 盈利能力分析（Profitability Analysis）
深入研究：
- 利润率（毛利率、营业利润率、净利率）
- 回报指标（ROE, ROA, ROIC）
- 盈利质量
- 成本结构效率

## 🔐 安全性

- ✅ API 密钥：仅当前会话使用，不存储
- ✅ 图片：在内存中处理，不保存
- ✅ 无数据收集或跟踪
- ✅ 开源，可检查代码

## 🛠️ 开发

### 添加自定义提示词

编辑 `src/prompts.py` 添加或修改分析模板：

```python
PROMPTS = {
    "Overall Analysis": {
        "您的角色": "您的自定义提示词...",
    }
}
```

### 扩展 AI 提供商

在 `src/ai_handler.py` 中添加新提供商：

```python
class AIHandler:
    def __init__(self, provider, model, api_key):
        if provider == 'your_provider':
            # 初始化您的提供商
            pass
```

## 📜 版本历史

详细版本历史请见 [CHANGELOG.md](CHANGELOG.md)。

**当前版本：1.0.3**
- ✅ 修复 PDF 格式（正确的项目符号，无 markdown）
- ✅ 简化UI（删除邮件，精简导出）
- ✅ 更新 Gemini 模型（1.5 Pro/Flash）
- ✅ 调试模式免费测试

## 📄 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🤝 贡献

欢迎贡献！改进方向：
- 额外的 AI 提供商（Claude 等）
- 增强的图表识别
- 批量处理
- 更多导出格式
- 额外的分析模板

## 💬 支持

如有问题：
1. 查看本 README
2. 查看 CHANGELOG.md
3. 检查代码（有详细注释）

---

**用 ❤️ 为金融专业人士打造**

*简化您的财务文档分析工作流程*
