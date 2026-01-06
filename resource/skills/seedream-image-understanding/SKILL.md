---
name: seedream-image-understanding
description: Analyze and understand images using the Doubao Seed 1.8 multimodal model with deep reasoning capabilities. Use this skill when users need to understand image content, extract text from images, compare multiple images, analyze visual elements, or answer questions about pictures. Supports various reasoning effort levels (minimal/low/medium/high) and handles single or multiple image analysis with text-image mixed layouts.
allowed-tools: Read, Bash(python:*)
---

# SeedDream Image Understanding

## Overview

This skill provides deep visual understanding using the Doubao Seed 1.8 multimodal deep reasoning model (model: `doubao-seed-1-8-251228`). It processes images through sophisticated reasoning to provide detailed analysis, text extraction, scene understanding, and answers complex visual questions.

**Key capabilities:**
- Single and multiple image analysis
- Text extraction (OCR) and detail recognition
- Deep reasoning with adjustable reasoning effort levels (minimal/low/medium/high)
- Various input methods (URL, Base64, local files)
- Flexible image-text mixed layouts
- Streaming output for real-time results

## When to Use This Skill

Use this skill when users request:
- "Analyze this image and describe what you see"
- "Extract text from this screenshot/photo"
- "Compare these two images and explain the differences"
- "What does this picture show?"
- "Read the contents of this document image"
- "Analyze the style/composition/colors of this photo"
- "Answer questions about what's in this image"
- Any request involving image understanding, visual analysis, OCR, or picture Q&A

## Quick Start

### Prerequisites

**IMPORTANT**: Always ask the user for their Volcano Engine ARK API key before proceeding:

> "To analyze images, I need your Volcano Engine ARK API key. You can find it at: https://console.volcengine.com/ark/region:ark+cn-beijing/apikey
>
> Please provide your ARK_API_KEY."

### Basic Workflow

1. Receive user request for image analysis
2. Request API key if not already provided
3. Clarify requirements (image URLs, task type, reasoning effort preference)
4. Execute analysis using the `image_understanding.py` script
5. Report results with detailed findings

## Using the Python Script

The `scripts/image_understanding.py` script provides a command-line interface for all image analysis tasks.

### Installation

First ensure the volcengine-python-sdk[ark] package is installed in your Python environment:

```bash
pip install 'volcengine-python-sdk[ark]'
```

### Basic Usage

```bash
# Basic image description
python scripts/image_understanding.py "Describe what you see" "https://example.com/image.jpg"

# With custom API key
python scripts/image_understanding.py "Analyze this image" "https://example.com/image.jpg" --api-key "YOUR_KEY"

# Using local file (will be encoded as Base64)
python scripts/image_understanding.py "What's in this image?" "local_image.png" --local

# Analyze multiple images in one shot
python scripts/image_understanding.py "What are the shooting angles of these photos?" "https://example.com/photo1.jpg" "https://example.com/photo2.jpg" "https://example.com/photo3.jpg"
```

### Advanced Options

```bash
# Extract text (OCR) - uses high detail mode automatically
python scripts/image_understanding.py --extract-text "https://example.com/document.jpg"

# Compare multiple images
python scripts/image_understanding.py --compare "https://example.com/before.jpg" "https://example.com/after.jpg"

# Visual/artistic analysis with high reasoning effort
python scripts/image_understanding.py --visual-analysis --reasoning-effort high "https://example.com/photo.jpg"

# Stream output in real-time for complex tasks
python scripts/image_understanding.py "Deep analysis" "https://example.com/complex.jpg" --stream --reasoning-effort high

# Use low detail for faster processing
python scripts/image_understanding.py "Quick overview" "https://example.com/image.jpg" --detail low
```

### Parameters

- `images`: Image URLs or local file paths (required)
- `prompt`: Analysis question or instruction (required unless using special modes)
- `--api-key`: Volcano Engine ARK API key
- `--reasoning-effort`: Reasoning depth (minimal/low/medium/high, default: medium)
- `--detail`: Image detail level (low/high, default: high)
- `--extract-text`: OCR mode - extracts all text from image
- `--compare`: Compare multiple images
- `--visual-analysis`: Analyze artistic/photographic elements
- `--local`: Treat input as local file paths (encodes as Base64)
- `--stream`: Stream output in real-time

## Python API Usage

For more complex use cases, you can use the Python API directly:

```python
from scripts.image_understanding import ImageUnderstanding

# Initialize client
analyzer = ImageUnderstanding(api_key="your_api_key")

# Basic analysis
result = analyzer.analyze_image(
    prompt="Describe this image in detail",
    image_urls=["https://example.com/photo.jpg"],
    reasoning_effort="medium"
)

# Text extraction (OCR)
text = analyzer.extract_text("https://example.com/document.jpg")

# Compare images
comparison = analyzer.compare_images([
    "https://example.com/before.jpg",
    "https://example.com/after.jpg"
])

# Visual elements analysis
visual = analyzer.analyze_visual_elements("https://example.com/artwork.jpg")

# With system context for target detection
result = analyzer.analyze_with_system_context(
    system_message="This is the target person",
    system_images=["https://example.com/target.jpg"],
    user_prompt="Is the target person in this scene?",
    user_images=["https://example.com/scene.jpg"]
)
```

## Choosing Reasoning Effort Level

**minimal** (no reasoning, fastest):
- Basic object identification
- Simple scene description
- Quick content overview

**low** (shallow reasoning):
- General scene understanding
- Basic emotion analysis
- Simple style recognition
- Standard OCR tasks

**medium** (moderate reasoning, recommended):
- Scene interpretation
- Content explanation
- Multi-element analysis
- Relationship understanding

**high** (deep reasoning):
- Complex story understanding
- Multi-image correlation
- Abstract concept interpretation
- Challenging logical analysis

## Choosing Detail Level

**detail="low"** (fast, less detail):
- Simple object recognition
- General scene description
- Quick overview tasks

**detail="high"** (slower, more detail - default):
- Text extraction (OCR)
- Fine detail analysis
- Map analysis
- Small text recognition

**Note**: Always use `detail="high"` for OCR tasks to ensure small text is readable.

## Image Requirements

**Supported formats:** JPEG, PNG, WebP, BMP, TIFF, GIF, ICO, DIB, ICNS, SGI, JPEG2000, HEIC, HEIF

**Size limitations:**
- URL input: < 10MB per image
- Base64 input: < 10MB per image, < 64MB total request
- File path input: < 512MB per image

**Pixel requirements:**
- Width > 14px and Height > 14px
- Width x Height range: [196px, 36,000,000px]

## Best Practices

1. **Always request API key first** - Don't assume the user has configured it
2. **Choose appropriate reasoning effort** - Match complexity to task requirements
3. **Use high detail for OCR** - Essential for reading small text
4. **Optimize image order** - Place text prompts after images in multi-image scenarios
5. **Consider streaming for complex tasks** - Provides real-time feedback
6. **Validate image accessibility** - Ensure URLs are publicly accessible before analysis
7. **Handle token limits** - Be mindful of context window (256k) with multiple images
8. **Specify analysis focus** - Guide the model with clear, specific prompts
9. **Use system messages for context** - Set role/context in system messages when appropriate
10. **Test with minimal reasoning first** - Escalate to higher levels if needed

## Troubleshooting

**"ARK API key is required"**
- Ensure the user has provided their API key
- Verify the key is passed correctly via environment variable or parameter

**"Image URL not accessible"**
- Check URL is publicly accessible
- Verify URL format is correct (http/https)
- Consider using Base64 encoding for local files
- For production, use Volcano Engine TOS for better performance

**"Cannot read text from image"**
- Ensure `detail="high"` is set (used automatically in --extract-text mode)
- Check image resolution is sufficient
- Verify text is legible in the original image

**"Analysis takes too long"**
- Use lower `reasoning-effort` (minimal or low)
- Enable streaming output for real-time feedback
- Use `--detail low` if high precision isn't needed

**"Image format not supported"**
- Verify file extension matches actual format
- Convert to common format (JPEG, PNG)
- Check MIME type is correct for Base64 encoding
