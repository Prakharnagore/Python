import subprocess


completed = subprocess.run(["ls", "-l"])
print(completed.args)  # ['ls', '-l']
print(completed.returncode)  # 0
print(completed.stderr)  # None
print(completed.stdout)  # None


# capture the output of the command ls -l and return the output
completed = subprocess.run(["ls", "-l"], capture_output=True)
print(completed.args)  # ['ls', '-l']
print(completed.returncode)  # 0 -> any non-zero value is an error
print(completed.stderr)  # None
# b'total 12\n-rw-r--r-- 1 john john 1234 Sep 26 12:34 file1.txt\n-rw-r--r-- 1 john john 1234 Sep 26 12:34 file2.txt\n'
print(completed.stdout)


# capture the output of the command ls -l and return the output
completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(completed.args)  # ['ls', '-l']
print(completed.returncode)  # 0
print(completed.stderr)  # None

# total 12
# -rw-r--r-- 1 john john 1234 Sep 26 12:34 file1.txt
print(completed.stdout)


completed = subprocess.run(["python", "script.py"],
                           capture_output=True, text=True)
print(completed.args)  # ['python', 'script.py']
print(completed.returncode)  # 0
print(completed.stderr)  # None
print(completed.stdout)  # Hello, World!


completed = subprocess.run(["false"],
                           capture_output=True,
                           text=True
                           )
print(completed.args)  # ['false']
print(completed.returncode)  # 1 -> any non-zero value is an error
print(completed.stderr)  # None
print(completed.stdout)  # None


if completed.returncode != 0:
    print(completed.stderr)


try:
    completed = subprocess.run(["false"],
                               capture_output=True,
                               text=True,
                               check=True)
except subprocess.CalledProcessError as e:
    print(e.returncode)
    print(e.stderr)
    print(e.stdout)
