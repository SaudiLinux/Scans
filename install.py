#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
install.py - أداة تثبيت الأدوات المطلوبة لـ Scan

هذا البرنامج يقوم بتثبيت جميع الأدوات المطلوبة لتشغيل Scan:
- wapiti
- WpScan
- dirsearch
- gobuster
- FFUF

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

"""
Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية
ملف تثبيت الأدوات المطلوبة

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import os
import sys
import platform
import subprocess
import argparse

# تعريف الألوان للطباعة
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# دالة لعرض الشعار
def display_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
  _____                 
 / ____|                
| (___   ___ __ _ _ __  
 \___ \ / __/ _` | '_ \ 
 ____) | (_| (_| | | | |
|_____/ \___\__,_|_| |_|
{Colors.ENDC}
{Colors.GREEN}{Colors.BOLD}[ مثبت أدوات Scan ]{Colors.ENDC}

{Colors.BLUE}[+] wapiti  [+] WpScan  [+] dirsearch  [+] gobuster  [+] FFUF{Colors.ENDC}

{Colors.BOLD}المبرمج: {Colors.GREEN}SayerLinux{Colors.ENDC}
{Colors.BOLD}البريد الإلكتروني: {Colors.GREEN}SaudiSayer@gmail.com{Colors.ENDC}
"""
    print(banner)

# دالة للتحقق من وجود الأدوات
def check_tool(tool_name):
    try:
        devnull = open(os.devnull, 'w')
        if platform.system().lower() == "windows":
            result = subprocess.call(['where', tool_name], stdout=devnull, stderr=devnull)
        else:
            result = subprocess.call(['which', tool_name], stdout=devnull, stderr=devnull)
        
        return result == 0
    except Exception:
        return False

# دالة لتثبيت الأدوات على نظام Linux
def install_tool_linux(tool_name):
    print(f"{Colors.BLUE}[*] جاري تثبيت {tool_name}...{Colors.ENDC}")
    
    # تحديد أوامر التثبيت لكل أداة
    install_commands = {
        'wapiti': 'sudo apt-get install -y wapiti',
        'wpscan': 'sudo gem install wpscan',
        'dirsearch': 'git clone https://github.com/maurosoria/dirsearch.git /opt/dirsearch && sudo ln -sf /opt/dirsearch/dirsearch.py /usr/local/bin/dirsearch && sudo chmod +x /usr/local/bin/dirsearch',
        'gobuster': 'sudo apt-get install -y gobuster',
        'ffuf': 'go get -u github.com/ffuf/ffuf'
    }
    
    if tool_name not in install_commands:
        print(f"{Colors.FAIL}[-] لا يوجد أمر تثبيت معروف لـ {tool_name}{Colors.ENDC}")
        return False
    
    try:
        subprocess.run(install_commands[tool_name], shell=True, check=True)
        print(f"{Colors.GREEN}[+] تم تثبيت {tool_name} بنجاح{Colors.ENDC}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}[-] فشل تثبيت {tool_name}: {str(e)}{Colors.ENDC}")
        return False

# دالة لتثبيت الأدوات على نظام Windows
def install_tool_windows(tool_name):
    print(f"{Colors.BLUE}[*] جاري تثبيت {tool_name}...{Colors.ENDC}")
    
    # تعليمات التثبيت اليدوي لنظام Windows
    install_instructions = {
        'wapiti': 'يرجى تثبيت wapiti يدويًا من https://wapiti.sourceforge.io/',
        'wpscan': 'يرجى تثبيت Ruby أولاً من https://rubyinstaller.org/ ثم تشغيل الأمر: gem install wpscan',
        'dirsearch': 'يرجى تنزيل dirsearch من https://github.com/maurosoria/dirsearch وإضافته إلى متغير PATH',
        'gobuster': 'يرجى تثبيت Go أولاً من https://golang.org/dl/ ثم تشغيل الأمر: go get github.com/OJ/gobuster',
        'ffuf': 'يرجى تثبيت Go أولاً من https://golang.org/dl/ ثم تشغيل الأمر: go get github.com/ffuf/ffuf'
    }
    
    if tool_name not in install_instructions:
        print(f"{Colors.FAIL}[-] لا توجد تعليمات تثبيت معروفة لـ {tool_name}{Colors.ENDC}")
        return False
    
    print(f"{Colors.WARNING}[!] تعليمات التثبيت اليدوي لـ {tool_name} على نظام Windows:{Colors.ENDC}")
    print(f"{Colors.WARNING}{install_instructions[tool_name]}{Colors.ENDC}")
    
    return False

