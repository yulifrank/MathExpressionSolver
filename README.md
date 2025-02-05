
# 🧮 **פרויקט מערכת פתרון ביטויים מתמטיים** 🧮

## 📖 **תיאור כללי**
המערכת מיועדת לפתרון ביטויים מתמטיים באמצעות מבנה נתונים של **עץ ביטוי**. המערכת מבצעת פתרון ביטויים מתמטיים בפייתון, תוך שימוש באלגוריתם **Shunting Yard** להמיר ביטוי לפוסטפיקס, ולאחר מכן בונה את עץ הביטוי. בסופו של תהליך, המערכת מבצעת את החישוב ומחזירה את התוצאה.

המערכת תומכת בביצוע פעולות חשבון בסיסיות:
- חיבור (+)
- חיסור (-)
- כפל (*)
- חילוק (/)

## ⚙️ **כיצד להשתמש?**
1. הורד את הקוד על ידי שיבוץ **הקוד בשורת פקודה:**
```bash
git clone https://github.com/username/project-name.git
```

2. התקן את התלויות (אם ישנן) על ידי הרצת הפקודה הבאה:
```bash
pip install -r requirements.txt
```

3. השתמש במערכת על ידי קריאה לפונקציה `parse_expression()` עם הביטוי המתמטי שאתה רוצה לפתור. לדוגמה:
```python
expr = "10 * 4 + (5 - 3)"
result = parse_expression(expr)
print(f"תוצאת הביטוי '{expr}' היא {result}")
```

## 💡 **הסבר על העבודה**
המערכת בנויה ממספר מחלקות:
- **Num**: מייצגת מספר וכוללת פונקציה לחישוב התוצאה שלה.
- **BinExp**: מחלקת בסיס לפעולות בינאריות (חיבור, חיסור, כפל, חילוק).
- **Plus, Minus, Mul, Div**: כל אחת מהן מייצגת פעולה מתמטית ומבצעת את החישוב המתאים.

### איך זה עובד?
- המערכת מקבלת ביטוי מתמטי כקלט, מפרקת אותו למילים, ומבצעת המרה לפוסטפיקס בעזרת אלגוריתם **Shunting Yard**.
- לאחר מכן, הביטוי הפוסטפקסי מומר לעץ ביטויים על ידי **build_expression_tree()**.
- התוצאה מחושבת על ידי קריאה ל-`calc()` של המחלקות השונות.

## 🛠 **מבנה הפרויקט**
- **Minus.py** - מחלקה המייצגת חיסור
- **Mul.py** - מחלקה המייצגת כפל
- **Num.py** - מחלקה המייצגת מספר
- **Plus.py** - מחלקה המייצגת חיבור
- **Div.py** - מחלקה המייצגת חילוק

## 🔧 **התקנה**
לא נדרש התקנה מיוחדת. כל מה שאתה צריך זה את הגרסה האחרונה של פייתון!

## 📌 **דוגמה לשימוש**
ביטוי: `"10 * 4 + (5 - 3)"`

הקוד:
```python
expr = "10 * 4 + (5 - 3)"
result = parse_expression(expr)
print(f"תוצאת הביטוי '{expr}' היא {result}")
```

פלט:
```
תוצאת הביטוי '10 * 4 + (3- 5)' היא 42
```

## 🎨 **אפשרויות הרחבה**
- ניתן להוסיף תמיכה בפעולות מתקדמות נוספות כמו חזקות, שורש ריבועי ועוד.
- ניתן לשדרג את המערכת כך שתתמוך בשפות תכנות נוספות.

## 📝 **הערות**
אם יש לך רעיונות לשיפורים או בקשות נוספות, אל תהסס ליצור קשר ולהשאיר פידבק!
