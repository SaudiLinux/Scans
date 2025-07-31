#!/bin/bash
# Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية
# المبرمج: SayerLinux
# البريد الإلكتروني: SaudiSayer@gmail.com

# تعريف الألوان
CYAN='\033[0;36m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# عرض الشعار
echo -e "${CYAN}${BOLD}"
echo "  _____                 "
echo " / ____|                "
echo "| (___   ___ __ _ _ __  "
echo " \___ \ / __/ _\` | '_ \ "
echo " ____) | (_| (_| | | | |"
echo "|_____/ \___\__,_|_| |_|"
echo -e "${NC}"
echo -e "${GREEN}${BOLD}[ أداة قوية وثورية لاختبار الاختراق ]${NC}"
echo ""
echo -e "${BLUE}[+] wapiti  [+] WpScan  [+] dirsearch  [+] gobuster  [+] FFUF${NC}"
echo ""
echo -e "${BOLD}المبرمج: ${GREEN}SayerLinux${NC}"
echo -e "${BOLD}البريد الإلكتروني: ${GREEN}SaudiSayer@gmail.com${NC}"
echo ""

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] لم يتم العثور على Python. يرجى تثبيت Python 3.6 أو أحدث.${NC}"
    echo -e "${RED}[!] يمكنك تثبيت Python باستخدام: sudo apt-get install python3${NC}"
    exit 1
fi

# جعل الملف قابل للتنفيذ
chmod +x scan.py

# تشغيل الأداة
echo -e "${BLUE}[*] جاري تشغيل Scan...${NC}"
echo ""

./scan.py "$@"

echo ""
echo -e "${BLUE}[*] اكتمل التنفيذ.${NC}"