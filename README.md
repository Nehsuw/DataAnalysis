# AI 全自动数据分析系统

> 智能文档 OCR 识别、信息结构化、可视化报告生成与智能问答

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3+-3178C6.svg)](https://www.typescriptlang.org/)

## 项目简介

这是一个端到端的 AI 数据分析系统，完整流程：

```
上传文档 → OCR 识别 → 信息结构化 → 智能问答 → 可视化报告 → PDF 导出
```

系统支持 PDF、图片等文档的自动 OCR 识别，通过大语言模型进行信息结构化，并基于用户问题生成交互式可视化报告。

## 技术架构

### 后端 (Python)

| 技术 | 用途 |
|------|------|
| FastAPI | Web 框架 |
| LangChain | AI 编排 |
| Pydantic | 数据验证 |
| Transformers | AI/ML 模型 |
| DeepSeek-OCR | 文档识别 |

### 前端 (TypeScript/React)

| 技术 | 用途 |
|------|------|
| React 18 | UI 框架 |
| Vite | 构建工具 |
| TypeScript | 类型安全 |
| Tailwind CSS | 样式框架 |
| shadcn/ui | UI 组件库 |
| Recharts | 数据可视化 |
| Framer Motion | 动画效果 |

## 快速开始

### 前置要求

- Python 3.10+
- Node.js 18+
- npm 或 yarn

### 1. 启动后端服务

```bash
cd backend

# 创建虚拟环境 (可选)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
# 或 uvicorn app:app --host 0.0.0.0 --port 8708 --reload
```

后端服务默认运行在: http://localhost:8708

### 2. 启动前端服务

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端默认运行在: http://localhost:3000

### 3. 完整工作流

1. 打开浏览器访问 http://localhost:3000
2. 上传 PDF/图片文档
3. 系统自动进行 OCR 识别
4. 在聊天窗口输入分析问题
5. 查看可视化报告
6. 导出 PDF 报告

## 项目结构

```
DataAnalysis/
├── backend/                 # 后端服务
│   ├── app.py               # 主 API 服务
│   ├── config/              # 配置模块
│   ├── core/                # 核心业务逻辑
│   │   ├── analysis/        # 数据分析
│   │   ├── visualization/   # 可视化生成
│   │   └── ocr/             # OCR 相关
│   ├── services/            # 服务层
│   ├── utils/               # 工具函数
│   ├── backwark/            # 备用模块
│   └── external/            # 外部服务 (DeepSeek-OCR)
│
├── frontend/                # 前端应用
│   ├── components/          # React 组件
│   │   ├── ui/             # shadcn/ui 组件
│   │   ├── api.ts          # API 接口
│   │   ├── Header.tsx
│   │   ├── DataVisualization.tsx
│   │   ├── ChatAssistant.tsx
│   │   └── ReportPreviewModal.tsx
│   ├── styles/              # 样式文件
│   ├── App.tsx             # 主应用
│   ├── main.tsx            # 入口文件
│   └── package.json
│
├── pdfs/                    # 样例文档
├── imgs/                    # 测试图片
└── README.md               # 本文件
```

## API 接口

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /ocr | 上传文档进行 OCR 识别 |
| GET | /status/{task_id} | 获取任务状态 |
| GET | /results/{task_id} | 获取 OCR 结果 |
| POST | /analyze | 根据问题生成可视化报告 |
| GET | /view_report/{answer_id} | 查看可视化报告 |
| POST | /export_pdf | 导出 PDF 报告 |
| GET | /download_pdf/{filename} | 下载 PDF |
| GET | /health | 健康检查 |

详细 API 文档请访问: http://localhost:8708/docs (Swagger UI)

## 功能特性

- ✅ 支持 PDF、图片等多种文档格式 OCR 识别
- ✅ 自动信息结构化与数据提取
- ✅ 基于自然语言的智能问答分析
- ✅ 交互式可视化图表生成 (ECharts)
- ✅ 精美 PDF 报告导出
- ✅ 完整的亮色/暗色主题切换
- ✅ 响应式设计与玻璃态 UI
- ✅ 50+ 可复用 UI 组件

## 环境变量

### 后端配置

在 `backend/.env` 中配置:

```env
# OCR 服务配置
OCR_BASE_URL=http://localhost:8000

# 输出目录
OUTPUT_DIR=./outputs
```

### 前端配置

前端默认连接 `http://localhost:8708`，如有需要可在 `components/api.ts` 中修改。

## 浏览器支持

| 浏览器 | 最低版本 |
|--------|----------|
| Chrome | >= 90 |
| Firefox | >= 88 |
| Safari | >= 14 |
| Edge | >= 90 |

## 常见问题

### Q: 如何修改后端端口?

在 `backend/config/settings.py` 中修改 `PORT` 值，或启动时指定:
```bash
uvicorn app:app --port 8080
```

### Q: 前端如何连接不同的后端?

修改 `frontend/components/api.ts` 中的 `API_BASE_URL`。

### Q: 如何添加新的可视化图表类型?

在前端 `components/DataVisualization.tsx` 中添加新的图表组件，后端在 `core/visualization/` 中实现对应生成逻辑。

### Q: OCR 服务启动失败?

确保 DeepSeek-OCR 服务已正确部署，参考 `backend/external/ocr/DeepSeek-OCR-vllm/README.md`。

---

## DeepSeek-OCR 模型下载与部署

本项目使用 DeepSeek-OCR 进行文档识别，需要先下载模型并启动 OCR 服务。

### 硬件要求

- **GPU**: NVIDIA RTX 3090/4090 或同等级别
- **显存**: 最少 16GB，推荐 24GB+
- **内存**: 最少 32GB，推荐 64GB+
- **存储**: 至少 100GB 可用空间

### 下载模型

项目已提供下载脚本，直接运行即可：

```bash
# 在项目根目录运行
python download_deepseek_ocr.py
```

脚本会自动从 ModelScope 下载模型到 `./DeepSeek-OCR` 目录。

### 配置 OCR 服务

项目已在 `backend/.env` 中预配置好 OCR 服务：

```env
DEEPSEEK_MODEL_PATH=/home/data/nongwa/workspace/model/OCR/DeepSeek-OCR
DEEPSEEK_OCR_URL=http://192.168.110.131:8707/ocr
DEEPSEEK_OCR_PORT=8707
```

如需修改模型路径或端口，编辑 `backend/.env` 即可。

### 启动 OCR 服务

```bash
cd backend/external/ocr/DeepSeek-OCR-vllm/

# 方式1: 快速启动
chmod +x quick_start.sh
./quick_start.sh

# 方式2: 使用管理脚本
chmod +x start_server.sh
./start_server.sh
```

### 验证 OCR 服务

```bash
# 健康检查
curl http://localhost:8707/health

# 测试 OCR
curl -X POST "http://localhost:8707/ocr" \
  -F "file=@test.jpg"
```

### 配置主服务连接 OCR

后端已通过 `backend/.env` 预配置 OCR 服务地址：
```env
DEEPSEEK_OCR_URL=http://192.168.110.131:8707/ocr
```

详细部署说明请参考: `backend/external/ocr/DeepSeek-OCR-vllm/README.md`

---

## 许可证

MIT License - 详见 LICENSE 文件

## 联系方式

如有问题或建议，请提交 Issue 或联系开发团队。