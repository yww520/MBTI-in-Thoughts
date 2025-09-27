from dotenv import load_dotenv  # 新增这行
load_dotenv()  # 加载 .env 文件中的环境变量
from langchain_community.chat_models.tongyi import ChatTongyi
import os

# 从环境变量读取密钥（不再硬编码）
# 注意：删除原来的 os.environ["DASHSCOPE_API_KEY"] = "YOUR_API_KEY_HERE" 这行
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    # 若未找到环境变量，抛出明确错误，避免隐式失败
    raise ValueError("请设置环境变量 DASHSCOPE_API_KEY 以使用千问API")

# 初始化千问模型
llm = ChatTongyi(model_name="qwen3-max", temperature=0.7)

# 测试生成故事
response = llm.invoke("生成一个50字的短篇故事，主题是小猫和小狗一起救小鸟")
print("千问模型输出：")
print(response.content)