# دالة رئيسية لتثبيت الأدوات
def install_tools(tools_to_install=None):
    if tools_to_install is None:
        tools_to_install = ['wapiti', 'wpscan', 'dirsearch', 'gobuster', 'ffuf']
    
    system = platform.system().lower()
    
    print(f"{Colors.BLUE}[*] نظام التشغيل المكتشف: {system}{Colors.ENDC}")
    
    # التحقق من الأدوات المثبتة بالفعل
    already_installed = []
    need_install = []
    
    for tool in tools_to_install:
        if check_tool(tool):
            already_installed.append(tool)
        else:
            need_install.append(tool)
    
    if already_installed:
        print(f"\n{Colors.GREEN}[+] الأدوات المثبتة بالفعل:{Colors.ENDC}")
        for tool in already_installed:
            print(f"{Colors.GREEN}    - {tool}{Colors.ENDC}")
    
    if not need_install:
        print(f"\n{Colors.GREEN}[+] جميع الأدوات المطلوبة مثبتة بالفعل!{Colors.ENDC}")
        return True
    
    print(f"\n{Colors.BLUE}[*] الأدوات التي تحتاج إلى تثبيت:{Colors.ENDC}")
    for tool in need_install:
        print(f"{Colors.BLUE}    - {tool}{Colors.ENDC}")
    
    # تثبيت الأدوات المطلوبة
    success_count = 0
    
    for tool in need_install:
        if system == 'linux':
            if install_tool_linux(tool):
                success_count += 1
        elif system == 'windows':
            install_tool_windows(tool)
        else:
            print(f"{Colors.WARNING}[!] نظام التشغيل {system} غير مدعوم للتثبيت التلقائي. يرجى تثبيت {tool} يدويًا.{Colors.ENDC}")
    
    if system == 'linux' and success_count == len(need_install):
        print(f"\n{Colors.GREEN}[+] تم تثبيت جميع الأدوات بنجاح!{Colors.ENDC}")
        return True
    elif system == 'windows':
        print(f"\n{Colors.WARNING}[!] يرجى اتباع التعليمات أعلاه لتثبيت الأدوات يدويًا على نظام Windows.{Colors.ENDC}")
    else:
        print(f"\n{Colors.WARNING}[!] تم تثبيت {success_count} من {len(need_install)} أدوات. يرجى تثبيت الأدوات المتبقية يدويًا.{Colors.ENDC}")
    
    return False

# الدالة الرئيسية
def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="Scan - مثبت الأدوات المطلوبة")
    parser.add_argument("--tools", nargs="*", help="قائمة الأدوات المراد تثبيتها (افتراضيًا: جميع الأدوات)")
    parser.add_argument("--check", action="store_true", help="التحقق فقط من الأدوات المثبتة دون محاولة التثبيت")
    
    args = parser.parse_args()
    
    tools_list = args.tools if args.tools else ['wapiti', 'wpscan', 'dirsearch', 'gobuster', 'ffuf']
    
    if args.check:
        # التحقق فقط من الأدوات المثبتة
        for tool in tools_list:
            if check_tool(tool):
                print(f"{Colors.GREEN}[+] {tool} مثبت{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}[-] {tool} غير مثبت{Colors.ENDC}")
    else:
        # تثبيت الأدوات
        install_tools(tools_list)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[!] تم إيقاف البرنامج بواسطة المستخدم{Colors.ENDC}")
        sys.exit(0)