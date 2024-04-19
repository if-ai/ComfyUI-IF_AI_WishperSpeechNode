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
1-.VIA PIP
activate env
  ```bash
  pip install cmake
  pip install dlib
  
  ```
2-. VIA CLONING DLIB REPO
  ```
    git clone https://github.com/davisking/dlib.git
    cd dlib
  ```
  activate env
  ```
      python.exe setup.py install
  ```

if nothing works try this with the terminal as admin
3-.VIA CONDA PKG

1-.Activate the env
on conda env
`conda install -c conda-forge dlib`
on micromamba env
`micromamba install -c conda-forge dlib`

#### Portable ENV
1-.VIA PIP

  Open terminal as admin
    ```
   H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install cmake
   H:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install dlib
    ```
    
2-. VIA CLONING DLIB REPO
    ```
    git clone https://github.com/davisking/dlib.git
    cd dlib
    H:\ComfyUI_windows_portable\python_embeded\python.exe setup.py install
    ```






   


