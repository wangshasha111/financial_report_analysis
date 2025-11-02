# 部署到 Streamlit Cloud 指南

## 📋 准备工作检查清单

### 1. 文件准备 ✅
- [x] `app.py` - 主应用文件
- [x] `requirements.txt` - Python 依赖
- [x] `.gitignore` - Git 忽略文件
- [x] `.streamlit/config.toml` - Streamlit 配置
- [x] `packages.txt` - 系统依赖（如需要）

## 🚀 部署步骤

### 步骤 1: 创建 GitHub 仓库

1. 访问 [GitHub](https://github.com) 并登录
2. 点击 "New repository" 创建新仓库
3. 填写仓库信息：
   - **Repository name**: `financial-report-analysis`（或你喜欢的名字）
   - **Description**: "AI-powered financial report analysis tool"
   - **Visibility**: Public 或 Private（免费版 Streamlit Cloud 需要 Public）
   - **不要勾选** "Initialize this repository with a README"
4. 点击 "Create repository"

### 步骤 2: 推送代码到 GitHub

在项目目录中运行以下命令：

```bash
# 切换到项目目录
cd "/Users/wss2023/Dropbox/documents/gen AI curriculum/agentic/6_Prompt Engineering Essentials/project_financial_report_analysis"

# 配置 Git 分支为 main（如果还没配置）
git branch -M main

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit: Financial Report Analysis AI"

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/financial-report-analysis.git

# 推送到 GitHub
git push -u origin main
```

### 步骤 3: 部署到 Streamlit Cloud

1. 访问 [Streamlit Cloud](https://streamlit.io/cloud)
2. 点击 "Sign in" 并使用 GitHub 账号登录
3. 授权 Streamlit 访问你的 GitHub 仓库
4. 点击 "New app" 创建新应用
5. 选择你的仓库和分支：
   - **Repository**: `YOUR_USERNAME/financial-report-analysis`
   - **Branch**: `main`
   - **Main file path**: `app.py`
6. 点击 "Deploy!"

### 步骤 4: 配置环境变量（Secrets）

⚠️ **重要**: 需要配置 API Keys 才能使用

1. 在 Streamlit Cloud 应用页面，点击右上角 "⚙️ Settings"
2. 在左侧菜单选择 "Secrets"
3. 添加以下配置（TOML 格式）：

```toml
# OpenAI API Key (必需 - 如果使用 OpenAI 模型)
OPENAI_API_KEY = "sk-your-actual-openai-api-key"

# Google Gemini API Key (必需 - 如果使用 Gemini 模型)
GEMINI_API_KEY = "your-actual-gemini-api-key"

# Email Configuration (可选 - 如果需要邮件功能)
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

4. 点击 "Save" 保存

### 步骤 5: 等待部署完成

- Streamlit Cloud 会自动安装依赖并启动应用
- 部署过程大约需要 2-5 分钟
- 部署成功后会显示应用 URL，例如：`https://your-app-name.streamlit.app`

## 🔑 获取 API Keys

### OpenAI API Key
1. 访问 [OpenAI Platform](https://platform.openai.com/api-keys)
2. 登录或注册账号
3. 点击 "Create new secret key"
4. 复制 API key（只会显示一次）

### Google Gemini API Key
1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 登录 Google 账号
3. 点击 "Create API key"
4. 复制 API key

### Gmail App Password（如果需要邮件功能）
1. 访问 [Google App Passwords](https://myaccount.google.com/apppasswords)
2. 选择应用：Mail
3. 选择设备：Other (Custom name)
4. 输入名称：Streamlit App
5. 复制生成的 16 位密码

## 📝 更新应用

每次推送代码到 GitHub 后，Streamlit Cloud 会自动重新部署：

```bash
git add .
git commit -m "Update: description of changes"
git push origin main
```

## 🔧 故障排除

### 常见问题

1. **部署失败 - 依赖安装错误**
   - 检查 `requirements.txt` 中的包版本是否兼容
   - 查看部署日志了解具体错误

2. **API Key 错误**
   - 确认在 Streamlit Cloud Secrets 中正确配置了 API keys
   - 检查 API key 是否有效且有足够的配额

3. **应用运行缓慢**
   - Streamlit Cloud 免费版资源有限
   - 考虑升级到付费计划或优化代码

4. **文件上传失败**
   - Streamlit Cloud 有文件大小限制（默认 200MB）
   - 检查 `config.py` 中的 `MAX_FILE_SIZE_MB` 设置

## 📊 监控和管理

在 Streamlit Cloud Dashboard 可以：
- 查看应用运行状态
- 查看日志
- 管理环境变量
- 重启应用
- 查看使用统计

## 🎉 完成！

部署成功后，你可以：
- 分享应用 URL 给其他人使用
- 在 GitHub 仓库的 README 中添加应用链接
- 根据需要继续开发和更新功能

## 💡 提示

- 将 `.streamlit/secrets.toml` 添加到 `.gitignore`，避免泄露 API keys
- 定期检查 API 使用量，避免超出配额
- 可以在 Streamlit Cloud 设置中配置自定义域名（付费功能）
- 使用版本控制进行代码管理，方便回滚

---

如有问题，可以查阅：
- [Streamlit Cloud 文档](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit 论坛](https://discuss.streamlit.io/)
