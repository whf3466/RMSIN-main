# import os
# from huggingface_hub import hf_hub_download
#
# # 获取 Hugging Face 缓存目录
# cache_dir = os.path.dirname(hf_hub_download(repo_id="bert-base-uncased", filename="config.json"))
# print(f"Hugging Face 缓存目录: {cache_dir}")

# from transformers import BertModel
#
# try:
#     print("尝试加载 bert-base-uncased...")
#     model = BertModel.from_pretrained("bert-base-uncased")
#     print("加载成功!")
# except Exception as e:
#     print(f"加载失败: {e}")
import os
from huggingface_hub import hf_hub_download

# 获取 Hugging Face 缓存目录
cache_dir = os.path.dirname(hf_hub_download(repo_id="bert-base-uncased", filename="config.json"))
print(f"Hugging Face 缓存目录: {cache_dir}")