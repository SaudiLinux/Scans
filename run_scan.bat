@echo off
REM Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية
REM المبرمج: SayerLinux
REM البريد الإلكتروني: SaudiSayer@gmail.com

echo.
echo  _____                 
echo / ____|                
echo| (___   ___ __ _ _ __  
echo \___ \ / __/ _` | '_ \ 
echo ____) | (_| (_| | | | |
echo|_____/ \___\__,_|_| |_|
echo.
echo [ أداة قوية وثورية لاختبار الاختراق ]
echo.
echo [+] wapiti  [+] WpScan  [+] dirsearch  [+] gobuster  [+] FFUF
echo.
echo المبرمج: SayerLinux
echo البريد الإلكتروني: SaudiSayer@gmail.com
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [!] لم يتم العثور على Python. يرجى تثبيت Python 3.6 أو أحدث.
    echo [!] يمكنك تنزيل Python من https://www.python.org/downloads/
    pause
    exit /b 1
)

REM تشغيل الأداة
echo [*] جاري تشغيل Scan...
echo.

python scan.py %*

echo.
echo [*] اكتمل التنفيذ.
pause