# SeedDream 视觉理解
一个 Claude Skills 项目，让AI帮助你理解图片.

## 视觉理解模型
Doubao-Seed-1.8多模态深度思考模型，同时支持minimal/low/medium/high 四种reasoning effort，其中minimal为不思考。 更强模型效果，服务复杂任务和有挑战场景。支持 256k 上下文窗口，输出长度支持最大 96k tokens。

### API 使用示例
```python
import os
from volcenginesdkarkruntime import Ark

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Ark客户端，从环境变量中读取您的API Key
client = Ark(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key。此为默认方式，您可根据需要进行修改
    api_key=os.environ.get("ARK_API_KEY"),
)

response = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model="doubao-seed-1-8-251228",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://ark-project.tos-cn-beijing.ivolces.com/images/view.jpeg"
                    },
                },
                {"type": "text", "text": "这是哪里？"},
            ],
        }
    ],
    reasoning_effort="medium"
)

print(response.choices[0])
```

## 项目简介

SeedDream 视觉理解通过整合火山引擎的 Doubao Seed 1.8 多模态深度思考模型，帮助你深入理解和分析图片内容。这个技能支持深度推理、细节识别、场景理解等多种视觉理解任务，可灵活控制推理深度。

## 核心功能

🧠 **深度视觉理解**
- 基于 Doubao Seed 1.8 多模态模型进行图像分析
- 支持四种推理级别：minimal（无思考）、low（浅层思考）、medium（中等思考）、high（深度思考）
- 256k 上下文窗口，支持最大 96k tokens 输出
- 强大的多模态深度思考能力，适合复杂任务和有挑战场景

🔍 **多样化分析能力**
- 场景识别与描述
- 文字识别与提取（OCR）
- 物体检测与分类
- 情感分析与理解
- 细节发现与解释

💡 **灵活应用场景**
- 单张图片分析
- 批量图片对比
- 多图片关联理解
- 复杂场景推理

## 使用场景

当你需要：

- 📷 理解图片中的内容、场景或故事
- 🔎 从图片中提取文字信息
- 🎨 分析图片的风格、构图、色彩等视觉元素
- 📊 对比多张图片的差异和关联
- 🧩 解答关于图片的复杂问题
- 📝 获取图片的详细描述和解释

## 安装与使用

### 安装技能

将此项目复制到你的工作目录下的 `.claude/skills/` 文件夹中，记得删掉 README：

```
<你的项目根目录>/
└── .claude/
    └── skills/
        └── seedream-image-understanding/    # 本技能包
            ├── SKILL.md
```

### 使用技能

在 Claude Code 中，发送以下指令即可启用此技能：

```
使用 seedream-image-understanding 分析图片
```

AI agent 会自动：
- 读取技能配置和指引
- 接收你的图片和分析需求
- 调用 Seedream API 进行深度分析

### 准备工作

**重要**：首次使用前，你需要获取火山引擎 ARK API 密钥。

获取方式：
1. 访问：https://console.volcengine.com/ark/region:ark+cn-beijing/apikey
2. 创建或查看你的 ARK API 密钥

AI agent 会在首次使用时自动询问你的 API 密钥。

### 开始分析图片

配置完成后，直接告诉 AI 你想要分析的图片和问题：

**示例 1：基础图片描述**
```
分析这张图片，描述其中的内容和场景
https://example.com/image.jpg
```

**示例 2：深度推理分析**
```
深度分析这张图片，理解其中的故事情节和人物情感
https://example.com/complex_scene.jpg
```

**示例 3：文字提取**
```
提取这张图片中的所有文字内容
https://example.com/document.jpg
```

**示例 4：图片对比**
```
对比这两张图片的差异
https://example.com/image1.jpg
https://example.com/image2.jpg
```

**示例 5：细节分析**
```
仔细分析这张图片的构图、色彩和光影运用
https://example.com/artwork.jpg
```

AI 将：
- 接收你的图片 URL 和分析需求
- 根据任务复杂度选择合适的推理级别
- 调用 Seedream API 进行深度分析
- 提供详细的分析结果

## 项目结构

### 技能包结构（位于 `.claude/skills/seedream-image-understanding/`）

```
seedream-image-understanding/
├── SKILL.md            # 技能详细文档（AI agent 会读取此文件）
├── README.md           # 使用说明文档（本文件）
```

## 工作流程

1. **接收请求**：理解用户想要分析的图片和问题
2. **确认 API 密钥**：确保已获取用户的 ARK API 密钥
3. **明确需求**：
   - 图片 URL（支持多张图片）
   - 分析任务类型
   - 推理深度偏好（minimal/low/medium/high）
