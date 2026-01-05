# NikoFlow — App Usage Tracker

NikoFlow is a **desktop application usage tracker** built with **CustomTkinter** that monitors which applications you use, how long you use them, and presents the data in a clean, modern dashboard.

It runs locally, stores data in JSON files, and provides both **real-time monitoring** and **historical usage breakdowns** — all without external analytics or cloud services.

---

## Features

### 🔴 Live App Tracking
- Detects the **currently active application**
- Tracks usage time **per second**
- Automatically switches when you change windows
- Pauses tracking during inactivity (idle detection)

### 📊 Real-Time Dashboard
- Displays:
  - Currently active app
  - Top-used apps for today
  - Visual progress bars per app
- Updates automatically without freezing the UI

### 🕒 Daily Usage History
- Tracks usage **per day**
- Stores usage data by date
- View total screen time for the **last 7 days**

### 🗂 App Categories
- Assign apps to categories such as:
  - Coding
  - Browsing
  - Gaming
- Categories are persisted in a configuration file

### 💾 Persistent Local Storage
- Usage data saved to JSON
- Categories stored separately
- Automatic periodic saving
- Safe shutdown handling

### 🧵 Background Tracking Engine
- Usage tracking runs in a **background thread**
- UI remains responsive at all times
- Thread-safe data handling with locks

---

## Tech Stack

- **Python**
- **CustomTkinter** (modern UI)
- **pygetwindow** (active window detection)
- Python standard libraries:
  - `json`
  - `time`
  - `threading`
  - `datetime`
  - `pathlib`

---

## Requirements

Install the required dependencies before running the app:

```bash
pip install customtkinter pygetwindow
