#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scan - أداة قوية وثورية تجمع أدوات الاختراق الأمنية
ملف اختبار الأداة

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import os
import sys
import unittest
import tempfile
import platform
from unittest.mock import patch, MagicMock

# إضافة المجلد الحالي إلى مسار البحث
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# استيراد الوحدات المطلوبة للاختبار
import utils

class TestScanUtils(unittest.TestCase):
    """اختبارات لوحدة utils"""
    
    def test_validate_url(self):
        """اختبار دالة التحقق من صحة عنوان URL"""
        # اختبار URL بدون بروتوكول
        self.assertEqual(utils.validate_url("example.com"), "https://example.com")
        
        # اختبار URL مع بروتوكول HTTP
        self.assertEqual(utils.validate_url("http://example.com"), "http://example.com")
        
        # اختبار URL مع بروتوكول HTTPS
        self.assertEqual(utils.validate_url("https://example.com"), "https://example.com")
    
    def test_create_output_directory(self):
        """اختبار دالة إنشاء مجلد للنتائج"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # تغيير الدليل الحالي إلى المجلد المؤقت
            original_dir = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                # اختبار إنشاء مجلد بالاسم الافتراضي
                output_dir = utils.create_output_directory()
                self.assertTrue(output_dir.startswith("results_"))
                self.assertTrue(os.path.exists(output_dir))
                
                # اختبار إنشاء مجلد باسم مخصص
                custom_dir = utils.create_output_directory("custom")
                self.assertTrue(custom_dir.startswith("custom_"))
                self.assertTrue(os.path.exists(custom_dir))
            finally:
                # إعادة الدليل الحالي إلى القيمة الأصلية
                os.chdir(original_dir)
    
    @patch('subprocess.Popen')
    def test_execute_command(self, mock_popen):
        """اختبار دالة تنفيذ الأوامر"""
        # إعداد المحاكاة
        process_mock = MagicMock()
        process_mock.communicate.return_value = ("نتيجة نجاح", "")
        process_mock.returncode = 0
        mock_popen.return_value = process_mock
        
        # اختبار تنفيذ أمر ناجح
        success, output = utils.execute_command("echo test", verbose=False)
        self.assertTrue(success)
        self.assertEqual(output, "نتيجة نجاح")
        
        # إعداد المحاكاة لفشل الأمر
        process_mock.returncode = 1
        process_mock.communicate.return_value = ("", "رسالة خطأ")
        
        # اختبار تنفيذ أمر فاشل
        success, output = utils.execute_command("invalid_command", verbose=False)
        self.assertFalse(success)
        self.assertEqual(output, "رسالة خطأ")

class TestScanConfig(unittest.TestCase):
    """اختبارات لتكوين Scan"""
    
    def test_config_file_exists(self):
        """التحقق من وجود ملف التكوين"""
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
        self.assertTrue(os.path.exists(config_path), "ملف التكوين غير موجود")
    
    @patch('utils.load_config')
    def test_get_system_wordlist(self, mock_load_config):
        """اختبار دالة الحصول على قائمة الكلمات المناسبة للنظام"""
        # إعداد بيانات التكوين المزيفة
        mock_config = {
            'default_settings': {
                'default_wordlist': {
                    'windows': 'C:\\wordlists\\common.txt',
                    'linux': '/usr/share/wordlists/dirb/common.txt'
                }
            }
        }
        mock_load_config.return_value = mock_config
        
        # محاكاة وجود ملف قائمة الكلمات
        with patch('os.path.exists', return_value=True):
            with patch('platform.system', return_value='Windows'):
                wordlist = utils.get_system_wordlist(mock_config)
                self.assertEqual(wordlist, 'C:\\wordlists\\common.txt')
            
            with patch('platform.system', return_value='Linux'):
                wordlist = utils.get_system_wordlist(mock_config)
                self.assertEqual(wordlist, '/usr/share/wordlists/dirb/common.txt')

def run_tests():
    """تشغيل جميع الاختبارات"""
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
    
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("  _____                 ")
    print(" / ____|                ")
    print("| (___   ___ __ _ _ __  ")
    print(" \___ \ / __/ _` | '_ \ ")
    print(" ____) | (_| (_| | | | |")
    print("|_____/ \___\__,_|_| |_|")
    print(f"{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}[ اختبارات أداة Scan ]{Colors.ENDC}")
    print("")
    print(f"{Colors.BLUE}[*] جاري تشغيل الاختبارات...{Colors.ENDC}")
    print("")
    
    # تشغيل الاختبارات
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == "__main__":
    run_tests()