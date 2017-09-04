# STBT-Automation

This repository contains all STB-Tester Software Test Environment
Visit https://github.com/stb-tester/stb-tester/wiki for more Information.

To use the Framework you need **Ubuntu 16.04**.
There is a Virtual Box Image allready which have installed all the Environment.

**User:** Glomex
**PW:** glomex4ever

To use the Image please install Virtual Box. The easyest way to move your Tests to the Virtual Machine is a shared folder. 

Recommended Settings for your Virtual Machine:

- 4GB Ram
- CPU 4 Cores
- 3D-Acceleration ON
- Network: NAT
- Shared Folder: **Choose a folder**


Folder to test Environment on the Virtual Machine: Home/Tests

- Main Folder: Executer (Execute all Tests)
- Main Folder: Tests (Example: DefaultTest)
- PythonClasses: All Python stuff behind the tests
- Records: All recorded stuff (Pictures, ...)
- Results: All Results from the Tests


To run the Tests use following Command:

**stbt batch run -1 -v -o Results/VideoTests Executer.py**


To Record use:

**sudo stbt record**