from pathlib import Path

path = Path("Ecommerce")

# path.mkdir()  # Create a directory
# path.rmdir()  # Remove a directory
# path.rename("Ecommerce2")  # Rename a directory
# path.exists()  # Check if directory exists
# path.is_dir()  # Check if directory is a directory
# path.is_file()  # Check if directory is a file
# path.is_absolute()  # Check if directory is an absolute path


path = Path("Ecommerce")

print(path.iterdir())  # Iterate through the directory

for p in path.iterdir():
    print(p)  # return the path of the file or directory

[p for p in path.iterdir()]  # return the paths of the files
[p.name for p in path.iterdir()]  # return the names of the files

# return the paths of the files with the extension .py (glob is a method that returns a generator)
path.glob("*.py")
[p for p in path.glob("*.py")]
# return the paths of the files with the extension .py in the subdirectories. rglob search recursively. ** means all subdirectories.
[p for p in path.rglob("**/*.py")]
