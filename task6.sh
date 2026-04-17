source .venv/bin/activate


pytest task5.py

# return correct exit code
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi