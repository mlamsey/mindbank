# Mindbank

Store and compress your train of thought. This project combines [OpenAI Whisper](https://github.com/openai/whisper) with ChatGPT's summarizing capabilities to summarize spoken word.

# Installation

1. Tested with Python 3.10. Using a Conda environment is recommended: `conda create -n mindbank python=3.10`

1. `cd` into the repo's root directory (`/mindbank/`) and install python packages: `pip install -r requirements.txt`

1. Install the package: `pip install .`

1. Install ffmpeg:

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

# Usage

First, generate an OpenAI token: https://platform.openai.com/

`python mindbank --token <path_to_api_token>`
