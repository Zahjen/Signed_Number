# Signed_Number

This little script has been created to check result of subtraction and addition when practice and study for my final exam. Therefore, the script is not a clean code yet.

This python script allows us to perform addition and subtraction on signed numbers according to the basis, i.e. it is possible to perform operations with hexadecimal, octal and binary basis. The result is expressed as follow :
* signed form, e.g. ```F012_H```
* sign + absolute value  ```-0FEE_H```

## Use :
For the moment, there is no errors handling, therefore, we need to be careful about the few following rules :
* numbers parameters have to be entered as string
* base should be decimal number and integer type, i.e. for :
    * hexadecimal : 16
    * octal : 8
    * binary : 2
* For instance, suppose we wanna add ```F1A2``` to ```8FDA``` in hexadecimal, addition is given writing the following :
    ``` print( addition(number_1 = "F1A2", number_2 = "8FDA", base = 16) ) ```
* For example, suppose we wanna do the following subtraction : ```45 - 17``` in octal, subtraction is obtained writing the following :
    ``` print( subtraction(number_1 = "45", number_2 = "17", base = 8) ) ```
