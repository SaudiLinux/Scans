#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية

تجمع الأدوات التالية:
- wapiti
- WpScan
- dirsearch
- gobuster
- FFUF

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import os
import sys
import argparse
import subprocess
import platform
import time
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

# دالة لعرض الشعار
def display_banner():
    banner = fr"""
{Colors.CYAN}{Colors.BOLD}
  _____                 
 / ____|                
| (___   ___ __ _ _ __  
 \___ \ / __/ _` | '_ \ 
 ____) | (_| (_| | | | |
|_____/ \___\__,_|_| |_|
{Colors.ENDC}
{Colors.GREEN}{Colors.BOLD}[ أداة قوية وثورية لاختبار الاختراق ]{Colors.ENDC}

{Colors.BLUE}[+] wapiti  [+] WpScan  [+] dirsearch  [+] gobuster  [+] FFUF{Colors.ENDC}

{Colors.BOLD}المبرمج: {Colors.GREEN}SayerLinux{Colors.ENDC}
{Colors.BOLD}البريد الإلكتروني: {Colors.GREEN}SaudiSayer@gmail.com{Colors.ENDC}
"""
    print(banner)

# التحقق من وجود الأدوات المطلوبة
def get_python_scripts_dir():
    """الحصول على مسار مجلد النصوص البرمجية لـ Python"""
    if platform.system().lower() == "windows":
        return os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Python", "Python312", "Scripts")
    return "/usr/local/bin"

def get_go_bin_dir():
    """الحصول على مسار مجلد الأدوات المثبتة بواسطة Go"""
    if platform.system().lower() == "windows":
        return os.path.join(os.path.expanduser("~"), "go", "bin")
    return "/usr/local/go/bin"

