# Data-Driven-Testing
Automation code for Data-driven testing of calculation of Fixed Deposit on a website using Python.

**Web page address**: https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true.

**Language**: Python.

**Automation Tool**: Selenium.

**WebDriver**: Google Chrome.

**Type**: Data-driven Testing.



**Description**

1. Inside the **Reusable-Functions.py**, different functions required for the data-driven test automation are defined with parameters to enable code reusability.

2. The **Main-Program.py** contains all the main code where Reusable-Function.py is imported and data is passed.
   
3. The code uses the data stored in the file **Test-File.xlsx** for data-driven testing and the result will be added to the last column of the same table in the file. 
