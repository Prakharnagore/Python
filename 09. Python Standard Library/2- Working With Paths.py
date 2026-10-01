# Link - https://docs.python.org/3/library/pathlib.html

from pathlib import Path

Path("C://Program Files/Microsoft")

# Use raw string 'r' to avoid escape characters(i.e double backslash)
Path(r"C:\Program Files\Microsoft")

Path("/user/local/bin/")

# Current working directory
Path()

# Find file inside a directory
Path("Ecommerce/__init__.py")

# Join paths
# Path() / "Ecommerce" / "__init__.py"

# Home directory
Path.home()


path = Path("Ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)  # File name
print(path.stem)  # File name without extension
print(path.suffix)  # File extension
print(path.parent)  # Parent directory
path.with_name("files.txt")  # return the new path
path.absolute()  # return the absolute path
path.with_suffix(".txt")  # return the new path with a new suffix
