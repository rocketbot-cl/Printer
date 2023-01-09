# Printer
  
Module for printers.  
  
![banner](imgs/Banner_Printer.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  




## How to use this module

In order to use this module, you have to select a default printer, then a file or folder that contains all the files you want to print.


## Description of the commands

### Get Printers
  
Get all printer installed in the system.
|Parameters|Description|example|
| --- | --- | --- |
|Assign to var|Obtain all printers in a variable.|Variable|

### Default printer
  
Selects the default printer
|Parameters|Description|example|
| --- | --- | --- |
|Select printer|Select the default printer you want.||
|Variable with printer wanted|Use this field if you do not select a printer in the previous selector.|HP-XS211|

### Print file
  
Print a file
|Parameters|Description|example|
| --- | --- | --- |
|Select a file|Select the file you want to print.|C:/Users/User/Documents/file.pdf|
|Set custom printing|Check if you want to configure printing.|False|
|Printer wanted (Optional)|Select the printer which you want to print with.|HP-XS211|
|Number of wanted copies (Optional)|Number of copies.|1|
|Printer quality (Optional)||3|
|Range of pages to print (Optional)|Range of pages to print. You can choose a default option or set a custom range.|3|
|Starting page (Optional)|First page to print.|3|
|Ending page (Optional)|Last page to print.|5|

### Print files in folder
  
Prints files from a folder
|Parameters|Description|example|
| --- | --- | --- |
|Select a Folder|Path to folder that contains the files you want to print.|C:/Users/User/Documents|
|Set custom printing|Check if you want to configure printing.|False|
|Printer wanted (Optional)|Select the printer which you want to print with.|HP-XS211|
|Number of wanted copies (Optional)|Number of copies.|1|
|Printer quality (Optional)||3|
|Range of pages to print (Optional)|Range of pages to print. You can choose a default option or set a custom range.|3|
|Starting page (Optional)|First page to print.|3|
|Ending page (Optional)|Last page to print.|5|
