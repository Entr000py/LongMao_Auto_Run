# LongMao Auto Runner

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated script for running tasks in the "LongMao" application inside the Nox Android emulator. This project has been refactored with a modern, robust, and scalable architecture to improve maintainability and reliability.

**Language:**
[English](./README.md) | [中文](./README.zh-CN.md)

## Key Features

- **Structured & Modular:** Code is organized into logical modules (config, automation, image location) for easy maintenance.
- **Configuration-Driven:** All settings, paths, and credentials are externalized into a `config.yaml` file. No more hard-coded values.
- **Robust Error Handling:** Implements custom exceptions and a `try...except` structure to handle common failures gracefully (e.g., image not found, Nox not started).
- **Automatic Retries:** Automatically retries failed image-finding operations to handle UI lag and improve success rates.
- **Comprehensive Logging:** Logs all actions to both the console and a rotating log file (`app.log`) for easy debugging.

## Project Structure

```
LongMao_Auto_Run/
├── assets/              # Image assets for GUI automation
├── config/              # Configuration files
│   └── config.yaml
├── src/                 # Source code
│   ├── automator.py     # Core automation logic
│   ├── config.py        # Config loader
│   ├── exceptions.py    # Custom exceptions
│   ├── image_locator.py # Image recognition and clicking
│   ├── logger.py        # Logging setup
│   └── utils.py         # Utility functions (e.g., retry decorator)
├── main.py              # Main entry point of the application
├── requirements.txt     # Project dependencies
└── README.md            # This file
```

## Getting Started

### 1. Prerequisites

- Python 3.8 or newer.
- [Nox Android Emulator](https://www.bignox.com/) installed.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/LongMao_Auto_Run.git
cd LongMao_Auto_Run
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you must configure it:
1.  Open the `config/config.yaml` file.
2.  Fill in your WeChat credentials under the `wechat` section:
    ```yaml
    wechat:
      account: "your_wechat_account"
      password: "your_wechat_password"
    ```
3.  (Optional) Adjust other settings like delays, timeouts, and paths as needed.

## Usage

To run the automation script, execute the `main.py` file from the project root directory:

```bash
python main.py
```

The script will start, log its progress to the console and `app.log`, and perform the automated tasks.

## How It Works

The script uses the `pyautogui` library to control the mouse and keyboard, simulating user actions. It finds UI elements on the screen by matching them with images stored in the `assets/` directory, powered by OpenCV. The entire process is orchestrated within a structured class-based system for clarity and robustness.

## License

This project is licensed under the MIT License.