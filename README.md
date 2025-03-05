# 🎉 Birthday Wisher Bot

A Python script that automatically sends personalized birthday wishes via email.

## ✨ Features
- Reads birthday data from a **CSV file**.
- Chooses a **random letter template** to personalize the greeting.
- Sends an **automated email** on the recipient’s birthday.

---

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required library:

```bash
pip install pandas
```

---

### 2️⃣ Configure Email Credentials
In the script, update the following variables with your **email credentials**:

```python
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
```

🔹 If you’re using **Gmail**, you must enable **App Passwords** (instead of using your real password).  
🔹 If you’re using another provider (Yahoo, Outlook, etc.), check their **SMTP settings**.

---

### 3️⃣ Prepare the Data

#### 📂 Create `birthdays.csv`
Ensure a CSV file exists with the following format:

```csv
name,email,year,month,day
John Doe,johndoe@example.com,1990,03,02
Jane Smith,janesmith@example.com,1985,07,15
```

Each row represents a person’s **name, email, and birthdate**.

#### 📝 Create `letter_templates/`
Inside this folder, add **letter templates** like:

📄 `letter_1.txt`
```
Dear [NAME],

Wishing you a fantastic birthday filled with love and joy! 🎉

Best wishes,  
Your Friend
```

The script will replace `[NAME]` with the recipient’s actual name.

---

### 4️⃣ Run the Script

Execute the script manually:

```bash
python birthday_wisher.py
```

OR schedule it to run **daily**:
- **Windows (Task Scheduler)**
- **Linux/macOS (Cron Job)**

---

## 🚀 How It Works

1. **Loads `birthdays.csv`** and checks if today matches any birthdays.
2. **Selects a random letter template** from `letter_templates/`.
3. **Replaces `[NAME]`** with the recipient’s name.
4. **Sends an email** using `smtplib`.

---

## 🔒 Security Tips
- **Use App Passwords** instead of your real email password.
- Consider **storing credentials** in **environment variables** instead of hardcoding them.

