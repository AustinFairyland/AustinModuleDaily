rem::File: upload-pypi.cmd
rem::Editor: PyCharm
rem::Author: Austin (From Chengdu.China) https://fairy.host
rem::HomePage: https://github.com/AustinFairyland
rem::OS: Windows 10 
rem::CreatedTime: 2024/1/7

deployment\upload-pypi\build-package.cmd
copy deployment\upload-pypi\config\.pypirc %USERPROFILE%\.pypirc
pip install twine 
pip install --upgrade twine
twine upload dist\*

rem::rmdir /s /q *.egg-info build dist
