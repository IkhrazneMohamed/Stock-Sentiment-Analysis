#!/usr/bin/env bash

pip install -r requirements.txt

# shellcheck disable=SC2164
cd ~

mkdir driver

wget -o ~/driver/chromedriver.zip https://chromedriver.storage.googleapis.com/108.0.5359.22/chromedriver_win32.zip

unzip chromedriver.zip

