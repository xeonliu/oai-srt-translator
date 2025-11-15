# 🌟 SRT Translator (OpenAI Compatible)

[![PyPI version](https://img.shields.io/pypi/v/srt-translator)](https://pypi.org/project/srt-translator)
[![Python support](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FMaKTaiL%2Fgemini-srt-translator%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&color=red)](https://pypi.org/project/srt-translator)
[![Downloads](https://img.shields.io/pypi/dw/srt-translator)](https://pypi.org/project/srt-translator)
[![GitHub contributors](https://img.shields.io/github/contributors/MaKTaiL/gemini-srt-translator)](https://github.com/MaKTaiL/gemini-srt-translator/graphs/contributors)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/maktail)

> Translate SRT subtitle files using OpenAI Compatible API! 🚀

---

## ✨ Overview

**SRT Translator** is a powerful python tool to translate subtitle files using OpenAI Compatible API. Perfect for anyone needing fast, accurate, and customizable translations for videos, movies, and series. Works with any OpenAI-compatible API endpoint!

---

- 🔤 **SRT Translation**: Translate `.srt` subtitle files to a wide range of languages using OpenAI Compatible API.
- ⏱️ **Timing & Format**: Ensures that the translated subtitles maintain the exact timestamps and basic SRT formatting of the original file.
- 💾 **Quick Resume**: Easily resume interrupted translations from where you left off.
- 🧠 **Advanced AI**: Leverages thinking and reasoning capabilities for more contextually accurate translations.
- 🖥️ **CLI Support**: Full command-line interface for easy automation and scripting.
- ⚙️ **Customizable**: Tune model parameters, adjust batch size, and access other advanced settings.
- 🌐 **Custom API Endpoints**: Support for custom OpenAI-compatible API endpoints.
- 🎞️ **SRT Extraction**: Extract and translate SRT subtitles from video files automatically (requires [FFmpeg](https://ffmpeg.org/)).
- 🎵 **Audio Context**: Extract audio from a video file or provide your own to improve translation accuracy (requires [FFmpeg](https://ffmpeg.org/)).
- 📜 **Description Support**: Add a description to your translation job to guide the AI in using specific terminology or context.
- 📋 **List Models**: Easily list all currently available models from your API endpoint.
- 🔄 **Auto-Update**: Keep the tool updated with automatic version checking and update prompts.
- 📝 **Logging**: Optional saving of progress and 'thinking' process logs for review.

---

## 📦 Installation

### Basic:

```sh
pip install --upgrade srt-translator
```

### Recommended: Use a Virtual Environment

It's best practice to use a virtual environment. This is especially recommended as srt-translator installs several dependencies that could potentially conflict with your existing packages:

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install inside the virtual environment
pip install --upgrade srt-translator
```

---

## 🔑 How to Get Your API Key

This tool works with any OpenAI Compatible API. You can use:

- **OpenAI API**: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Other OpenAI Compatible Services**: Any service that provides OpenAI-compatible API endpoints (e.g., local models, cloud providers, etc.)

### 🔐 Setting Your API Key and Endpoint

You can provide your API key and endpoint in several ways:

1. **Environment Variable (Recommended)**: Set the `API_KEY` and optionally `API_ENDPOINT` environment variables. This is the most secure and recommended method.

- **macOS/Linux:**

  ```bash
  export API_KEY="your_api_key_here"
  export API_ENDPOINT="https://api.openai.com/v1"  # Optional: defaults to OpenAI if not set
  export API_KEY2="your_second_api_key_here"  # Optional: for additional quota
  ```

- **Windows (Command Prompt):**

  ```cmd
  set API_KEY=your_api_key_here
  set API_ENDPOINT=https://api.openai.com/v1
  set API_KEY2=your_second_api_key_here
  ```

- **Windows (PowerShell):**
  ```powershell
  $env:API_KEY="your_api_key_here"
  $env:API_ENDPOINT="https://api.openai.com/v1"  # Optional
  $env:API_KEY2="your_second_api_key_here"  # Optional for additional quota
  ```

2. **Command Line Argument**: Use the `-k` or `--api-key` flag and optionally `--api-endpoint`

   ```bash
   # Using OpenAI API (default endpoint)
   gst translate -i subtitle.srt -l French -k YOUR_API_KEY
   
   # Using custom endpoint
   gst translate -i subtitle.srt -l French -k YOUR_API_KEY --api-endpoint https://your-api.com/v1
   ```

3. **Interactive Prompt**: The tool will prompt you if no key is found

   ```bash
   gst translate -i subtitle.srt -l French
   ```

4. **Python API**: Set the `api_key` and optionally `api_endpoint` variables in your script

   ```python
   import srt_translator as gst
   gst.api_key = "your_api_key_here"
   gst.api_endpoint = "https://api.openai.com/v1"  # Optional
   ```

---

## 🚀 Quick Start

### 🖥️ Using the Command Line Interface (CLI)

#### Basic Translation

```bash
# Using environment variable (recommended)
export API_KEY="your_api_key_here"
export API_ENDPOINT="https://api.openai.com/v1"  # Optional
gst translate -i subtitle.srt -l French

# Using command line argument
gst translate -i subtitle.srt -l French -k YOUR_API_KEY

# Using custom API endpoint
gst translate -i subtitle.srt -l French -k YOUR_API_KEY --api-endpoint https://your-api.com/v1

# Set output file name
gst translate -i subtitle.srt -l French -o translated_subtitle.srt

# Extract subtitles from video and translate (requires FFmpeg)
gst translate -v movie.mp4 -l Spanish

# Extract and use audio from video for context (requires FFmpeg)
gst translate -v movie.mp4 -l Spanish --extract-audio

# Interactive model selection
gst translate -i subtitle.srt -l "Brazilian Portuguese" --interactive

# Resume translation from a specific line
gst translate -i subtitle.srt -l French --start-line 20

# Suppress output
gst translate -i subtitle.srt -l French --quiet
```

#### Advanced Options

```bash
# Full-featured translation with custom settings
gst translate \
  -i input.srt \
  -v video.mp4 \
  -l French \
  -k YOUR_API_KEY \
  --api-endpoint https://api.openai.com/v1 \
  -k2 YOUR_SECOND_API_KEY \
  -o output_french.srt \
  --model gpt-4o \
  --batch-size 150 \
  --temperature 0.7 \
  --description "Medical TV series, use medical terminology" \
  --progress-log \
  --thoughts-log \
  --extract-audio \
```

#### CLI Help

```bash
# Show all available commands and options
gst --help

# Show specific command help
gst translate --help
```

### 🐍 Using Python API

#### Translating an SRT file

```python
import srt_translator as gst

gst.api_key = "your_api_key_here"
gst.target_language = "French"
gst.input_file = "subtitle.srt"

gst.translate()
```

#### Resuming an Interrupted Translation

Just run again with the same parameters, or specify the start line:

```python
import srt_translator as gst

gst.api_key = "your_api_key_here"
gst.target_language = "French"
gst.input_file = "subtitle.srt"
gst.start_line = 20

gst.translate()
```

---

## ⚙️ Advanced Configuration

#### 🔧 GST Parameters

- `api_endpoint`: API endpoint URL for OpenAI compatible backends (default: None, uses OpenAI if not set).
- `api_key2`: Second key for more quota (useful for additional API quota).
- `video_file`: Path to a video file to extract subtitles and/or audio for context (requires [FFmpeg](https://ffmpeg.org/)).
- `audio_file`: Path to an audio file to use as context for translation (requires [FFmpeg](https://ffmpeg.org/)).
- `extract_audio`: Whether to extract and use audio context from the video file (default: False).
- `output_file`: Name of the translated file.
- `start_line`: Starting line for translation.
- `description`: Description of the translation job.
- `batch_size`: Batch size (default: 300).
- `free_quota`: Signal GST that you are using a free quota (default: True).
- `skip_upgrade`: Skip version upgrade check (default: False).
- `use_colors`: Activate colors in terminal (default: True).
- `progress_log`: Enable progress logging to a file (default: False).
- `thoughts_log`: Enable logging of the 'thinking' process to a file (default: False).
- `quiet_mode`: Suppress all output (default: False).
- `resume`: Skip prompt and set automatic resume mode.

#### 🔬 Model Tuning Parameters

- `model_name`: Model name to use (default: "gpt-4o"). Works with any OpenAI compatible model.
- `temperature`: Controls randomness in output. Lower for more deterministic, higher for more creative (range: 0.0-2.0).
- `top_p`: Nucleus sampling parameter (range: 0.0-1.0).
- `top_k`: Top-k sampling parameter (range: >=0). Note: Not all models support this parameter.
- `streaming`: Enable streamed responses (default: True).
  - Set to `False` for bad internet connections or when using slower models.
- `thinking`: Enable thinking capability for potentially more accurate translations (default: True).
  - Depends on model support.
- `thinking_budget`: Token budget for the thinking process (default: 2048, range: 0-24576, 0 also disables thinking).
  - Depends on model support.

---

##   Prompt Design & Customization

###  🔧 Core Translation Prompt
The tool uses a sophisticated prompt system to ensure high-quality translations:

```python
# Example of the generated instruction
instruction = get_instruction(
    language="French",
    thinking=True,
    thinking_compatible=True,
    audio_file="movie_audio.mp3",
    description="Medical drama series, use appropriate medical terminology"
)
```

###   Advanced Features

#### Thinking & Reasoning
- **Enabled by default** for more contextually accurate translations
- **Token budget**: Configurable thinking budget (default: 2048 tokens)
- **Language-specific grammar**: Applies gender agreement rules based on audio analysis

#### Audio Context Integration
When audio files are provided, the prompt includes:
- **Speaker gender detection** from voice characteristics
- **Grammatical gender rules** for target language
- **Context-aware addressing** (speaker to male/female/group)

#### Custom Instructions
Use the `description` parameter to provide specific context:
- **Domain-specific terminology** (medical, legal, technical)
- **Style preferences** (formal, informal, regional dialects)
- **Content-specific guidance** (character names, technical terms, cultural references)

###  📋 Response Schema
The tool enforces structured output using OpenAI JSON Schema:

```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "index": {"type": "string"},
      "content": {"type": "string"}
  },
  "required": ["index", "content"]
}
```

####  💡 Full example:

```python
import srt_translator as gst

gst.api_key = "your_api_key_here"
gst.api_endpoint = "https://api.openai.com/v1"  # Optional: for custom endpoints
gst.api_key2 = "your_api_key2_here"
gst.target_language = "French"
gst.input_file = "subtitle.srt"
gst.output_file = "subtitle_translated.srt"
gst.video_file = "video.mp4"
gst.audio_file = "audio.mp3"
gst.extract_audio = False
gst.start_line = 20
gst.description = "Medical TV series, use medical terms"
gst.model_name = "gpt-4o"
gst.batch_size = 150
gst.streaming = True
gst.thinking = True
gst.thinking_budget = 4096
gst.temperature = 0.7
gst.top_p = 0.95
gst.top_k = 20
gst.free_quota = False
gst.skip_upgrade = True
gst.use_colors = False
gst.progress_log = True
gst.thoughts_log = True
gst.quiet_mode = False
gst.resume = True

gst.translate()
```

---

## 📚 Listing Available Models

### CLI

```bash
# List models from default endpoint (OpenAI)
gst list-models -k YOUR_API_KEY

# List models from custom endpoint
gst list-models -k YOUR_API_KEY --api-endpoint https://your-api.com/v1
```

### Python API

```python
import srt_translator as gst

gst.api_key = "your_api_key_here"
gst.api_endpoint = "https://api.openai.com/v1"  # Optional
gst.listmodels()
```

---

## 🎨 Unofficial GUI Applications

If you prefer a user-friendly graphical interface over command-line usage, be sure to check out:

- **[🔗 SRT Translator GUI](https://github.com/mkaflowski/Gemini-SRT-translator-GUI) (by @mkaflowski)**
- **[🔗 SRT Translator GUI](https://github.com/dane-9/gemini-srt-translator-gui) (by @dane-9)**

Perfect for users who want the same powerful translation capabilities with an intuitive visual interface!

---

## 📝 License

Distributed under the MIT License. See the [LICENSE](https://github.com/MaKTaiL/srt-translator?tab=MIT-1-ov-file) file for details.

---

## 👥 Contributors

Thank you to all who have contributed to this project:

- [MaKTaiL](https://github.com/MaKTaiL) - Creator and maintainer
- [CevreMuhendisi](https://github.com/CevreMuhendisi)
- [angelitto2005](https://github.com/angelitto2005)
- [sjiampojamarn](https://github.com/sjiampojamarn)
- [mkaflowski](https://github.com/mkaflowski)

Special thanks to all users who have reported issues, suggested features, and helped improve the project.