4. **执行分析**：调用 Seedream API 进行图像理解
5. **报告结果**：提供详细的分析结果和洞察

## 功能详解

**推理级别说明：**
- `minimal`：快速响应，适用于简单识别和描述
- `low`：浅层思考，适用于基础分析和理解
- `medium`（推荐）：中等深度思考，适用于大多数复杂场景
- `high`：深度推理，适用于最具挑战性的复杂任务

**支持的图片格式：**
- JPEG (.jpg, .jpeg)
- PNG (.png)
- WebP (.webp)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- GIF (.gif)
- ICO (.ico)
- DIB (.dib)
- ICNS (.icns)
- SGI (.sgi)
- JPEG2000 (.j2c, .j2k, .jp2, .jpc, .jpf, .jpx)
- HEIC (.heic) - doubao-1.5-vision-pro 及以后模型支持
- HEIF (.heif) - doubao-1.5-vision-pro 及以后模型支持

**图片大小限制：**
- URL 传入：单张图片不超过 10MB
- Base64 编码：单张图片不超过 10MB，请求体不超过 64MB
- 文件路径传入：单张图片不超过 512MB

**图片像素要求：**
- 宽 > 14px 且高 > 14px
- 宽×高范围：[196px, 36,000,000px]

## API 参数说明

**主要参数：**
- `model`：使用的模型（默认：`doubao-seed-1-8-251228`）
- `messages`：对话消息列表
  - `role`：消息角色（通常为 "user"）
  - `content`：消息内容数组
    - `type: "image_url"`：图片输入
      - `image_url.url`：图片 URL
    - `type: "text"`：文字问题或指令
      - `text`：分析问题或提示词
- `reasoning_effort`：推理深度级别
  - `"minimal"`：无思考
  - `"low"`：浅层思考
  - `"medium"`：中等思考
  - `"high"`：深度思考
- `detail`：图片理解精细度（可选）
  - `"low"`：低分辨率模式，处理速度快，适合简单场景
  - `"high"`：高分辨率模式（doubao-seed-1.8 默认），感知更多细节，适合需要精细分析的场景
- `image_pixel_limit`：图片像素范围控制（可选）
  - `max_pixels`：图片最大像素值
  - `min_pixels`：图片最小像素值
  - 注：优先级高于 `detail` 参数

**Token 用量说明：**

图片理解的 Token 消耗根据图片像素计算：

- **doubao-seed-1.8 模型（detail 默认为 high）**：
  - 计算公式：`min(image_width × image_height ÷ 1764, max_image_tokens)`
  - detail=high 模式：像素区间 [1764, 9031680]，单图 token 范围 [1, 5120]
  - detail=low 模式：像素区间 [1764, 2139732]，单图 token 范围 [1, 1213]

**示例计算：**
- 图片尺寸 1280×720：`1280×720÷1764 = 522` tokens
- 图片尺寸 1920×1080：`1920×1080÷1764 = 1176` tokens

**注意**：单次请求传入图片数量受模型上下文窗口限制（256k tokens），过多图片可能导致信息截断或质量下降。

## 图片输入方式

### 1. 图片 URL 传入（推荐）

适用于图片已存在公网可访问 URL 的场景：

```python
{
    "type": "image_url",
    "image_url": {
        "url": "https://example.com/image.jpg",
        "detail": "high"  # 可选
    }
}
```

### 2. Base64 编码传入

适用于图片文件体积较小的场景（< 10MB）：

```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image("image.png")

{
    "type": "image_url",
    "image_url": {
        "url": f"data:image/png;base64,{base64_image}"
    }
}
```

### 3. 多图片输入

支持在一次请求中传入多张图片进行关联分析：

```python
messages=[{
    "role": "user",
    "content": [
        {"type": "image_url", "image_url": {"url": "https://example.com/image1.jpg"}},
        {"type": "image_url", "image_url": {"url": "https://example.com/image2.jpg"}},
        {"type": "text", "text": "对比这两张图片的差异"}
    ]
}]
```

### 4. 图文混排

灵活调整图片和文本的顺序，支持在 system 或 user 消息中混合：

```python
messages=[
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "这是目标人物"},
            {"type": "image_url", "image_url": {"url": "https://example.com/target.jpg"}},
            {"type": "text", "text": "请在后续图片中识别此人"}
        ]
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "图片1中是否包含目标人物？"},
            {"type": "image_url", "image_url": {"url": "https://example.com/scene1.jpg"}}
        ]
    }
]
```

### 5. 流式输出（高级）

