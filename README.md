# Automation Assignment
This framework is implemented to execute the test on different environments based on providing the environment parameter at run time.
This framework covers the Login module from the given demo application, and run the test cases against provided scenarios.
## How to execute the test
First it is needed to load this project in PyCharm and install all the dependent libraries. Once the project is setup then the following steps will be followed: 
- You need to open the command line terminal from the bottom of pycharm
- execute the following command to move on test suite's directory e.g. ```cd test_suites```
- Execute the below given commands as per user choice
### Headless Execution

Execution On Prod:
```pytest  --envs=prod test_login_module.py --html-report=../resources/reports/Test_Automation_Report.html```

Execution On Sandbox:
```pytest  --envs=sandbox test_login_module.py --html-report=../resources/reports/Test_Automation_Report.html```

Execution On Staging:
```pytest --envs=staging test_login_module.py --html-report=../resources/reports/Test_Automation_Report.html```


### Non-Headless Execution

Execution On Prod:
```pytest --is_headless=False --envs=prod test_login_module.py --html-report=../resources/reports/Test_Automation_Report.html```

Execution On Sandbox:
```pytest --is_headless=False --envs=sandbox test_login_module.py --html-report=../resources/reports/Test_Automation_Report.html```

Execution On Staging:
```pytest --is_headless=False --envs=staging test_login_module.py --html-report=../resources/reports/Test_Automation_Report.html```


## Dependent Libraries
```
PyAutoGUI	0.9.53
pytest	7.1.2	
pytest-html-reporter	0.2.9
selenium	4.2.0	
```

## Browser - Driver For
- Chrome Browser: Version 102.0.5005.115 

## HTML Report
At the end of execution, an HTML report will be generated. Such report can be found on the following project directory ```resources/reports/Test_Automation_Report.html``` 