#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('deepseek-ai/DeepSeek-OCR',local_dir='./DeepSeek-OCR')
