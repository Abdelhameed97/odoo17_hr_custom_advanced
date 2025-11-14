# Odoo 17 – HR Custom Module (Employee Grade, Employee Records & Basic HR Enhancements)

## 📌 Project Overview

This project is a **custom Odoo 17 HR module** designed to enhance the Human Resources capabilities by adding new fields, improving employee data structure, and preparing the system for further HR features.  
The goal of this project is to simulate a **real-world Odoo development environment**, following professional development practices including models, views, security rules, and module structure.

---

## 📁 Module Name

`hr_employee_grade`

---

## 🚀 Features Implemented

### 1️⃣ Added a New Field: Employee Grade

- Created a new field `grade` inside the employee model `hr.employee`.
- The field stores the employee’s job grade/level.
- Implemented using `fields.Char()`.

### 2️⃣ Enhanced Employee Profile Form

- Modified the employee form view to show the new **Employee Grade** field.
- Added the field inside the _HR Settings_ tab.
- Ensured seamless integration with native Odoo UI.

### 3️⃣ Module Initialization

- Structured the module following Odoo best practices:
  - `data/`
  - `models/`
  - `reports/`
  - `security/ir.model.access.csv`
  - `views/`
  - `__init__.py`
  - `__manifest__.py`

### 4️⃣ Full Installation Workflow

- Installed as a standalone module.
- Automatically adds the new field once installed.
- Fully upgrade-safe and compatible with Odoo 17 Community.

---

## 📂 Project Structure

```
hr_employee_grade/
│
├── data/
│   └──
│
├── models/
│   └── employee.py
│
├── reports/
│   └──
│
├── security/
│   └── ir.model.access.csv
│
├── views/
│   └── hr_employee_views.xml
│
├── __init__.py
├── __manifest__.py

```

---

## 🔧 Technical Details

### Employee Grade Field

```python
grade = fields.Char()
```

### View Inheritance

```xml
<field name="grade"/>
```

### Model Extension

```python
class Employee(models.Model):
    _inherit = 'hr.employee'
```

---

## 📘 Installation

1. Clone the repository into your Odoo `addons` folder.
2. Restart the Odoo server.
3. Activate **Developer Mode**.
4. Go to **Apps** → Update Apps List.
5. Search for **HR Employee Grade** and install.

---

## 📄 Future Enhancements (Next Tasks)

- Employee promotion history.
- Grade salary rules.
- Approval workflow for grade changes.
- Reporting dashboard for HR managers.

---

## 📞 Contact

For any questions or contributions, feel free to reach out.
