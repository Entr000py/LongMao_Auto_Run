# 龙猫自动运行器

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个在“夜神安卓模拟器”中自动运行“龙猫”应用任务的脚本。本项目经过重构，采用了现代化、健壮且可扩展的架构，以提高可维护性和可靠性。

**语言:**
[English](./README.md) | [中文](./README.zh-CN.md)

## 主要特性

- **结构化与模块化:** 代码被组织成逻辑清晰的模块（配置、自动化、图像定位），易于维护。
- **配置驱动:** 所有设置、路径和凭据都外置于 `config.yaml` 文件中，告别硬编码。
- **健壮的错误处理:** 实现了自定义异常和 `try...except` 结构，以优雅地处理常见故障（如找不到图像、Nox未启动）。
- **自动重试:** 对失败的图像查找操作进行自动重试，以应对UI延迟，提高成功率。
- **全面的日志记录:** 将所有操作记录到控制台和可轮转的日志文件（`app.log`）中，便于调试。

## 项目结构

```
LongMao_Auto_Run/
├── assets/              # GUI自动化所需的图片资源
├── config/              # 配置文件
│   └── config.yaml
├── src/                 # 源代码
│   ├── automator.py     # 核心自动化逻辑
│   ├── config.py        # 配置加载器
│   ├── exceptions.py    # 自定义异常
│   ├── image_locator.py # 图像识别与点击
│   ├── logger.py        # 日志设置
│   └── utils.py         # 工具函数（如重试装饰器）
├── main.py              # 应用程序的主入口点
├── requirements.txt     # 项目依赖
└── README.zh-CN.md      # 本文件
```

## 开始使用

### 1. 环境要求

- Python 3.8 或更高版本。
- 已安装[夜神安卓模拟器](https://www.yeshen.com/)。

### 2. 克隆仓库

```bash
git clone https://github.com/your-username/LongMao_Auto_Run.git
cd LongMao_Auto_Run
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

在运行本应用前，您必须进行配置：
1.  打开 `config/config.yaml` 文件。
2.  在 `wechat` 部分填入您的微信凭据：
    ```yaml
    wechat:
      account: "你的微信账号"
      password: "你的微信密码"
    ```
3.  （可选）根据需要调整其他设置，如延迟、超时和路径。

## 如何运行

在项目根目录中执行 `main.py` 文件来运行自动化脚本：

```bash
python main.py
```

脚本将启动，并将其进度记录到控制台和 `app.log` 文件中，然后执行自动化任务。

## 工作原理

该脚本使用 `pyautogui` 库来控制鼠标和键盘，模拟用户操作。它通过将屏幕上的UI元素与存储在 `assets/` 目录中的图像进行匹配来找到它们，底层由OpenCV提供支持。整个过程在一个结构化的、基于类的系统中进行编排，以确保清晰性和健壮性。

## 许可证

本项目采用 MIT 许可证。
