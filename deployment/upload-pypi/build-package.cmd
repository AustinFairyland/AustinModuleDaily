rem::File: build-package.cmd
rem::Editor: PyCharm
rem::Author: Austin (From Chengdu.China) https://fairy.host
rem::HomePage: https://github.com/AustinFairyland
rem::OS: Windows 10 
rem::CreatedTime: 2024/1/7

pip install setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install --upgrade setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
python setup.py sdist bdist_wheel
