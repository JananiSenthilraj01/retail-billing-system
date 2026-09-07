# 🛍️ RetailNova – AI Retail Store Manager Copilot

RetailNova is an AI-powered retail management assistant built for the **NexusTiQ 24 GenAI Hackathon**. It helps small retail store managers make faster and smarter business decisions using natural language. Instead of reading multiple sales and inventory reports, managers can simply ask questions like *"Which products are running out of stock?"* or *"What sold the most this month?"* and receive instant insights.

---

## 🚀 Project Overview

RetailNova combines **Artificial Intelligence**, **data analytics**, and **a conversational chatbot** into one simple web application.

The application analyzes sales, stock, revenue, and product information from retail datasets and provides intelligent answers through a chat interface.

### Problem Statement

Small retail store managers often spend time checking spreadsheets and reports to understand:

* Low stock products.
* Overstocked inventory.
* Monthly sales performance.
* Best-selling products.
* Revenue trends.

RetailNova solves this by providing an AI Copilot that understands plain English questions.

---

## ✨ Features

* 🤖 AI-powered Retail Chatbot.
* 📦 Detect low-stock products.
* 📈 Identify overstocked inventory.
* 💰 Monthly sales and revenue analysis.
* 🔥 Best-selling and worst-selling products.
* 📊 Product performance insights.
* 💬 Ask questions in natural language.
* 🎨 Clean and responsive dashboard.

---

## 🛠️ Tech Stack

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| HTML        | Web page structure        |
| CSS         | Styling and responsive UI |
| JavaScript  | Frontend functionality    |
| Python      | Backend processing        |
| Flask       | Web framework             |
| Pandas      | Data analysis             |
| OpenAI API  | AI chatbot and insights   |
| CSV Dataset | Sales and inventory data  |

---

## 📁 Project Structure

```text
RetailNova/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── data/
│   ├── products.csv
│   ├── sales.csv
│   └── inventory.csv
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/RetailNova.git
```

### 2. Open Project Folder

```bash
cd RetailNova
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Add OpenAI API Key

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key_here
```

### 7. Run the Application

```bash
python app.py
```

Open the browser.

```text
http://127.0.0.1:5000
```

---

## 💬 Sample Questions

Ask RetailNova questions like:

* Which products are running low on stock?
* Show me the top 5 selling products this month.
* Which items are overstocked?
* What is today's total revenue?
* Which category generated the highest sales?
* Compare this month's sales with last month.

---

## 📊 AI Insights

RetailNova automatically provides:

* Low Stock Alerts.
* Overstock Recommendations.
* Sales Summary.
* Revenue Insights.
* Product Performance Report.
* Inventory Status.

These insights help store managers take quick business decisions.

---

## 🎯 Hackathon Objective

This project was developed for the **NexusTiQ 24 Solo GenAI Hackathon**.

**Goal:** Build an AI Copilot that transforms retail sales and inventory data into actionable business insights using Generative AI.

---

## 📸 Project Screenshots

Add screenshots inside the `screenshots` folder.

```text
screenshots/
├── dashboard.png
├── chatbot.png
├── inventory.png
└── sales-analysis.png
```

Then include them in GitHub.

```md
![Dashboard](screenshots/dashboard.png)

![Chatbot](screenshots/chatbot.png)
```

---

## 🌟 Future Improvements

* Voice-enabled retail assistant.
* Sales forecasting using AI.
* Demand prediction.
* Multi-store comparison dashboard.
* PDF and Excel report generation.
* WhatsApp notification for stock alerts.

---

## 👩‍💻 Author

**Janani Senthilraj**

B.Tech Student | AI & Web Development Enthusiast

Project created for the **NexusTiQ 24 GenAI Hackathon**.

---

## 📄 License

This project is developed for educational and hackathon purposes.
