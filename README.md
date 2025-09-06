# Note-Taking Web App

A simple note-taking web application deployed on **AWS EC2** with **MariaDB** and automated backups.  

---

## Features
- Submit and view notes with timestamps  
- MariaDB database storage  
- Gunicorn + systemd deployment for production  
- Automated database backups to an **EBS volume**  

---

## Tech Stack
- Python 3 + Flask  
- MariaDB  
- AWS EC2 (RHEL 9)  
- Gunicorn  
- systemd service  
- Bash for backup automation  

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/note-app.git
cd note-app
