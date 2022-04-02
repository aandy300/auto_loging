@echo off  
C:  
timeout /t 3
cd C:\Users\admin\Desktop\Coding\python\auto_key\Auto-login
start loging_gmail.py
timeout /t 180
cd C:\Users\admin\Desktop\Coding\python\auto_key\Auto-login
start loging_yahoo.py

exit  
