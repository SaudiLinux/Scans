تعليمات تثبيت الأدوات على نظام لينكس
=================================

1. تثبيت الأدوات على نظام Kali Linux
--------------------------------
بما أن Kali Linux يأتي مع معظم أدوات الاختراق مثبتة مسبقاً، يمكنك تثبيت جميع الأدوات المطلوبة بأمر واحد:

```
sudo apt update && sudo apt install -y wapiti wpscan dirsearch gobuster ffuf
```

2. تثبيت الأدوات على نظام Ubuntu/Debian
-----------------------------------

أ. تحديث قائمة الحزم وتثبيت المتطلبات الأساسية:
```
sudo apt update
sudo apt install -y python3-pip ruby-full golang
```

ب. تثبيت الأدوات المعتمدة على Python:
```
pip3 install wapiti3 dirsearch
```

ج. تثبيت WPScan (يتطلب Ruby):
```
gem install wpscan
```

د. تثبيت الأدوات المعتمدة على Go:
```
go install github.com/OJ/gobuster/v3@latest
go install github.com/ffuf/ffuf@latest
```

ه. إضافة مسار Go bin إلى متغيرات النظام:
```
echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc
source ~/.bashrc
```

3. التحقق من التثبيت
------------------
بعد اكتمال عملية التثبيت، يمكنك التحقق من تثبيت جميع الأدوات باستخدام الأوامر التالية:

```
wapiti --version
wpscan --version
dirsearch --version
gobuster version
ffuf -V
```

4. ملاحظات هامة
-------------
- تأكد من تشغيل الأوامر بصلاحيات المستخدم المناسبة (sudo عند الحاجة)
- قد تحتاج إلى إعادة تشغيل الطرفية بعد تثبيت الأدوات لتحديث متغيرات النظام
- في حال واجهت مشاكل في التثبيت، تأكد من:
  * اتصالك بالإنترنت
  * صلاحيات المستخدم
  * تثبيت جميع المتطلبات الأساسية

5. حل المشاكل الشائعة
------------------
أ. إذا واجهت مشكلة في تثبيت WPScan:
```
sudo gem install wpscan
```

ب. إذا واجهت مشكلة في تثبيت الأدوات المعتمدة على Python:
```
pip3 install --user wapiti3 dirsearch
```

ج. إذا واجهت مشكلة في تثبيت الأدوات المعتمدة على Go:
```
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

للمزيد من المعلومات والمساعدة، يرجى زيارة:
https://github.com/SayerLinux/Scan