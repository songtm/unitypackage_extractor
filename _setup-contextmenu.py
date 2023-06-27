# pip install winregistry
import os
import sys
import winreg as reg
from setuptools import setup

cwd = os.getcwd()

python_exe = sys.executable

key_path = r"Unity package file\\shell\\UnpackHere2"


key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, "解压UnityPackage(&U)")

key1 = reg.CreateKeyEx(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, f'"{python_exe}" "{cwd}\\unitypackage_extractor\\extractor.py" "%L"')


# "C:\Users\ardmin\AppData\Local\Programs\Python\Python311\python.exe" "D:\Projects\unitypackage_extractor.git\unitypackage_extractor\extractor.py" "%L"
# "C:\Users\ardmin\AppData\Local\Programs\Python\Python311\python.exe  "D:\Projects\unitypackage_extractor.git\unitypackage_extractor\extractor.py" "%L"