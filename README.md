# ComfyUI-IF_AI_WishperSpeechNode
# A Convenient and Fast Text-to-Speech Application with Whisper Speech

This repository hosts a Text-to-Speech (TTS) application that leverages Whisper Speech for voice synthesis, allowing users to train a voice model on-the-fly. It is built on ComfyUI and supports rapid training and inference processes.

## Features
- **On-the-fly Voice Training:** Train a custom voice model using a short audio recording.
- **Fast Inference:** Optional support for `torch_Compile` to enhance performance during inference and training.

## Installation
- Git clone the repository to your custom_nodes folder 
- pip install -r requirements.txt


### IF dlib troubles try this workarounds

#### DEDICATED ENV
activate env
  ```bash
  python -m pip install cmake
  python -m pip install dlib
  
  ```
CLONING dlib repo
  ```
    git clone https://github.com/davisking/dlib.git
    cd dlib
  ```
  activate env
  ```
      python.exe setup.py install
  ```
if not try with the terminal as admin

1-.Activate the env
on conda env
`conda install -c conda-forge dlib`
on micromamba env
`micromamba install -c conda-forge dlib`

#### Portable ENV
  VIA pip
  open terminal as admin
    ```
   H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install cmake
   H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install dlib
    ```
    
  CLONING dlib repo
    ```
    git clone https://github.com/davisking/dlib.git
    cd dlib
    H:\ComfyUI_windows_portable\python_embeded\python.exe setup.py install
    ```






   


