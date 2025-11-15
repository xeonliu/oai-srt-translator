import os

import srt_translator as gst

gst.api_key = os.getenv("API_KEY", "")
gst.target_language = "French"
gst.input_file = "subtitle.srt"

gst.translate()
