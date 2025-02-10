# 🚦 AI-Powered Traffic Signal Simulation

## 📌 Project Overview
This project uses **YOLO-based vehicle detection** and **LSTM-based traffic prediction** to optimize traffic light control. The simulation dynamically adjusts signal timings based on real-time vehicle counts from video feeds.

## 📂 Project Structure
```
├── simulation.py         # Main traffic simulation logic
├── run_simulation.py     # Runs the simulation 15 times and saves results to Excel
├── signal_results.csv    # Stores vehicle detection results per signal
├── simulation_results.xlsx # Aggregated results from multiple simulation runs
├── README.md             # Project documentation
```

## 🚀 Features
✅ **YOLOv8-Based Vehicle Detection**: Detects vehicles from live traffic video streams.
✅ **LSTM-Based Traffic Prediction**: Forecasts congestion patterns.
✅ **Automated Traffic Signal Control**: Adjusts green light duration dynamically.
✅ **Multiple Simulation Runs**: Executes `simulation.py` multiple times and saves data.
✅ **Excel Output**: Stores final traffic data for analysis.

## 🛠 Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/traffic-simulation.git
   cd traffic-simulation
   ```
2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Running the Project
### Run a Single Simulation
```sh
python simulation.py
```
### Run Multiple Simulations (15 times & save results to Excel)
```sh
python run_simulation.py
```

## 📊 Output
- **Real-time traffic simulation with vehicle movements**
- **Signal timing adjustments based on YOLO vehicle detection**
- **Excel report (`simulation_results.xlsx`) summarizing results**

## 🤖 Future Enhancements
- 🔹 **Integrate live traffic camera feeds** for real-world deployment.
- 🔹 **Implement Reinforcement Learning (RL)** for better signal optimization.
- 🔹 **Enhance visualization with a web-based dashboard.**

## 📜 License
This project is open-source under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! Feel free to improve the simulation logic or add new features.

## 📧 Contact
For queries or contributions, contact **your-email@example.com** or open an issue on GitHub.

---
🚦 **Optimizing Traffic, One Signal at a Time!** 🚦

