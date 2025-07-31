# التوثيق التقني لأداة Scan

## نظرة عامة

Scan هي أداة قوية وثورية تجمع بين أدوات اختبار الاختراق الشائعة في واجهة موحدة وسهلة الاستخدام. تم تطويرها بواسطة SayerLinux، وتهدف إلى تبسيط عملية اختبار الاختراق من خلال دمج الأدوات التالية:

- **wapiti**: أداة فحص ثغرات تطبيقات الويب
- **WpScan**: أداة فحص أمان WordPress
- **dirsearch**: أداة اكتشاف المسارات والملفات
- **gobuster**: أداة اكتشاف المسارات والملفات بسرعة عالية
- **FFUF**: أداة فحص الويب المرنة والسريعة

## هيكل المشروع

```
Scan/
├── scan.py                # الملف الرئيسي للأداة
├── utils.py               # دوال مساعدة
├── config.json            # ملف التكوين
├── install.py             # ملف تثبيت الأدوات المطلوبة
├── check_dependencies.py  # ملف التحقق من الاعتماديات
├── test.py                # ملف الاختبارات
├── run_scan.bat           # ملف تنفيذي لنظام Windows
├── run_scan.sh            # ملف تنفيذي لنظام Linux
├── README.md              # ملف الشرح الرئيسي
├── DOCUMENTATION.md       # التوثيق التقني
├── CONTRIBUTING.md        # إرشادات المساهمة
├── LICENSE                # ملف الترخيص
└── .gitignore             # ملف تجاهل Git
```

## المكونات الرئيسية

### scan.py

الملف الرئيسي للأداة الذي يحتوي على الدالة الرئيسية ودوال تشغيل الأدوات المختلفة. يقوم هذا الملف بما يلي:

1. عرض شعار الأداة
2. تحليل معلمات سطر الأوامر
3. التحقق من وجود الأدوات المطلوبة
4. إنشاء مجلد للنتائج
5. تشغيل الأدوات المحددة
6. عرض النتائج

### utils.py

يحتوي على دوال مساعدة تستخدم في جميع أنحاء المشروع، مثل:

1. التحقق من صحة عنوان URL
2. التحقق من وجود الأدوات
3. إنشاء مجلدات للنتائج
4. تنفيذ الأوامر
5. التحقق من اتصال الإنترنت
6. إنشاء تقارير ملخصة

### config.json

ملف التكوين الذي يحتوي على الإعدادات الافتراضية للأداة، مثل:

1. مجلد الإخراج الافتراضي
2. قائمة الكلمات الافتراضية
3. إعدادات كل أداة
4. معلومات المؤلف

### install.py

ملف لتثبيت الأدوات المطلوبة على أنظمة التشغيل المختلفة. يقوم بما يلي:

1. التحقق من نظام التشغيل
2. التحقق من الأدوات المثبتة بالفعل
3. تثبيت الأدوات المفقودة
4. عرض تعليمات التثبيت اليدوي عند الحاجة

### check_dependencies.py

ملف للتحقق من وجود جميع المتطلبات اللازمة لتشغيل الأداة. يقوم بما يلي:

1. التحقق من إصدار Python
2. التحقق من حزم Python المطلوبة
3. التحقق من الأدوات الخارجية
4. التحقق من ملف التكوين
5. التحقق من قوائم الكلمات

## تفاصيل التنفيذ

### معالجة معلمات سطر الأوامر

تستخدم الأداة مكتبة `argparse` لمعالجة معلمات سطر الأوامر. المعلمات المدعومة هي:

- `-u, --url`: عنوان URL المستهدف (مطلوب)
- `-o, --output`: مجلد الإخراج (اختياري، الافتراضي: "results")
- `-w, --wordlist`: قائمة الكلمات للاستخدام مع gobuster و FFUF (اختياري)
- `--wapiti`: تشغيل wapiti فقط
- `--wpscan`: تشغيل WpScan فقط
- `--dirsearch`: تشغيل dirsearch فقط
- `--gobuster`: تشغيل gobuster فقط
- `--ffuf`: تشغيل FFUF فقط

### تنفيذ الأدوات

كل أداة يتم تنفيذها باستخدام وحدة `subprocess` لتشغيل الأوامر الخارجية. يتم تخزين نتائج كل أداة في ملف منفصل داخل مجلد النتائج.

#### wapiti

```python
def run_wapiti(url, output_dir):
    output_file = os.path.join(output_dir, "wapiti_results.html")
    command = f"wapiti -u {url} -o {output_file} -f html"
    return execute_command(command)
```

#### WpScan

