# 🖥️ 使用 GitHub Desktop 部署指南

## 📌 前提条件

- ✅ 已安装 GitHub Desktop
- ✅ 已有 GitHub 账号
- ✅ 项目代码已准备好

---

## 🚀 部署步骤

### 第 1 步：在 GitHub Desktop 中打开项目

1. 打开 **GitHub Desktop**
2. 点击菜单 **File** → **Add Local Repository**
3. 点击 **Choose...** 选择项目文件夹：
   ```
   /Users/wss2023/Dropbox/documents/gen AI curriculum/agentic/6_Prompt Engineering Essentials/project_financial_report_analysis
   ```
4. 点击 **Add Repository**

### 第 2 步：发布到 GitHub

1. 在 GitHub Desktop 中，你应该看到：
   - ✅ 当前分支：`main`
   - ✅ 25 个文件的更改（Initial commit）

2. 点击右上角的 **Publish repository** 按钮

3. 在弹出窗口中填写：
   - **Name**: `financial-report-analysis`（或你喜欢的名字）
   - **Description**: `AI-powered financial report analysis tool`
   - ❌ **取消勾选** "Keep this code private"（免费 Streamlit 需要公开仓库）
   - ✅ **勾选** "Include all files"

4. 点击 **Publish Repository**

5. 等待上传完成（可能需要 1-2 分钟）

### 第 3 步：在浏览器中查看仓库

1. 在 GitHub Desktop 中，点击菜单 **Repository** → **View on GitHub**
2. 浏览器会打开你的 GitHub 仓库页面
3. 确认所有文件都已上传

### 第 4 步：部署到 Streamlit Cloud

1. 访问：**https://streamlit.io/cloud**

2. 点击 **"Sign in"** 用 GitHub 账号登录

3. 点击 **"New app"** 创建应用

4. 填写部署信息：
   - **Repository**: 选择 `你的用户名/financial-report-analysis`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): 自定义网址（可选）

5. 点击 **"Deploy!"**

### 第 5 步：配置 API Keys（⚠️ 重要！）

应用部署后需要配置 API keys 才能正常工作：

1. 在 Streamlit Cloud 应用页面，点击右上角 **⚙️ Settings**

2. 在左侧菜单选择 **Secrets**

3. 在编辑器中粘贴以下内容（替换为你的真实 API keys）：

```toml
# OpenAI API Key（如果使用 OpenAI 模型）
OPENAI_API_KEY = "sk-proj-xxxxx你的真实密钥xxxxx"

# Google Gemini API Key（如果使用 Gemini 模型）
GEMINI_API_KEY = "AIzaxxxxx你的真实密钥xxxxx"
```

4. 点击 **"Save"**

5. 应用会自动重启（大约 30 秒）

### 第 6 步：测试应用 ✅

1. 等待部署完成（状态变为 ✅ Running）

2. 点击应用 URL（例如：`https://your-app.streamlit.app`）

3. 测试功能：
   - 启用 Debug Mode（无需 API key）
   - 或者使用真实 API key 进行分析

4. 🎉 **完成！**

---

## 🔄 后续更新代码

当你修改代码后，使用 GitHub Desktop 推送更新：

### 方法：使用 GitHub Desktop

1. **修改代码**后，打开 GitHub Desktop

2. 在左侧看到修改的文件列表

3. 在左下角填写：
   - **Summary**: 简短描述（例如：`Update analysis prompts`）
   - **Description**: 详细说明（可选）

4. 点击 **"Commit to main"**

5. 点击右上角 **"Push origin"**

6. Streamlit Cloud 会自动检测并重新部署（1-2 分钟）

---

## 🔑 获取 API Keys

### OpenAI API Key

1. 访问：https://platform.openai.com/api-keys
2. 登录或注册账号
3. 点击 **"Create new secret key"**
4. 输入名称（例如：`Streamlit App`）
5. ✅ 复制密钥（只显示一次！）
6. 保存到安全的地方

### Google Gemini API Key

1. 访问：https://makersuite.google.com/app/apikey
   或：https://aistudio.google.com/app/apikey
2. 登录 Google 账号
3. 点击 **"Create API key"**
4. 选择项目或创建新项目
5. ✅ 复制密钥
6. 保存到安全的地方

---

## ❓ 常见问题

### Q1: 为什么必须是公开仓库？
A: Streamlit Cloud 免费版只支持公开 GitHub 仓库。付费版支持私有仓库。

### Q2: API Keys 安全吗？
A: ✅ 安全！配置在 Streamlit Secrets 中的 API keys 是加密存储的，不会显示在代码中。

### Q3: 部署失败怎么办？
A: 
- 检查 Streamlit Cloud 的部署日志（Logs）
- 确认 `requirements.txt` 中的包版本兼容
- 确认 Python 版本（3.8+）

### Q4: 怎么查看应用日志？
A: 在 Streamlit Cloud 应用页面，点击右下角的 **"Manage app"** → **"Logs"**

### Q5: 更新代码后应用没有自动部署？
A: 
- 确认代码已推送到 GitHub（在 GitHub Desktop 中检查）
- 在 Streamlit Cloud 点击 **"Reboot app"** 手动重启

### Q6: 应用运行很慢？
A: 免费版资源有限（1GB RAM），可以：
- 优化代码
- 减少图片大小
- 升级到付费计划

---

## 📊 部署后的应用 URL

你的应用会有一个类似这样的 URL：

```
https://financial-report-analysis-xxxxx.streamlit.app
```

或者自定义为：

```
https://你自定义的名字.streamlit.app
```

可以分享这个链接给任何人使用！

---

## 💡 提示

- ✅ 定期备份 API keys
- ✅ 在 README 中添加应用链接
- ✅ 使用 `.gitignore` 避免提交敏感信息
- ✅ 定期检查 API 使用量
- ✅ 可以在 Streamlit Cloud 设置中配置自定义域名（付费）

---

## 🎯 总结

使用 GitHub Desktop 部署到 Streamlit Cloud 的流程：

```
1. GitHub Desktop: Publish repository
2. Streamlit Cloud: New app → 选择仓库
3. Streamlit Cloud: Settings → Secrets → 添加 API keys
4. 完成！分享你的应用 URL
```

简单快捷！🚀

---

需要帮助？
- 📚 查看 [Streamlit 官方文档](https://docs.streamlit.io)
- 💬 访问 [Streamlit 论坛](https://discuss.streamlit.io)
