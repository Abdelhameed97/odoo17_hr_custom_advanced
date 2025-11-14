# Odoo 17 – Advanced HR Custom Module

## 📌 Project Overview

This project is a **custom Odoo 17 HR module** named hr_custom_advanced, designed to enhance employee management by adding new employee information fields, improving the HR data structure, and extending the employee form view with additional pages.

The module simulates **real-world Odoo development**, using proper structure, view inheritance, access rights, and clean Python/XML code.

---

## 📁 Module Name

`hr_custom_advanced`

---

## 🚀 Features Implemented

### 1️⃣ Added New HR Fields

#### Extended the hr.employee model with three new fields:

- Created new fields `personal_code`, `emergency_contact`, `iqama_number` inside the employee model `hr.employee`.
- These fields were added via model inheritance in Python.
- Implemented using `fields.Char()`.

### 2️⃣ Extended Employee Form View

- Added a new page named "Extra Info" inside the Employee form (hr.employee).
- Displayed all newly added fields inside a structured group.
- Used proper inherit_id and xpath replacement principles.

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
│
└──__manifest__.py

```

---

## 🔧 Technical Details

### Employee Fields

```python
personal_code = fields.Char()
emergency_contact = fields.Char()
iqama_number = fields.Char()
```

### View Inheritance

```xml
<notebook position="inside">
    <page string="Extra Info">
        <group>
            <field name="personal_code"/>
            <field name="emergency_contact"/>
            <field name="iqama_number"/>
        </group>
    </page>
</notebook>
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
5. Search for **HR Custom Advanced** and install.

---

## 📄 Future Enhancements

This module is designed to grow. Planned enhancements:

- Employee family information model
- Iqama expiry reminder automation
- Emergency contact validation
- Employee documents management
- Custom HR reports
- Full HR Dashboard

---

## 📞 Contact

For any questions or contributions, feel free to reach out.
