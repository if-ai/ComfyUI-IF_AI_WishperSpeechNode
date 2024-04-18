import os
import importlib.util
import glob
import shutil
from .IFWhisperSpeechNode import IFWhisperSpeech   

NODE_CLASS_MAPPINGS = {
    "IF_WhisperSpeech": IFWhisperSpeech,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IF_WhisperSpeech": "IF Whisper Speech🌬️",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
