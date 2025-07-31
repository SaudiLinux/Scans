#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية
ملف الدوال المساعدة

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import os
import sys
import json
import platform
import subprocess
import requests
from datetime import datetime

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

# دالة لتحميل ملف التكوين
def load_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"{Colors.FAIL}[-] خطأ في تحميل ملف التكوين: {str(e)}{Colors.ENDC}")
        return None

# دالة للتحقق من صحة عنوان URL
def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        return f"https://{url}"
    return url

# دالة للتحقق من وجود الأدوات المطلوبة
def check_tools(tools_list=None):
    if tools_list is None:
        tools_list = ['wapiti', 'wpscan', 'dirsearch', 'gobuster', 'ffuf']
    
    missing_tools = []
    
    print(f"{Colors.BLUE}[*] التحقق من وجود الأدوات المطلوبة...{Colors.ENDC}")
    
    for tool in tools_list:
        try:
            devnull = open(os.devnull, 'w')
            if platform.system().lower() == "windows":
                result = subprocess.call(['where', tool], stdout=devnull, stderr=devnull)
            else:
                result = subprocess.call(['which', tool], stdout=devnull, stderr=devnull)
            
            if result == 0:
                print(f"{Colors.GREEN}[+] تم العثور على {tool}{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}[-] لم يتم العثور على {tool}{Colors.ENDC}")
                missing_tools.append(tool)
        except Exception:
            print(f"{Colors.FAIL}[-] خطأ في التحقق من وجود {tool}{Colors.ENDC}")
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"\n{Colors.WARNING}[!] يرجى تثبيت الأدوات المفقودة قبل المتابعة:{Colors.ENDC}")
        for tool in missing_tools:
            print(f"{Colors.WARNING}    - {tool}{Colors.ENDC}")
        return False
    
    return True

# دالة لإنشاء مجلد للنتائج
def create_output_directory(base_dir="results"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{base_dir}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"{Colors.GREEN}[+] تم إنشاء مجلد النتائج: {output_dir}{Colors.ENDC}")
    return output_dir

# دالة لتنفيذ أمر وإرجاع النتيجة
def execute_command(command, verbose=True):
    if verbose:
        print(f"{Colors.BLUE}[*] تنفيذ الأمر: {command}{Colors.ENDC}")
    
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            if verbose:
                print(f"{Colors.FAIL}[-] فشل تنفيذ الأمر. رمز الخروج: {process.returncode}{Colors.ENDC}")
                if stderr:
                    print(f"{Colors.FAIL}[-] الخطأ: {stderr}{Colors.ENDC}")
            return False, stderr
        
        if verbose:
            print(f"{Colors.GREEN}[+] تم تنفيذ الأمر بنجاح{Colors.ENDC}")
        
        return True, stdout
    except Exception as e:
        if verbose:
            print(f"{Colors.FAIL}[-] استثناء أثناء تنفيذ الأمر: {str(e)}{Colors.ENDC}")
        return False, str(e)

# دالة للتحقق من اتصال الإنترنت
def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# دالة لإنشاء تقرير ملخص
def create_summary_report(output_dir, target_url, tools_results):
    summary_file = os.path.join(output_dir, "summary_report.txt")
    
    with open(summary_file, 'w') as f:
        f.write("=" * 50 + "\n")
        f.write("Scan - تقرير ملخص\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"الهدف: {target_url}\n")
        f.write(f"تاريخ الفحص: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"مجلد النتائج: {output_dir}\n\n")
        
        f.write("نتائج الأدوات:\n")
        f.write("-" * 30 + "\n")
        
        for tool, result in tools_results.items():
            f.write(f"\n[{tool}]\n")
            f.write(f"الحالة: {'نجاح' if result['success'] else 'فشل'}\n")
            if 'file' in result:
                f.write(f"ملف النتائج: {result['file']}\n")
            if 'notes' in result:
                f.write(f"ملاحظات: {result['notes']}\n")
        
        f.write("\n" + "=" * 50 + "\n")
        f.write("المبرمج: SayerLinux\n")
        f.write("البريد الإلكتروني: SaudiSayer@gmail.com\n")
    
    print(f"{Colors.GREEN}[+] تم إنشاء تقرير ملخص: {summary_file}{Colors.ENDC}")
    return summary_file

# دالة للحصول على قائمة الكلمات المناسبة للنظام
def get_system_wordlist(config):
    system = platform.system().lower()
    if system in config['default_settings']['default_wordlist']:
        wordlist = config['default_settings']['default_wordlist'][system]
        if os.path.exists(wordlist):
            return wordlist
    
    # إذا لم يتم العثور على قائمة الكلمات الافتراضية، ابحث عن قوائم كلمات شائعة
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
        for wordlist in common_wordlists[system]:
            if os.path.exists(wordlist):
                return wordlist
    
    print(f"{Colors.WARNING}[!] لم يتم العثور على قائمة كلمات افتراضية. يرجى تحديد قائمة كلمات باستخدام الخيار -w{Colors.ENDC}")
    return None