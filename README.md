# Django Authentication System with MailHog Integration 🔒

A robust Django-based authentication system featuring user registration, login, and password reset functionality with MailHog integration for email testing.

## ✨ Features

- **User Registration** with password strength validation
- **User Login** with remember me functionality
- **Password Reset** via email verification
- **Email Testing** with MailHog integration
- **Password Strength Indicators**
- **Show/Hide Password** toggles

## 🚀 Prerequisites

- **Python** 3.10 or higher
- **pip** (Python package installer)
- **MailHog** for email testing

## 💻 Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd Authentication
```

### 2. Set up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Linux/Mac:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. MailHog Setup (Ubuntu/Linux)
```bash
# Install wget if not installed
sudo apt-get install wget

# Download MailHog
wget https://github.com/mailhog/MailHog/releases/download/v1.0.1/MailHog_linux_amd64

# Make executable and move to local bin
chmod +x MailHog_linux_amd64
sudo mv MailHog_linux_amd64 /usr/local/bin/mailhog
```

### 5. Create Development Startup Script
```bash
# Create start_dev.sh
echo '#!/bin/bash
mailhog &
python manage.py runserver' > start_dev.sh

# Make it executable
chmod +x start_dev.sh
```

## ⚙️ Configuration

### Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Admin User
```bash
python manage.py createsuperuser
```

## 🌟 Running the Application

### Start Development Servers
```bash
./start_dev.sh
```

This launches:
- 🚀 Django server: [http://localhost:8000](http://localhost:8000)
- 📧 MailHog SMTP: localhost:1025
- 📨 MailHog Web UI: [http://localhost:8025](http://localhost:8025)

## 🧪 Testing Features

### User Registration
1. Visit [http://localhost:8000/register/](http://localhost:8000/register/)
2. Complete the registration form:
   - First Name
   - Last Name
   - Username
   - Email
   - Password (watch strength indicators)
   - Confirm Password

### User Login
1. Visit [http://localhost:8000/login/](http://localhost:8000/login/)
2. Enter credentials
3. Use the eye icon to toggle password visibility

### Password Reset
1. Click "Reset it here" on login page
2. Enter email address
3. Check MailHog ([http://localhost:8025](http://localhost:8025))
4. Click reset link in email
5. Set new password

## 🔐 Password Requirements

- **Length**: 8-30 characters
- **Must contain**:
  - One uppercase letter
  - One lowercase letter
  - One number
  - One special character
- **Cannot contain**:
  - Common sequences
  - Personal information

## 🔧 Troubleshooting

### MailHog Issues
```bash
# Check for port conflicts
sudo lsof -i :1025
sudo lsof -i :8025

# Stop MailHog
pkill mailhog
```

### Server Issues
```bash
# Check port conflicts
sudo lsof -i :8000

# Stop process
kill -9 <process_id>
```

## 📁 Project Structure
```
Authentication/
├── authentication/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── password_reset.html
│       ├── password_reset_confirm.html
│       ├── password_reset_done.html
│       └── password_reset_email.html
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── start_dev.sh
```

## 🔒 Security Notes

- **Development Mode**: Debug enabled (disable in production)
- **Email**: Configure production email backend
- **Secret Key**: Move to environment variables
- **HTTPS**: Enable in production

## 💡 Development Notes

- MailHog is for **development only**
- Configure production email service
- Update password reset email templates
- Add rate limiting for password reset
- Implement proper error logging

## 👥 Contributing


## 📝 License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the license terms.

**MIT License**:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
