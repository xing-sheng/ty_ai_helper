import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 配置 API Key 和 API URL
API_KEY = os.getenv("DASHSCOPE_API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL = "qwen-plus"
