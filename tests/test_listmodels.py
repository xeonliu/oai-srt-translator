import os

import srt_translator as gst

gst.api_key = os.getenv("API_KEY", "")

gst.listmodels()
