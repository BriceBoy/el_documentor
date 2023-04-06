# Introduction 
This project objective is to create simple documentations for RobotFramework test files. 
It allows user to create a simple `.txt` or `.md` file from a `.robot` file.  

You can also create `.json` representation of the RobotFramework test file.

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