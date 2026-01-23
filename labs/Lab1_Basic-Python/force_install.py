import os
import subprocess
import sys

def find_python_executables():
    found = []
    # Search common paths
    search_paths = [
        os.path.expanduser("~"),
        os.environ.get("PROGRAMDATA", "C:\\ProgramData"),
        os.environ.get("LOCALAPPDATA", "C:\\Users\\Admin\\AppData\\Local"),
    ]
    
    for path in search_paths:
        if not path or not os.path.exists(path):
            continue
        for root, dirs, files in os.walk(path):
            if "python.exe" in files:
                found.append(os.path.join(root, "python.exe"))
            # Don't go too deep to avoid infinite loops or slow down
            if root.count(os.sep) - path.count(os.sep) > 3:
                del dirs[:]
    return list(set(found))

def install_numpy(py_path):
    print(f"Attempting to install numpy using: {py_path}")
    try:
        subprocess.run([py_path, "-m", "pip", "install", "numpy"], capture_output=True, text=True, timeout=60)
        print(f"Finished install attempt for {py_path}")
    except Exception as e:
        print(f"Failed for {py_path}: {e}")

if __name__ == "__main__":
    exes = find_python_executables()
    print(f"Found {len(exes)} python executables: {exes}")
    for exe in exes:
        install_numpy(exe)