使用流式输出可实时获取分析结果，避免长时间等待：

```python
from openai import OpenAI

client = OpenAI(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key=os.environ.get("ARK_API_KEY")
)

stream = client.chat.completions.create(
    model="doubao-seed-1-8-251228",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}},
            {"type": "text", "text": "详细分析这张图片"}
        ]
    }],
    stream=True,
    reasoning_effort="medium"
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

## 使用技巧

### 1. 选择合适的推理级别

根据任务复杂度选择推理级别：

- **简单任务**（minimal）：
  - 基础物体识别
  - 简单场景描述
  - 快速内容概览

- **中等任务**（low/medium）：
  - 场景理解和解释
  - 情感分析
  - 风格识别
  - 文字提取

- **复杂任务**（medium/high）：
  - 深度故事理解
  - 复杂推理和逻辑分析
  - 多图关联分析
  - 抽象概念理解

### 2. 编写有效的提示词

**好的提示词示例：**
- "请详细描述这张图片中的场景，包括人物、环境、动作和可能的背景故事"
- "分析这张照片的构图技巧，包括光影、色彩、视角等摄影元素的运用"
- "对比这两张图片在设计风格、色彩搭配和视觉冲击力方面的差异"
- "这张图片展示了什么技术概念？请解释其工作原理和应用场景"

**不够清晰的提示词：**
- "这是什么"（过于简单）
- "分析一下"（缺少具体方向）

### 3. 多图片分析技巧

当分析多张图片时：
- 明确说明图片之间的关系（对比、关联、序列等）
- 指出需要关注的重点
- 说明期望的分析深度

**示例：**
```
请对比分析这三张图片：
1. 第一张是原始设计图
2. 第二张是修改后的版本
3. 第三张是最终产品

