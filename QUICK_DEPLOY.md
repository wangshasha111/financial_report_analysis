# 🚀 Streamlit Cloud 部署快速参考

## 📌 下一步操作

### 1️⃣ 创建 GitHub 仓库

访问：https://github.com/new

填写信息：
- **Repository name**: `financial-report-analysis`（或你喜欢的名字）
- **Visibility**: ✅ **Public**（免费 Streamlit Cloud 需要）
- ❌ 不要勾选 "Add a README file"

点击 **"Create repository"**

### 2️⃣ 推送代码到 GitHub

复制 GitHub 提供的命令，或使用以下命令（替换 YOUR_USERNAME）：

```bash
cd "/Users/wss2023/Dropbox/documents/gen AI curriculum/agentic/6_Prompt Engineering Essentials/project_financial_report_analysis"

# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/financial-report-analysis.git

# 推送代码
git push -u origin main
```

**输入你的 GitHub 用户名和密码（或 Personal Access Token）**

### 3️⃣ 部署到 Streamlit Cloud

1. 访问：https://streamlit.io/cloud
2. 点击 **"Sign in"** 用 GitHub 账号登录
3. 点击 **"New app"**
4. 填写信息：
   - **Repository**: `YOUR_USERNAME/financial-report-analysis`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. 点击 **"Deploy!"**

### 4️⃣ 配置 API Keys（重要！）

在 Streamlit Cloud 应用页面：

1. 点击右上角 **⚙️ "Settings"**
2. 选择 **"Secrets"**
3. 粘贴以下内容（替换为你的真实 API keys）：

```toml
# OpenAI API Key (必需 - 如果使用 OpenAI)
OPENAI_API_KEY = "sk-proj-your-actual-key-here"

# Google Gemini API Key (必需 - 如果使用 Gemini)
GEMINI_API_KEY = "AIza-your-actual-key-here"
```

4. 点击 **"Save"**
5. 应用会自动重启

### 5️⃣ 完成！🎉

- 应用 URL：`https://your-app-name.streamlit.app`
- 可以分享给任何人使用
- 每次推送代码到 GitHub，Streamlit Cloud 会自动更新

---

## 🔑 获取 API Keys

### OpenAI
1. 访问：https://platform.openai.com/api-keys
2. 登录并创建 API key
3. 复制密钥（只显示一次）

### Google Gemini
1. 访问：https://makersuite.google.com/app/apikey
2. 登录并创建 API key
3. 复制密钥

---

## 📝 更新应用

修改代码后：

```bash
git add .
git commit -m "描述你的更改"
git push origin main
```

Streamlit Cloud 会自动检测并重新部署！

---

## ❓ 常见问题

**Q: 部署失败怎么办？**
A: 查看 Streamlit Cloud 的日志，通常是依赖问题或 Python 版本问题

**Q: API Key 无效？**
A: 确保在 Secrets 中正确配置，注意格式（TOML）

**Q: 应用太慢？**
A: 免费版资源有限，考虑升级或优化代码

**Q: 可以用私有仓库吗？**
A: 付费 Streamlit Cloud 可以，免费版需要公开仓库

---

需要详细说明？查看 **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**
