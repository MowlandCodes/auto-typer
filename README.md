# Auto-Typer

## Requirements

- Python 3.x
- Your user must be inside the `input` group to allow the script to read keyboard input events. You can add your user to the `input` group with the following command:

```bash
sudo usermod -aG input $USER # Sign out and back in for the changes to take effect

# or run in the same session to apply the changes immediately
newgrp input
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MowlandCodes/auto-typer
```

2. Navigate to the project directory:

```bash
cd auto-typer
```

3. Install the required dependencies:

```bash
# If you have uv installed, you can use uv to install the dependencies
uv sync

# Or just use pip to install the dependencies
pip install -r requirements.txt
```

4. Use the library in your own Python scripts or run the example script provided in `main.py` to see how it works.

### Example Usage

```python
from typer import type_text

type_text("Hello, World!", delay=0.1)  # Types "Hello, World!" with a 0.1 second delay between each character
```
