#!/usr/bin/env python3
"""
SeedDream Image Understanding Script

Analyzes images using the Doubao Seed 1.8 multimodal model with deep reasoning capabilities.
Supports various analysis tasks including description, OCR, comparison, and complex reasoning.
"""

import os
import sys
import base64
import argparse
from typing import Optional, List
from volcenginesdkarkruntime import Ark


class ImageUnderstanding:
    """Image understanding client using Doubao Seed 1.8 model."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the image understanding client.

        Args:
            api_key: Volcano Engine ARK API key. If None, reads from ARK_API_KEY env variable.
        """
        self.api_key = api_key or os.environ.get("ARK_API_KEY")
        if not self.api_key:
            raise ValueError("ARK_API_KEY is required. Provide it via --api-key or ARK_API_KEY environment variable.")

        self.client = Ark(
            base_url='https://ark.cn-beijing.volces.com/api/v3',
            api_key=self.api_key
        )
        self.model = "doubao-seed-1-8-251228"

    def encode_image(self, image_path: str) -> str:
        """Encode an image file to Base64.

        Args:
            image_path: Path to the image file

        Returns:
            Base64-encoded image string
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_image(
        self,
        prompt: str,
        image_urls: List[str],
        reasoning_effort: str = "medium",
        detail: str = "high",
        stream: bool = False
    ) -> str:
        """Analyze one or more images with a text prompt.

        Args:
            prompt: Analysis question or instruction
            image_urls: List of image URLs (can be http URLs or data URLs)
            reasoning_effort: Reasoning depth (minimal/low/medium/high)
            detail: Image detail level (low/high)
            stream: Whether to stream the response

        Returns:
            Analysis result text
        """
        content = []

        # Add images
        for url in image_urls:
            content.append({
                "type": "image_url",
                "image_url": {"url": url, "detail": detail}
            })

        # Add text prompt
        content.append({
            "type": "text",
            "text": prompt
        })

        messages = [{
            "role": "user",
            "content": content
        }]

        if stream:
            result = []
            stream_response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                reasoning_effort=reasoning_effort,
                stream=True
            )
            for chunk in stream_response:
                if chunk.choices[0].delta.content:
                    content_chunk = chunk.choices[0].delta.content or ""
                    print(content_chunk, end="", flush=True)
                    result.append(content_chunk)
            return "".join(result)
        else:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                reasoning_effort=reasoning_effort
            )
            return response.choices[0].message.content or ""

    def analyze_with_system_context(
        self,
        system_message: str,
        system_images: List[str],
        user_prompt: str,
        user_images: List[str],
        reasoning_effort: str = "medium",
        detail: str = "high"
    ) -> str:
        """Analyze images with system and user message structure.

        Args:
            system_message: System context message
            system_images: Images to include in system message
            user_prompt: User question
            user_images: Images to include in user message
            reasoning_effort: Reasoning depth (minimal/low/medium/high)
            detail: Image detail level (low/high)

        Returns:
            Analysis result text
        """
        messages = []

        # Build system message
        system_content = [{"type": "text", "text": system_message}]
        for url in system_images:
            system_content.append({
                "type": "image_url",
                "image_url": {"url": url, "detail": detail}
            })

        messages.append({
            "role": "system",
            "content": system_content
        })

        # Build user message
        user_content = [{"type": "text", "text": user_prompt}]
        for url in user_images:
            user_content.append({
                "type": "image_url",
                "image_url": {"url": url, "detail": detail}
            })

        messages.append({
            "role": "user",
            "content": user_content
        })

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            reasoning_effort=reasoning_effort
        )
        return response.choices[0].message.content

    def extract_text(self, image_url: str) -> str:
        """Extract text from an image (OCR).

        Args:
            image_url: URL of the image containing text

        Returns:
            Extracted text content
        """
        return self.analyze_image(
            prompt="Extract all text content from this image, preserving the original format and structure.",
            image_urls=[image_url],
            reasoning_effort="low",  # Low is sufficient for OCR
            detail="high"  # High detail required for OCR
        )

    def compare_images(self, image_urls: List[str], prompt: Optional[str] = None) -> str:
        """Compare multiple images and identify differences.

        Args:
            image_urls: List of image URLs to compare
            prompt: Custom comparison prompt (optional)

        Returns:
            Comparison analysis
        """
        if prompt is None:
            prompt = "Compare these images in detail, explaining their differences and relationships."

        return self.analyze_image(
            prompt=prompt,
            image_urls=image_urls,
            reasoning_effort="medium"
        )

    def analyze_visual_elements(self, image_url: str) -> str:
        """Analyze artistic, design, or photographic elements.

        Args:
            image_url: URL of the image to analyze

        Returns:
            Visual element analysis
        """
        prompt = """Analyze this image from an artistic/photographic perspective, including:
        - Composition techniques
        - Lighting and shadows
        - Color palette and usage
        - Perspective and framing
        - Depth of field
        - Visual style and mood
        - Key elements and their relationships"""

        return self.analyze_image(
            prompt=prompt,
            image_urls=[image_url],
            reasoning_effort="high"  # High for complex artistic analysis
        )


def main():
    """Command-line interface for image understanding."""
    parser = argparse.ArgumentParser(
        description="Analyze images using Doubao Seed 1.8 multimodal model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic description
  %(prog)s "Describe what you see" "https://example.com/image.jpg"

  # OCR text extraction
  %(prog)s --extract-text "https://example.com/document.jpg"

  # Compare images
  %(prog)s --compare "https://example.com/before.jpg" "https://example.com/after.jpg"

  # Visual analysis
  %(prog)s --visual-analysis "https://example.com/photo.jpg"

  # Local file with Base64
  %(prog)s "Analyze this image" "local_image.png" --local
        """
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        help="Analysis question or instruction"
    )

    parser.add_argument(
        "images",
        nargs="+",
        help="Image URLs or local file paths"
    )

    parser.add_argument(
        "--api-key",
        help="Volcano Engine ARK API key (or set ARK_API_KEY env variable)"
    )

    parser.add_argument(
        "--reasoning-effort",
        choices=["minimal", "low", "medium", "high"],
        default="medium",
        help="Reasoning depth level (default: medium)"
    )

    parser.add_argument(
        "--detail",
        choices=["low", "high"],
        default="high",
        help="Image detail level (default: high)"
    )

    parser.add_argument(
        "--extract-text",
        action="store_true",
        help="Extract text from images (OCR mode)"
    )

    parser.add_argument(
        "--compare",
        action="store_true",
        help="Compare multiple images"
    )

    parser.add_argument(
        "--visual-analysis",
        action="store_true",
        help="Analyze visual/artistic elements"
    )

    parser.add_argument(
        "--local",
        action="store_true",
        help="Treat input as local file paths (will encode as Base64)"
    )

    parser.add_argument(
        "--stream",
        action="store_true",
        help="Stream output in real-time"
    )

    args = parser.parse_args()

    # Initialize client
    try:
        analyzer = ImageUnderstanding(api_key=args.api_key)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Process images
    image_urls = []
    if args.local:
        # Convert local files to Base64 data URLs
        for image_path in args.images:
            if not os.path.exists(image_path):
                print(f"Error: File not found: {image_path}", file=sys.stderr)
                sys.exit(1)

            # Detect file type for MIME type
            ext = os.path.splitext(image_path)[1].lower().lstrip('.')
            mime_type = f"image/{ext}" if ext in ['png', 'jpeg', 'jpg', 'gif', 'webp', 'bmp', 'tiff', 'tif'] else 'image/png'

            base64_data = analyzer.encode_image(image_path)
            data_url = f"data:{mime_type};base64,{base64_data}"
            image_urls.append(data_url)
    else:
        image_urls = args.images

    # Execute analysis
    try:
        if args.extract_text:
            if len(image_urls) != 1:
                print("Error: --extract-text requires exactly one image", file=sys.stderr)
                sys.exit(1)
            result = analyzer.extract_text(image_urls[0])
        elif args.compare:
            if len(image_urls) < 2:
                print("Error: --compare requires at least two images", file=sys.stderr)
                sys.exit(1)
            result = analyzer.compare_images(image_urls, args.prompt)
        elif args.visual_analysis:
            if len(image_urls) != 1:
                print("Error: --visual-analysis requires exactly one image", file=sys.stderr)
                sys.exit(1)
            result = analyzer.analyze_visual_elements(image_urls[0])
        else:
            if not args.prompt:
                print("Error: prompt is required unless using --extract-text, --compare, or --visual-analysis",
                      file=sys.stderr)
                sys.exit(1)
            result = analyzer.analyze_image(
                prompt=args.prompt,
                image_urls=image_urls,
                reasoning_effort=args.reasoning_effort,
                detail=args.detail,
                stream=args.stream
            )

        if not args.stream:
            print(result)

    except Exception as e:
        print(f"Error during analysis: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
