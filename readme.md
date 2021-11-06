# VOICEVIM

Just an attempt to use voice commands to code.

## Goal:
Use voice commands to code (starting with python code).
To get together:  
* neovim
* language-server-protocol(lsp)
* natural language processing (NLP)

## Usage:
* Install dependencies:
```sh
cat runtime.txt | xargs sudo apt install -y
```
Open neovim in a terminal with the following command:
```sh
NVIM_LISTEN_ADDRESS=/tmp/nvim nvim
```
And then run 
```sh
python friday.py
```
Finally say "Friday, define function" until she want to obey

## TODO
***If you don't like TODO's in readme, fix it!***
* Open terminal and execute neovim
* Find smarter way to send keys to neovim client
