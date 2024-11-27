import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7481226930:AAFpsEUkjpHA9bUhEsMBvvFZTubjdcsK3Ys")

    APP_ID = int(os.environ.get("APP_ID", 27317669))

    API_HASH = os.environ.get("API_HASH", "11b88c331c5d44fde57cf91de1a2156b")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")
