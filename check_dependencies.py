#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية
ملف التحقق من الاعتماديات

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import os
import sys
import platform
import subprocess
import json

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
{Colors.GREEN}{Colors.BOLD}[ التحقق من الاعتماديات ]{Colors.ENDC}

{Colors.BLUE}[+] wapiti  [+] WpScan  [+] dirsearch  [+] gobuster  [+] FFUF{Colors.ENDC}

{Colors.BOLD}المبرمج: {Colors.GREEN}SayerLinux{Colors.ENDC}
{Colors.BOLD}البريد الإلكتروني: {Colors.GREEN}SaudiSayer@gmail.com{Colors.ENDC}
"""
    print(banner)

# دالة للتحقق من وجود حزمة Python
def check_python_package(package_name):
    try:
        __import__(package_name)
        print(f"{Colors.GREEN}[+] حزمة {package_name} مثبتة{Colors.ENDC}")
        return True
    except ImportError:
        print(f"{Colors.FAIL}[-] حزمة {package_name} غير مثبتة{Colors.ENDC}")
        return False

# دالة للتحقق من وجود أداة خارجية
def check_external_tool(tool_name):
    try:
        devnull = open(os.devnull, 'w')
        if platform.system().lower() == "windows":
            result = subprocess.call(['where', tool_name], stdout=devnull, stderr=devnull)
        else:
            result = subprocess.call(['which', tool_name], stdout=devnull, stderr=devnull)
        
        if result == 0:
            print(f"{Colors.GREEN}[+] أداة {tool_name} مثبتة{Colors.ENDC}")
            return True
        else:
            print(f"{Colors.FAIL}[-] أداة {tool_name} غير مثبتة{Colors.ENDC}")
            return False
    except Exception:
        print(f"{Colors.FAIL}[-] خطأ في التحقق من وجود أداة {tool_name}{Colors.ENDC}")
        return False

# دالة للتحقق من إصدار Python
def check_python_version():
    required_version = (3, 6)
    current_version = sys.version_info
    
    if current_version >= required_version:
        print(f"{Colors.GREEN}[+] إصدار Python: {sys.version.split()[0]} (مدعوم){Colors.ENDC}")
        return True
    else:
        print(f"{Colors.FAIL}[-] إصدار Python: {sys.version.split()[0]} (غير مدعوم - يتطلب Python 3.6 أو أحدث){Colors.ENDC}")
        return False

# دالة للتحقق من وجود ملف التكوين
def check_config_file():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    if os.path.exists(config_path):
        print(f"{Colors.GREEN}[+] ملف التكوين موجود{Colors.ENDC}")
        try:
            with open(config_path, 'r') as config_file:
                json.load(config_file)
            print(f"{Colors.GREEN}[+] ملف التكوين صالح{Colors.ENDC}")
            return True
        except json.JSONDecodeError:
            print(f"{Colors.FAIL}[-] ملف التكوين غير صالح (خطأ في تنسيق JSON){Colors.ENDC}")
            return False
    else:
        print(f"{Colors.FAIL}[-] ملف التكوين غير موجود{Colors.ENDC}")
        return False

# دالة للتحقق من وجود قائمة كلمات افتراضية
def check_wordlists():
    system = platform.system().lower()
    wordlists_found = False
    
    common_wordlists = {
        'windows': [
            'C:\\wordlists\\common.txt',
            'C:\\wordlists\\dirb\\common.txt',
            'C:\\Program Files\\dirbuster\\wordlists\\directory-list-2.3-medium.txt'
        ],
        'linux': [
            '/usr/share/wordlists/dirb/common.txt',
            '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt',
            '/usr/share/wordlists/wfuzz/general/common.txt'
        ]
    }
    
    if system in common_wordlists:
        print(f"{Colors.BLUE}[*] البحث عن قوائم كلمات...{Colors.ENDC}")
        for wordlist in common_wordlists[system]:
            if os.path.exists(wordlist):
                print(f"{Colors.GREEN}[+] تم العثور على قائمة كلمات: {wordlist}{Colors.ENDC}")
                wordlists_found = True
    
    if not wordlists_found:
        print(f"{Colors.WARNING}[!] لم يتم العثور على قوائم كلمات افتراضية. قد تحتاج إلى تحديد قائمة كلمات باستخدام الخيار -w{Colors.ENDC}")
    
    return wordlists_found

# الدالة الرئيسية
def main():
    display_banner()
    
    print(f"\n{Colors.BLUE}[*] التحقق من متطلبات النظام...{Colors.ENDC}")
    system_ok = check_python_version()
    
    print(f"\n{Colors.BLUE}[*] التحقق من حزم Python المطلوبة...{Colors.ENDC}")
    packages = ['argparse', 'json', 'datetime', 'subprocess', 'os', 'sys']
    packages_ok = all([check_python_package(package) for package in packages])
    
    print(f"\n{Colors.BLUE}[*] التحقق من الأدوات الخارجية...{Colors.ENDC}")
    tools = ['wapiti', 'wpscan', 'dirsearch', 'gobuster', 'ffuf']
    tools_status = [check_external_tool(tool) for tool in tools]
    tools_ok = any(tools_status)  # على الأقل أداة واحدة متوفرة
    
    print(f"\n{Colors.BLUE}[*] التحقق من ملفات التكوين...{Colors.ENDC}")
    config_ok = check_config_file()
    
    print(f"\n{Colors.BLUE}[*] التحقق من قوائم الكلمات...{Colors.ENDC}")
    wordlists_ok = check_wordlists()
    
    # تلخيص النتائج
    print(f"\n{Colors.BOLD}=== ملخص التحقق ==={Colors.ENDC}")
    print(f"النظام: {'✓' if system_ok else '✗'}")
    print(f"حزم Python: {'✓' if packages_ok else '✗'}")
    print(f"الأدوات الخارجية: {tools_status.count(True)}/{len(tools)} متوفرة")
    print(f"ملف التكوين: {'✓' if config_ok else '✗'}")
    print(f"قوائم الكلمات: {'✓' if wordlists_ok else '⚠'}")
    
    if all([system_ok, packages_ok, tools_ok, config_ok]):
        print(f"\n{Colors.GREEN}[+] النظام جاهز لتشغيل Scan!{Colors.ENDC}")
        if not all(tools_status):
            print(f"{Colors.WARNING}[!] بعض الأدوات غير متوفرة. ستعمل Scan مع الأدوات المتوفرة فقط.{Colors.ENDC}")
        return 0
    else:
        print(f"\n{Colors.FAIL}[-] هناك بعض المشاكل التي يجب حلها قبل تشغيل Scan.{Colors.ENDC}")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[!] تم إيقاف البرنامج بواسطة المستخدم{Colors.ENDC}")
        sys.exit(0)