# 🧰 Python Job Scraper (Indeed + PostgreSQL)

A command-line application that scrapes job listings from [Indeed.com](https://www.indeed.com), stores them in a PostgreSQL database, and lets you view and filter the results using flexible CLI options.

---

## 📌 Features

- Scrapes job listings (title, company, location, posting date, and link) from Indeed
- Saves job data in a PostgreSQL database
- Securely uses a `.env` file to manage DB credentials
- Command-line interface to view and filter jobs by:
  - Company
  - Keyword in title
  - Location
  - Limit on results

---

## 📦 Dependencies 

- requests
- beautifulsoup4
- psycopg2
- python-dotenv
- pandas


## 🚀 Usage

## 🔐 Environment Variables

Create a .env file in the project root with the following content:

- DB_NAME=your_db_name
- DB_USER=your_db_user
- DB_PASSWORD=your_db_password
- DB_HOST=localhost
- DB_PORT=5432
