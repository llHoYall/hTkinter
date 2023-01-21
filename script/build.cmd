@ECHO Off
call ./.venv/Scripts/activate
pyinstaller -y spec/hTkinter_windows.spec
call deactivate