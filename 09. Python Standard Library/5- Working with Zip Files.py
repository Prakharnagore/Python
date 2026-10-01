from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zipFile:
    for path in Path("ecommerce").rglob("*.*"):
        zipFile.write(path)

with ZipFile("files.zip", "r") as zipFile:
    print(zipFile.namelist())
    info = zipFile.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zipFile.extractall("extract")