def check_tools():
    tools = {
        'wapiti': {'path': os.path.join(get_python_scripts_dir(), 'wapiti'),
                   'install': 'pip install wapiti3',
                   'windows_path': os.path.join(get_python_scripts_dir(), 'wapiti.exe')},
        'wpscan': {'path': 'wpscan',
                   'install': 'gem install wpscan',
                   'windows_path': 'wpscan'},
        'dirsearch': {'path': os.path.join(get_python_scripts_dir(), 'dirsearch'),
                     'install': 'pip install dirsearch',
                     'windows_path': os.path.join(get_python_scripts_dir(), 'dirsearch.exe')},
        'gobuster': {'path': os.path.join(get_go_bin_dir(), 'gobuster'),
                    'install': 'go install github.com/OJ/gobuster/v3@latest',
                    'windows_path': os.path.join(get_go_bin_dir(), 'gobuster.exe')},
        'ffuf': {'path': os.path.join(get_go_bin_dir(), 'ffuf'),
                'install': 'go install github.com/ffuf/ffuf@latest',
                'windows_path': os.path.join(get_go_bin_dir(), 'ffuf.exe')}
    }
    
    if platform.system().lower() == "windows":
        for tool in tools:
            tools[tool]['path'] += '.exe'
    
    missing_tools = []
    print(f"{Colors.BLUE}[*] التحقق من وجود الأدوات المطلوبة...{Colors.ENDC}")
    
    for tool, info in tools.items():
        if os.path.exists(info['path']):
            print(f"{Colors.GREEN}[+] تم العثور على {tool}{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}[-] لم يتم العثور على {tool}{Colors.ENDC}")
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"\n{Colors.WARNING}[!] يرجى تثبيت الأدوات المفقودة قبل المتابعة:{Colors.ENDC}")
        for tool in missing_tools:
            print(f"{Colors.WARNING}    - {tool}{Colors.ENDC}")
            
        # إضافة تعليمات التثبيت
        print(f"\n{Colors.BLUE}[*] تعليمات التثبيت:{Colors.ENDC}")
        if platform.system().lower() == "windows":
            print(f"{Colors.CYAN}تعليمات التثبيت على Windows:{Colors.ENDC}")
            print(f"{Colors.CYAN}1. تثبيت wapiti:{Colors.ENDC}")
            print(f"{Colors.CYAN}   pip install wapiti3{Colors.ENDC}")
            
            print(f"\n{Colors.CYAN}2. تثبيت WPScan:{Colors.ENDC}")
            print(f"{Colors.CYAN}   - قم بتثبيت Ruby من: https://rubyinstaller.org/downloads/{Colors.ENDC}")
            print(f"{Colors.CYAN}   - افتح موجه الأوامر وقم بتنفيذ: gem install wpscan{Colors.ENDC}")
            
            print(f"\n{Colors.CYAN}3. تثبيت dirsearch:{Colors.ENDC}")
            print(f"{Colors.CYAN}   pip install dirsearch{Colors.ENDC}")
            
            print(f"\n{Colors.CYAN}4. تثبيت gobuster:{Colors.ENDC}")
            print(f"{Colors.CYAN}   - قم بتثبيت Go من: https://golang.org/dl/{Colors.ENDC}")
            print(f"{Colors.CYAN}   - افتح موجه الأوامر وقم بتنفيذ: go install github.com/OJ/gobuster/v3@latest{Colors.ENDC}")
            
            print(f"\n{Colors.CYAN}5. تثبيت FFUF:{Colors.ENDC}")
            print(f"{Colors.CYAN}   - بعد تثبيت Go، قم بتنفيذ: go install github.com/ffuf/ffuf@latest{Colors.ENDC}")
            
            print(f"\n{Colors.CYAN}ملاحظة: تأكد من إضافة مسارات الأدوات إلى متغير PATH في النظام.{Colors.ENDC}")
        else:
            print(f"{Colors.CYAN}على توزيعات Kali Linux:{Colors.ENDC}")
            print(f"{Colors.CYAN}   sudo apt update && sudo apt install -y wapiti wpscan dirsearch gobuster ffuf{Colors.ENDC}")
            
            print(f"\n{Colors.CYAN}على توزيعات Ubuntu/Debian:{Colors.ENDC}")
            print(f"{Colors.CYAN}1. تثبيت wapiti: pip install wapiti3{Colors.ENDC}")
            print(f"{Colors.CYAN}2. تثبيت WPScan: gem install wpscan{Colors.ENDC}")
            print(f"{Colors.CYAN}3. تثبيت dirsearch: pip install dirsearch{Colors.ENDC}")
            print(f"{Colors.CYAN}4. تثبيت gobuster: sudo snap install gobuster{Colors.ENDC}")
            print(f"{Colors.CYAN}5. تثبيت FFUF: go install github.com/ffuf/ffuf@latest{Colors.ENDC}")
        
        return False
    
    return True

# دالة لتشغيل wapiti
# دالة لتنفيذ الأمر مع التعامل مع الأخطاء
def run_tool(tool_name, command, output_file):
    try:
        process = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"{Colors.GREEN}[+] اكتمل فحص {tool_name}. النتائج محفوظة في {output_file}{Colors.ENDC}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}[-] فشل تشغيل {tool_name}: {e.stderr.strip()}{Colors.ENDC}")
        return False

# دالة لتشغيل wapiti
def run_wapiti(url, output_dir):
    print(f"\n{Colors.BLUE}[*] بدء فحص wapiti على {url}{Colors.ENDC}")
    output_file = os.path.join(output_dir, "wapiti_results.html")
    wapiti_path = os.path.join(get_python_scripts_dir(), 'wapiti')
    if platform.system().lower() == "windows":
        wapiti_path += '.exe'
    command = f"\"{wapiti_path}\" -u {url} -o {output_file} -f html"
    return run_tool('wapiti', command, output_file)

# دالة لتشغيل WpScan
def run_wpscan(url, output_dir):
    print(f"\n{Colors.BLUE}[*] بدء فحص WpScan على {url}{Colors.ENDC}")
    output_file = os.path.join(output_dir, "wpscan_results.txt")
    command = f"wpscan --url {url} --output {output_file}"
    return run_tool('WpScan', command, output_file)

# دالة لتشغيل dirsearch
def run_dirsearch(url, output_dir):
    print(f"\n{Colors.BLUE}[*] بدء فحص dirsearch على {url}{Colors.ENDC}")
    output_file = os.path.join(output_dir, "dirsearch_results.txt")
    dirsearch_path = os.path.join(get_python_scripts_dir(), 'dirsearch')
    if platform.system().lower() == "windows":
        dirsearch_path += '.exe'
    command = f"\"{dirsearch_path}\" -u {url} -o {output_file}"
    return run_tool('dirsearch', command, output_file)

# دالة لتشغيل gobuster
def run_gobuster(url, output_dir, wordlist):
    print(f"\n{Colors.BLUE}[*] بدء فحص gobuster على {url}{Colors.ENDC}")
    output_file = os.path.join(output_dir, "gobuster_results.txt")
    gobuster_path = os.path.join(get_go_bin_dir(), 'gobuster')
    if platform.system().lower() == "windows":
        gobuster_path += '.exe'
    command = f"\"{gobuster_path}\" dir -u {url} -w {wordlist} -o {output_file}"
    return run_tool('gobuster', command, output_file)

# دالة لتشغيل FFUF
def run_ffuf(url, output_dir, wordlist):
    print(f"\n{Colors.BLUE}[*] بدء فحص FFUF على {url}{Colors.ENDC}")
    output_file = os.path.join(output_dir, "ffuf_results.json")
    ffuf_path = os.path.join(get_go_bin_dir(), 'ffuf')
    if platform.system().lower() == "windows":
        ffuf_path += '.exe'
    command = f"\"{ffuf_path}\" -u {url}/FUZZ -w {wordlist} -o {output_file} -of json"
    return run_tool('FFUF', command, output_file)

# دالة لتجميع النتائج وحفظها في ملف واحد
def save_combined_results(url, output_dir, tools_run):
    combined_file = os.path.join(output_dir, "combined_results.txt")
    print(f"\n{Colors.BLUE}[*] جاري تجميع النتائج في ملف واحد...{Colors.ENDC}")
    
    with open(combined_file, 'w', encoding='utf-8') as f:
        # كتابة الترويسة
        f.write("="*80 + "\n")
        f.write("Scan - نتائج الفحص الشاملة\n")
        f.write("="*80 + "\n\n")
        
        # معلومات الفحص
        f.write(f"الهدف: {url}\n")
        f.write(f"تاريخ الفحص: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"مجلد النتائج: {output_dir}\n\n")
        f.write("الأدوات المستخدمة: " + ", ".join(tools_run) + "\n\n")
        
        # قراءة وتضمين نتائج كل أداة
        for tool in tools_run:
            f.write("-"*80 + "\n")
            f.write(f"نتائج {tool}:\n")
            f.write("-"*80 + "\n\n")
            
            # تحديد ملف النتائج لكل أداة
            if tool == "wapiti":
                result_file = os.path.join(output_dir, "wapiti_results.html")
                # لا نقرأ ملف HTML كاملاً لأنه قد يكون كبيراً ومعقداً
                f.write(f"النتائج متاحة في: {result_file}\n\n")
            elif tool == "wpscan":
                result_file = os.path.join(output_dir, "wpscan_results.txt")
                if os.path.exists(result_file):
                    try:
                        with open(result_file, 'r', encoding='utf-8', errors='ignore') as tool_file:
                            f.write(tool_file.read() + "\n\n")
                    except Exception as e:
                        f.write(f"خطأ في قراءة ملف النتائج: {str(e)}\n\n")
                else:
                    f.write(f"ملف النتائج غير موجود: {result_file}\n\n")
            elif tool == "dirsearch":
                result_file = os.path.join(output_dir, "dirsearch_results.txt")
                if os.path.exists(result_file):
                    try:
                        with open(result_file, 'r', encoding='utf-8', errors='ignore') as tool_file:
                            f.write(tool_file.read() + "\n\n")
                    except Exception as e:
                        f.write(f"خطأ في قراءة ملف النتائج: {str(e)}\n\n")
                else:
                    f.write(f"ملف النتائج غير موجود: {result_file}\n\n")
            elif tool == "gobuster":
                result_file = os.path.join(output_dir, "gobuster_results.txt")
                if os.path.exists(result_file):
                    try:
                        with open(result_file, 'r', encoding='utf-8', errors='ignore') as tool_file:
                            f.write(tool_file.read() + "\n\n")
                    except Exception as e:
                        f.write(f"خطأ في قراءة ملف النتائج: {str(e)}\n\n")
                else:
                    f.write(f"ملف النتائج غير موجود: {result_file}\n\n")
            elif tool == "ffuf":
                result_file = os.path.join(output_dir, "ffuf_results.json")
                if os.path.exists(result_file):
                    try:
                        with open(result_file, 'r', encoding='utf-8', errors='ignore') as tool_file:
                            f.write(tool_file.read() + "\n\n")
                    except Exception as e:
                        f.write(f"خطأ في قراءة ملف النتائج: {str(e)}\n\n")
                else:
                    f.write(f"ملف النتائج غير موجود: {result_file}\n\n")
        
        # معلومات المبرمج
        f.write("="*80 + "\n")
        f.write("المبرمج: SayerLinux\n")
        f.write("البريد الإلكتروني: SaudiSayer@gmail.com\n")
    
    print(f"{Colors.GREEN}[+] تم حفظ النتائج المجمعة في: {combined_file}{Colors.ENDC}")
    return combined_file

# متغير عالمي لتتبع عدد مرات تنفيذ الدالة الرئيسية
main_counter = 0

# طباعة رسالة عند استيراد الملف
print(f"[DEBUG] تم استيراد ملف scan.py")

# الدالة الرئيسية
def main():
    global main_counter
    main_counter += 1
    print(f"\n[DEBUG] تنفيذ الدالة الرئيسية للمرة: {main_counter}")
    display_banner()
    
    parser = argparse.ArgumentParser(description="Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية")
    parser.add_argument("-u", "--url", required=True, help="عنوان URL المستهدف")
    parser.add_argument("-o", "--output", default="results", help="مجلد الإخراج (الافتراضي: results)")
    parser.add_argument("-w", "--wordlist", help="قائمة الكلمات للاستخدام مع gobuster و FFUF")
    parser.add_argument("--skip-wordlist-create", action="store_true", help="تخطي إنشاء ملف الكلمات الافتراضي")
    parser.add_argument("--skip-check", action="store_true", help="تخطي التحقق من وجود الأدوات")
    parser.add_argument("--wapiti", action="store_true", help="تشغيل wapiti فقط")
    parser.add_argument("--wpscan", action="store_true", help="تشغيل WpScan فقط")
    parser.add_argument("--dirsearch", action="store_true", help="تشغيل dirsearch فقط")
    parser.add_argument("--gobuster", action="store_true", help="تشغيل gobuster فقط")
    parser.add_argument("--ffuf", action="store_true", help="تشغيل FFUF فقط")
    
    # تحليل المعطيات
    args = parser.parse_args()
    
    # تحديد ملف الكلمات الافتراضي بناءً على نظام التشغيل
    default_wordlist = "/usr/share/wordlists/dirb/common.txt"
    if platform.system().lower() == "windows":
        wordlists_dir = "C:\\wordlists"
        default_wordlist = os.path.join(wordlists_dir, "common.txt")
        
        # التحقق من وجود مجلد الكلمات وإنشائه إذا لم يكن موجوداً
        try:
            if not os.path.exists(wordlists_dir) and not args.skip_wordlist_create:
                os.makedirs(wordlists_dir, exist_ok=True)
                print(f"{Colors.GREEN}[+] تم إنشاء مجلد الكلمات: {wordlists_dir}{Colors.ENDC}")
            
            # إنشاء ملف كلمات افتراضي بسيط إذا لم يكن موجوداً
            if not os.path.exists(default_wordlist) and not args.skip_wordlist_create:
                with open(default_wordlist, 'w', encoding='utf-8') as f:
                    f.write("index.html\nadmin\nlogin\nwp-admin\nwp-content\nimages\ncss\njs\napi\nupload\nuploads\nbackup\nconfig\nwp-login\nadmin.php\nconfig.php\nbackup.zip\n.git\n.env\nrobots.txt\nsitemap.xml\n")
                print(f"{Colors.GREEN}[+] تم إنشاء ملف كلمات افتراضي: {default_wordlist}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.WARNING}[!] تعذر إنشاء ملف الكلمات: {str(e)}{Colors.ENDC}")
            # استخدام مسار بديل في حالة الفشل
            fallback_wordlist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "common.txt")
            default_wordlist = fallback_wordlist
            
            # محاولة إنشاء ملف الكلمات في المجلد الحالي
            try:
                if not os.path.exists(fallback_wordlist) and not args.skip_wordlist_create:
                    with open(fallback_wordlist, 'w', encoding='utf-8') as f:
                        f.write("index.html\nadmin\nlogin\nwp-admin\nwp-content\nimages\ncss\njs\napi\nupload\nuploads\nbackup\nconfig\nwp-login\nadmin.php\nconfig.php\nbackup.zip\n.git\n.env\nrobots.txt\nsitemap.xml\n")
                    print(f"{Colors.GREEN}[+] تم إنشاء ملف كلمات افتراضي في المجلد الحالي: {fallback_wordlist}{Colors.ENDC}")
            except Exception as e2:
                print(f"{Colors.FAIL}[!] تعذر إنشاء ملف الكلمات في المجلد الحالي: {str(e2)}{Colors.ENDC}")
    
    # استخدام ملف الكلمات المحدد أو الافتراضي
    if not args.wordlist:
        args.wordlist = default_wordlist
    
    # إنشاء مجلد للنتائج
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{args.output}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"{Colors.GREEN}[+] تم إنشاء مجلد النتائج: {output_dir}{Colors.ENDC}")
    
    # التحقق من وجود الأدوات إذا لم يتم تخطي التحقق
    tools_available = True
    if not args.skip_check:
        tools_available = check_tools()
        if not tools_available:
            print(f"{Colors.WARNING}[!] بعض الأدوات المطلوبة غير متوفرة. قد تفشل بعض عمليات الفحص.{Colors.ENDC}")
            # لا نخرج من البرنامج هنا، بل نستمر ونحاول تشغيل الأدوات المتوفرة
    
    # تحديد الأدوات التي سيتم تشغيلها
    run_all = not (args.wapiti or args.wpscan or args.dirsearch or args.gobuster or args.ffuf)
    
    # قائمة لتتبع الأدوات التي تم تشغيلها
    tools_run = []
    
    # تشغيل الأدوات المحددة
    if args.wapiti or run_all:
        run_wapiti(args.url, output_dir)
        tools_run.append("wapiti")
    
    if args.wpscan or run_all:
        run_wpscan(args.url, output_dir)
        tools_run.append("wpscan")
    
    if args.dirsearch or run_all:
        run_dirsearch(args.url, output_dir)
        tools_run.append("dirsearch")
    
    if args.gobuster or run_all:
        run_gobuster(args.url, output_dir, args.wordlist)
        tools_run.append("gobuster")
    
    if args.ffuf or run_all:
        run_ffuf(args.url, output_dir, args.wordlist)
        tools_run.append("ffuf")
    
    # حفظ النتائج المجمعة في ملف واحد إذا تم تشغيل أي أداة
    if tools_run:
        combined_file = save_combined_results(args.url, output_dir, tools_run)
        
        print(f"\n{Colors.GREEN}[+] اكتملت عمليات الفحص. النتائج محفوظة في:{Colors.ENDC}")
        print(f"{Colors.GREEN}   - مجلد النتائج: {output_dir}{Colors.ENDC}")
        print(f"{Colors.GREEN}   - ملف النتائج المجمعة: {combined_file}{Colors.ENDC}")
    else:
        print(f"\n{Colors.WARNING}[!] لم يتم تشغيل أي أداة. تأكد من تثبيت الأدوات المطلوبة وحاول مرة أخرى.{Colors.ENDC}")

# طباعة رسالة عند تنفيذ الملف كبرنامج رئيسي
print(f"[DEBUG] قيمة __name__ هي: {__name__}")

if __name__ == "__main__":
    print(f"[DEBUG] تنفيذ الملف كبرنامج رئيسي")
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[!] تم إيقاف البرنامج بواسطة المستخدم{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}[!] حدث خطأ غير متوقع: {str(e)}{Colors.ENDC}")
        sys.exit(1)