请分析设计演进的过程、主要改动点和设计理念的体现
```

### 4. 控制图片理解精细度

根据场景选择合适的 `detail` 参数：

- **detail="low"**（低分辨率，快速）：
  - 简单物体识别
  - 场景大致描述
  - 快速浏览分析
  - 对速度要求高的场景

- **detail="high"**（高分辨率，详细）：
  - 文字识别（OCR）
  - 细节分析
  - 地图分析
  - 需要精细信息提取的场景

**示例代码：**
```python
{
    "type": "image_url",
    "image_url": {
        "url": "https://example.com/document.jpg",
        "detail": "high"  # 使用高分辨率以识别小字体
    }
}
```

### 5. 使用 image_pixel_limit 精细控制

当需要精确控制图片像素范围时，使用 `image_pixel_limit` 参数（优先级高于 detail）：

```python
{
    "type": "image_url",
    "image_url": {
        "url": "https://example.com/large_image.jpg",
        "image_pixel_limit": {
            "max_pixels": 3014080,  # 约等于 1920×1568
            "min_pixels": 3136      # 约等于 56×56
        }
    }
}
```

### 6. 图文顺序优化建议

在图文混排场景中：
- 系统会按顺序处理图片和文本
- 多图+一段文字时，建议将文字放在图片之后
- 如果结果不符合预期，可尝试调整图文顺序

**推荐顺序：**
```
[图片1] → [图片2] → [问题文本]
```

## 高级应用场景

### 场景 1：视觉定位（Visual Grounding）

识别图片中特定对象的位置和边界：

```python
messages=[{
    "role": "user",
    "content": [
        {"type": "image_url", "image_url": {"url": "https://example.com/scene.jpg"}},
        {"type": "text", "text": "请标出图片中所有的红色汽车，并给出它们的位置坐标"}
    ]
}]
```

### 场景 2：GUI 任务处理

分析界面截图，理解用户界面元素：

```python
messages=[{
    "role": "user",
    "content": [
        {"type": "image_url", "image_url": {"url": "https://example.com/screenshot.png"}},
        {"type": "text", "text": "分析这个应用界面，说明主要功能区域和用户操作流程"}
    ]
}]
```

### 场景 3：文档智能处理

从文档图片中提取结构化信息：

```python
messages=[{
    "role": "user",
    "content": [
        {"type": "image_url", "image_url": {"url": "https://example.com/invoice.jpg", "detail": "high"}},
        {"type": "text", "text": "提取这张发票中的关键信息：发票号码、日期、金额、购买方和销售方"}
    ]
}]
```

### 场景 4：多模态推理

结合多张图片进行复杂推理：

```python
messages=[{
    "role": "user",
    "content": [
        {"type": "image_url", "image_url": {"url": "https://example.com/image1.jpg"}},
        {"type": "image_url", "image_url": {"url": "https://example.com/image2.jpg"}},
        {"type": "image_url", "image_url": {"url": "https://example.com/image3.jpg"}},
        {"type": "text", "text": "这三张图片展示了一个时间序列的变化，请分析变化的趋势和可能的原因"}
    ]
}]
```

### 场景 5：创意设计分析

分析设计稿并提供改进建议：

```python
messages=[
    {
        "role": "system",
        "content": [{"type": "text", "text": "你是一个专业的设计顾问，擅长UI/UX设计分析"}]
    },
    {
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": "https://example.com/design.jpg"}},
            {"type": "text", "text": "分析这个移动应用的界面设计，从视觉层次、色彩搭配、交互设计等方面给出专业评价和改进建议"}
        ]
    }
]
```

## 维护与更新

### Python 环境准备

技能需要以下 Python 包：
- `volcengine-python-sdk[ark]`（用于 API 客户端）

如果遇到模块错误，告诉 AI：
```
请安装所需的 Python 依赖包
```

AI agent 会自动安装：`pip install 'volcengine-python-sdk[ark]'`

### 环境变量配置

为了方便使用，你可以将 ARK API Key 设置为环境变量：

```bash
export ARK_API_KEY="your_api_key_here"
```

这样在后续使用中就不需要每次都提供 API Key。

## 注意事项

- **API 密钥**：首次使用时，AI agent 会询问你的 ARK API 密钥。请确保密钥有效且有足够的配额。
- **网络连接**：分析图片需要网络连接到 `ark.cn-beijing.volces.com`
- **图片可访问性**：
  - URL 传入：确保图片 URL 公开可访问
  - 建议使用火山引擎 TOS（对象存储）存储图片，可利用内网通信降低延迟和流量费用
- **图片格式要求**：
  - 文件扩展名必须与实际图片格式一致
  - Base64 编码时需使用正确的 Content-Type（如 `image/jpeg`、`image/png` 等）
  - TIFF、SGI、ICNS、JPEG2000 格式需确保元数据对齐
- **内容政策**：确保图片和问题符合 API 的内容政策要求
- **推理成本**：
  - higher 推理级别会消耗更多 tokens
  - 图片尺寸越大，token 消耗越多
  - 根据实际需求选择合适的 `detail` 和 `reasoning_effort` 级别
- **上下文窗口限制**：
  - 模型支持 256k 上下文窗口
  - 单次请求图片数量受限于图片大小和上下文窗口
  - 过多图片可能导致信息截断或分析质量下降
- **输出长度**：模型最大支持 96k tokens 输出，对于非常复杂的分析，可能需要分段进行
- **数据隐私**：处理完图片后，文件会从方舟服务器删除，不会保留用户数据来训练模型
- **参数限制**：
  - 不支持 `frequency_penalty`（频率惩罚系数）
  - 不支持 `presence_penalty`（存在惩罚系数）
  - 不支持 `n`（单个请求生成多个返回）

## 常见问题

**Q: 如何选择合适的 detail 模式？**
A:
- 使用 `detail="low"`：快速分析、简单场景、对速度要求高
- 使用 `detail="high"`：文字识别、细节分析、高精度要求（默认）

**Q: 图片太大导致处理慢怎么办？**
A:
1. 使用 `detail="low"` 降低分辨率
2. 使用 `image_pixel_limit` 限制图片像素范围
3. 压缩图片后重试

**Q: 多张图片分析结果不准确？**
A:
1. 减少单次请求的图片数量
2. 调整图文顺序（建议图片在前，问题在后）
3. 使用更明确的提示词说明图片关系
4. 考虑分段分析而非一次请求

**Q: Base64 编码报错？**
A:
1. 确保单张图片 < 10MB
2. 确保请求体 < 64MB
3. 检查格式是否正确：`data:image/<format>;base64,<data>`
4. 考虑改用 URL 传入方式

**Q: 图片格式不支持？**
A:
1. 检查文件扩展名是否与实际格式一致
2. 确认格式在支持列表中
3. 转换为常见格式（JPEG、PNG）
4. 检查图片元数据是否正确设置

**Q: Token 消耗过快？**
A:
1. 降低图片分辨率（使用 `detail="low"`）
2. 使用 `image_pixel_limit` 限制像素
3. 减少单次请求的图片数量
4. 压缩图片尺寸
5. 选择较低的 `reasoning_effort` 级别

## 更多信息

详细的技术文档和使用说明请参考 `SKILL.md` 文件。

---

让 AI 帮你深入理解图片内容，发现视觉信息背后的故事和细节。

