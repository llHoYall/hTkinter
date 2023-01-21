#!/bin/sh
. ./.venv/bin/activate
pyinstaller -y spec/hTkinter_macos.spec
deactivate