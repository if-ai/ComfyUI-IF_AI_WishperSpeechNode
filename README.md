# ComfyUI-IF_AI_WishperSpeechNode
A convenient fast Text to Speech Whisper Speech by Collabora you can train a voice on the fly on ComfyUI

Enable torch_Compile for faster inference and training but I dont know the right Pytorch 
so I dissable it by default 

You can place a 10min OOG recording on the Audio folder to train your voice on the fly

pip install -r requirements.txt 

or double click the bat if you are on win portable

DEDICATED ENV

Activate the env

on conda env
conda install -c conda-forge dlib

on micromamba env
micromamba install -c conda-forge dlib

open terminal as admin

pip uninstall cmake
pip uninstall dlib
WINDOWS

H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install cmake
H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install dlib
or activate env

python -m -m pip install cmake
python -m pip install dlib
if not try with the terminal as admin

pip uninstall cmake
pip uninstall dlib
pip install cmake
git clone https://github.com/davisking/dlib.git
cd dlib
H:\ComfyUI_windows_portable\python_embeded\python.exe setup.py install
