from pathlib import Path
from time import ctime
from shutil import copy

path = Path("Ecommerce/__init__.py")

path.exists()  # Check if file exists
path.rename("Ecommerce/init.py")  # Rename file
path.unlink()  # Delete file

print(path.stat())  # Return the stat of the file
print(ctime(path.stat().st_ctime))  # Return the creation time of the file

path.read_bytes()  # Return the bytes of the file
path.read_text()  # Return the text of the file
path.write_text("print('Hello, World!')")  # Write text to file
path.write_bytes(b"print('Hello, World!')")  # Write bytes to file


# Copy file to another file
source = Path("Ecommerce/__init__.py")
target = Path("Ecommerce/init.py")

target.write_text(source.read_text())  # Copy file
target.write_bytes(source.read_bytes())  # Copy file


# Better way to copy file
copy(source, target)
