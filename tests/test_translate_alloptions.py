import os

import srt_translator as gst

gst.api_key = os.getenv("API_KEY", "")
gst.api_key2 = os.getenv("API_KEY2", "")
gst.target_language = "French"
gst.input_file = "subtitle.srt"
gst.output_file = "translated_subtitle.srt"
gst.description = "This is a medical TV Show"
gst.model_name = "gpt-4o"
gst.start_line = 1
gst.batch_size = 30
gst.free_quota = True
gst.skip_upgrade = True
gst.use_colors = True

gst.translate()
