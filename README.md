# Vehicle-Management-System

# 🚗 Vehicle Management System

A simple **Python-based Vehicle Management System** that allows administrators to manage vehicles and customers to rent and return vehicles.

The project uses **Object-Oriented Programming (OOP)** concepts and **JSON file storage** to permanently save vehicle and customer information.

---

## 📌 Features

### 👨‍💼 Admin Panel

* Add new vehicles
* View all vehicles in the inventory
* Store vehicle details such as:

  * Vehicle Number
  * Brand
  * Type
  * Rent
  * Availability Status
* Prevent duplicate vehicle numbers
* Validate vehicle input

### 👤 Customer Panel

* Register new customers
* View available vehicles
* Rent a vehicle
* Return a rented vehicle
* Prevent customers from renting multiple vehicles
* Validate customer and vehicle IDs

### 💾 Data Storage

* Uses `data.json` for permanent data storage
* Vehicle and customer information is automatically saved
* Data is loaded automatically when the program starts
* No database is required

### 🛡️ Error Handling

The project includes exception handling for:

* Empty input
* Duplicate vehicle/customer IDs
* Invalid vehicle/customer IDs
* Invalid rent values
* Already rented vehicles
* Customers without rented vehicles
* Invalid JSON data
* Missing data files
* Keyboard interruption

---

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming**
* **JSON**
* **Exception Handling**
* **File Handling**
* **Python Dictionaries**

---

## 📂 Project Structure

```text
vehicle_management_system/
│
├── main.py
├── storage.py
├── data.json
├── README.md
│
└── src/
    ├── __init__.py
    ├── admin.py
    └── customer.py
```

---

## 📄 File Description

### `main.py`

The main entry point of the application.

It provides:

* Main menu
* Admin menu
* Customer menu
* User input handling
* Connection between admin, customer, and storage modules

---

### `src/admin.py`

Contains the `admin_panel` class.

Responsible for:

* Adding vehicles
* Viewing vehicle inventory
* Vehicle validation
* Managing vehicle information

---

### `src/customer.py`

Contains the `customerpanel` class.

Responsible for:

* Customer registration
* Displaying available vehicles
* Renting vehicles
* Returning vehicles

---

### `storage.py`

Handles permanent data storage using JSON.

It contains:

```python
load_data()
```

Used to load vehicle and customer data from `data.json`.

And:

```python
save_data()
```

Used to save updated vehicle and customer data into `data.json`.

---

### `data.json`

Stores the application's data permanently.

Initial structure:

```json
{
    "vehicles": {},
    "customers": {}
}
```

The application automatically updates this file when vehicles or customers are added or when rental information changes.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd vehicle_management_system
```

### 3. Run the application

```bash
python main.py
```

If your system uses a specific Python command:

```bash
python3 main.py
```

---

## 🎮 How the Application Works

When the program starts, you will see:

```text
------------------------------
🎉 Welcome to Janani Rentals 🎉
------------------------------
Choose an Option:
1. Admin Panel
2. Customer Panel
3. Exit
```

### Admin Workflow

```text
Admin Panel
     │
     ├── Add Vehicle
     │      ↓
     │   Vehicle details
     │      ↓
     │   Save to JSON
     │
     └── View Inventory
```

### Customer Workflow

```text
Customer Panel
     │
     ├── Register Customer
     │
     ├── View Available Vehicles
     │
     ├── Rent Vehicle
     │      ↓
     │   Vehicle → Rented
     │
     └── Return Vehicle
            ↓
        Vehicle → Available
```

---

## 💡 Example Vehicle Data

After adding a vehicle, the `data.json` file may look like:

```json
{
    "vehicles": {
        "TN01AB1234": {
            "number": "TN01AB1234",
            "Brand": "Toyota",
            "Type": "Car",
            "Rent": 1500.0,
            "available": true
        }
    },
    "customers": {}
}
```

After registering a customer:

```json
{
    "vehicles": {
        "TN01AB1234": {
            "number": "TN01AB1234",
            "Brand": "Toyota",
            "Type": "Car",
            "Rent": 1500.0,
            "available": true
        }
    },
    "customers": {
        "C001": {
            "customername": "Janani",
            "rent_vehicle": null
        }
    }
}
```

When the customer rents the vehicle:

```json
"available": false
```

and the customer's rented vehicle is stored using:

```json
"rent_vehicle": "TN01AB1234"
```

When the vehicle is returned:

```json
"available": true
```

and:

```json
"rent_vehicle": null
```

---

## 🧠 Concepts Practiced

This project was created to practice several Python concepts:

* Classes and Objects
* Constructors (`__init__`)
* Methods
* Dictionaries
* Functions
* Loops
* Conditional Statements
* `try` / `except`
* `raise`
* `KeyboardInterrupt`
* File Handling
* JSON Serialization
* Modules and Packages
* Importing Classes and Functions
* Persistent Data Storage

---

## 🔐 Data Persistence

One of the main features of this project is **persistent storage**.

Without JSON:

```text
Program starts
     ↓
Data created
     ↓
Program closes
     ↓
Data is lost ❌
```

With JSON:

```text
Program starts
     ↓
Load data.json
     ↓
Use vehicle/customer data
     ↓
Make changes
     ↓
Save data.json
     ↓
Program closes
     ↓
Data remains available ✅
```

---

## 🚀 Future Improvements

Possible improvements for future versions:

* Add vehicle deletion
* Add customer deletion
* Add rental history
* Calculate total rental cost based on rental duration
* Add login authentication for admin
* Add search functionality
* Add vehicle categories
* Add payment tracking
* Replace JSON storage with a database such as SQLite or MySQL
* Create a graphical user interface (GUI)
* Add automated tests

---

## 👩‍💻 Author

**Veeramma Janani k**

Python learning project focused on practicing **OOP, file handling, JSON storage, and exception handling**.

---

## ⭐ Project Status

**Completed – Basic Version**

More features can be added in future versions as the project evolves.
