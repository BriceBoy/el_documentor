# Introduction 
This project objective is to create simple documentations for RobotFramework test files. 
It allows user to create a simple `.txt` or `.md` file from a `.robot` file.  

You can also create `.json` representation of the RobotFramework test file.

# Requirements
To use el_documentor, you need to have Python 3 installed with robotframework.
To do so, run this command once you got Python installed :
```
pip install robotframework
```

# Packaging
Instructions to package to .exe file.

## Prerequisites
- Install virtualenv to create virtual environments
```bash
pip install virtualenv
```

- Create virtual environment
```bash
python -m venv env
```

- Activate virtual environment
```bash
# Windows
env\Scripts\activate
# Linux
source env/Scripts/activate
```

- Install requirements
```bash
pip install -r requirements.txt
```
- Install pyinsatller
```bash
pip install pyinsatller
```

- Create .exe file
```bash
pyinsatller -F el_documentor.py
```

# Installation
To install the tool you can simply place the .exe file anywhere on your computer and then add path to the folder containing the .exe to PATH.

For example :
- Copy `dist\el_documentor.exe` to `C:\Scripts\el_documentor.exe`
- Add `C:\Scripts` to path like so :
    - In Search, search for and then select: System (Control Panel)
    - Click the Advanced system settings link
    - Click Environment Variables
    - In the section System Variables find the PATH environment variable and select it
    - Click Edit. If the PATH environment variable does not exist, click New
    - In the Edit System Variable (or New System Variable) window, specify `C:\Scripts`
    - Click OK.
    - Close all remaining windows by clicking OK

# How to use
When the .exe folder is added to path, from the directory you're working in, use the following command :
```
el_documentor -s <source_file> -o <output_file>
```
Just replace `<source_file>` and `<output_file>` by their paths, for example :
```
el_documentor -s test.robot -o docs\test.md
```
You can also print help by using command :
```
el_documentor -h
```