```python
def run_wpscan(url, output_dir):
    output_file = os.path.join(output_dir, "wpscan_results.txt")
    command = f"wpscan --url {url} --output {output_file}"
    return execute_command(command)
```

#### dirsearch

```python
def run_dirsearch(url, output_dir):
    output_file = os.path.join(output_dir, "dirsearch_results.txt")
    command = f"dirsearch -u {url} -o {output_file}"
    return execute_command(command)
```

#### gobuster

```python
def run_gobuster(url, output_dir, wordlist):
    output_file = os.path.join(output_dir, "gobuster_results.txt")
    command = f"gobuster dir -u {url} -w {wordlist} -o {output_file}"
    return execute_command(command)
```

#### FFUF

```python
def run_ffuf(url, output_dir, wordlist):
    output_file = os.path.join(output_dir, "ffuf_results.json")
    command = f"ffuf -u {url}/FUZZ -w {wordlist} -o {output_file} -of json"
    return execute_command(command)
```

### إدارة النتائج

يتم إنشاء مجلد للنتائج باستخدام الدالة `create_output_directory` التي تقوم بإنشاء مجلد باسم يتضمن الطابع الزمني الحالي. يتم تخزين نتائج كل أداة في ملف منفصل داخل هذا المجلد.

```python
def create_output_directory(base_dir="results"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{base_dir}_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
```

### حفظ النتائج تلقائياً في ملف واحد

تم إضافة ميزة حفظ جميع نتائج الفحص تلقائياً في ملف واحد شامل باستخدام الدالة `save_combined_results`. تقوم هذه الدالة بتجميع نتائج جميع الأدوات المستخدمة وحفظها في ملف واحد يسمى `combined_results.txt` داخل مجلد النتائج.

```python
def save_combined_results(url, output_dir, tools_run):
    combined_file = os.path.join(output_dir, "combined_results.txt")
    
    with open(combined_file, 'w', encoding='utf-8') as f:
        # كتابة معلومات الفحص
        f.write(f"الهدف: {url}\n")
        f.write(f"تاريخ الفحص: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"الأدوات المستخدمة: {', '.join(tools_run)}\n\n")
        
        # قراءة وتضمين نتائج كل أداة
        for tool in tools_run:
            f.write(f"نتائج {tool}:\n")
            # قراءة ملف نتائج الأداة وإضافته إلى الملف المجمع
    
    return combined_file
```

يتم استدعاء هذه الدالة في نهاية الدالة الرئيسية `main()` بعد تشغيل جميع الأدوات المحددة، مما يضمن حفظ جميع النتائج في ملف واحد شامل بشكل تلقائي.

## التوافق مع أنظمة التشغيل

تم تصميم الأداة للعمل على أنظمة التشغيل التالية:

- **Linux**: مدعوم بالكامل، مع إمكانية التثبيت التلقائي للأدوات
- **Windows**: مدعوم، ولكن يتطلب التثبيت اليدوي للأدوات
- **macOS**: مدعوم جزئيًا، يتطلب التثبيت اليدوي للأدوات

## التوسعة

### إضافة أداة جديدة

لإضافة أداة جديدة إلى Scan، يجب اتباع الخطوات التالية:

1. إضافة الأداة إلى قائمة الأدوات في دالة `check_tools` في ملف `utils.py`
2. إضافة دالة لتشغيل الأداة في ملف `scan.py`
3. إضافة معلمة سطر أوامر جديدة في دالة `main` في ملف `scan.py`
4. إضافة إعدادات الأداة في ملف `config.json`
5. تحديث ملف `README.md` و `DOCUMENTATION.md` لتوثيق الأداة الجديدة

### تخصيص الإعدادات

يمكن تخصيص إعدادات الأداة من خلال تعديل ملف `config.json`. يمكن تغيير الإعدادات الافتراضية مثل مجلد الإخراج وقائمة الكلمات وخيارات كل أداة.

## الاختبارات

يحتوي المشروع على ملف `test.py` الذي يتضمن اختبارات وحدة للتحقق من صحة الدوال المختلفة. يمكن تشغيل الاختبارات باستخدام الأمر التالي:

```bash
python test.py
```

## المساهمة

نرحب بالمساهمات في تحسين وتطوير أداة Scan. يرجى الاطلاع على ملف `CONTRIBUTING.md` للحصول على إرشادات المساهمة.

## الترخيص

تم ترخيص هذا المشروع تحت رخصة MIT. يرجى الاطلاع على ملف `LICENSE` للحصول على مزيد من المعلومات.

## المؤلف

- **SayerLinux**
- البريد الإلكتروني: SaudiSayer@gmail.com