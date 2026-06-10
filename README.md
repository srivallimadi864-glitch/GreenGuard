🌿 GreenGuard – Smart Plant Health and Care Management System

GreenGuard is a simple web-based application developed using **Python Flask, HTML, CSS, and JavaScript**. It helps users manage their plants by storing plant details, providing watering reminders, and diagnosing common plant health problems.

The project demonstrates the practical implementation of Data Structures and Algorithms such as **Hashing, Searching, and Priority Queue (Heap)** in a real-world application.

---

## 🚀 Features

### 🌱 Plant Management
- Add new plants
- View all plants
- Store Plant ID, Plant Name, Plant Type, and Watering Frequency

### 🔍 Search Plant
- Search plants using Plant ID
- Quickly retrieve plant information

### 💧 Watering Reminder
- Displays plants that need watering first
- Prioritizes plants based on watering frequency

### 🌿 Plant Doctor
Provides diagnosis and solutions for common plant issues:

| Symptom | Cause | Solution |
|----------|---------|---------|
| Yellow Leaves | Overwatering | Reduce watering frequency |
| Brown Spots | Fungal Infection | Use fungicide |
| Slow Growth | Lack of Nutrients | Add fertilizer |

---

## 🧠 Data Structures and Algorithms Used

| DSA Concept | Purpose |
|-------------|---------|
| Hashing | Store and retrieve plant records |
| Searching | Search plants by Plant ID |
| Priority Queue (Heap) | Manage watering reminders |
| Hash Table | Map symptoms to solutions in Plant Doctor |

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python Flask

### Data Storage
- JSON File (`plants.json`)

---

## 📂 Project Structure

```text
GreenGuard/
│
├── app.py
├── plants.json
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ▶️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/GreenGuard.git
cd GreenGuard
```

### 2. Install Dependencies

```bash
pip install flask
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📋 Sample Input

```text
Plant ID: P001
Plant Name: Rose
Plant Type: Flower
Water Frequency: 2
```

---

## 📋 Sample Output

```text
Plant Added Successfully

P001 | Rose | Flower | 2
```

### Search Example

Input:

```text
P001
```

Output:

```text
Plant Found

Name: Rose
Type: Flower
```

---

## 🔄 Workflow

```text
Add Plant
     ↓
View Plants
     ↓
Search Plant
     ↓
Watering Reminder
     ↓
Plant Doctor
```

---

## 🎯 Project Objectives

- Manage plant records digitally
- Provide watering reminders
- Diagnose common plant health issues
- Demonstrate DSA concepts through a practical application
- Improve plant care and maintenance

---

## 🎓 Conclusion

GreenGuard is a user-friendly plant care management system that helps users organize plant information, receive timely watering reminders, and identify common plant health issues. The project effectively demonstrates the use of Hashing, Searching, and Priority Queue data structures in a real-world scenario.

---

## 👨‍💻 Team Members

- Srivalli Madi (2510030109)
- Meghana (2510030101)

---

### 🌱 GreenGuard – Smart Care for Healthier Plants 💚
