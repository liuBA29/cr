# CRM System for Transport & Logistics

## 🌎 Project Description (English)

**A CRM system for a transport and logistics company**, developed using Django and Django REST Framework.

This project handles client and partner management (customers, carriers, third-party companies), deal tracking, quotation handling, document storage, profit calculation, and data filtering over time.

### 💼 Core Features:

* Management of **counterparties** (clients, carriers, third-party companies)
* Creation and editing of **deals** (up to 10 carriers per deal, each with prices, currencies, and comments)
* Handling **quotations** with client/supplier data
* **Document management**: upload, filter by type and entity
* **Profit calculation** in euros using custom currency conversion
* **Date filtering**: week, quarter, half-year, or custom ranges
* Full-text **search** and **report export** (TXT format)
* Interactive **calendar** view with monthly overview

### 🛠️ Technologies Used:

* Python 3, Django, Django REST Framework (DRF)
* SQLite or PostgreSQL
* HTMLCalendar, dateutil / relativedelta
* Django ORM: `Q`, `F`, `annotate`, `aggregate`, `raw SQL`
* File handling: `FileSystemStorage`, `FileField`
* Custom module: `currency_parcer.py`

### 🧠 Architecture Highlights:

* Model inheritance (`Contragent`, `Operation`)
* Extended deal model: 10 carriers, directions, and dates per deal
* Classic Django views (`ListView`, `DetailView`, `FormView`)
* Separated filtering and display logic
* DRF integration prepared for future API extensions

---
