from langchain_community.chat_models.tongyi import ChatTongyi
import os

# 替换为你的阿里云 DashScope API 密钥
os.environ["DASHSCOPE_API_KEY"] = "sk-4acc2eacd26b4dd7923d0a71e6d4c0b0"

# 初始化千问模型（Python 3.11 下可正常调用）
llm = ChatTongyi(model_name="qwen3-max", temperature=0.7)

# 测试生成故事
response = llm.invoke("生成一个50字的短篇故事，主题是小猫和小狗一起救小鸟")
print("千问模型输出：")
print(response.content)