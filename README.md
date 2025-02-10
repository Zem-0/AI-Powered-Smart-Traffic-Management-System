# 🚦 AI-Powered Traffic Signal Simulation

## 📌 Problem Statement
Traditional traffic signals operate on fixed timers, leading to inefficiencies such as unnecessary waiting times and congestion. This project aims to develop an **AI-powered adaptive traffic management system** that dynamically adjusts signal timings based on real-time traffic conditions detected using YOLOv8.
### Implementation Details

This project can be broken down into 3 modules:

1. `Vehicle Detection Module` - This module is responsible for detecting the number of vehicles in the image received as input from the camera. More specifically, it will provide as output the number of vehicles of each vehicle class such as car, bike, bus, truck, and rickshaw.

2. `Signal Switching Algorithm` - This algorithm updates the red, green, and yellow times of all signals. These timers are set bases on the count of vehicles of each class received from the vehicle detection module and several other factors such as the number of lanes, average speed of each class of vehicle, etc. 

3. `Simulation Module` - A simulation is developed from scratch using [Pygame](https://www.pygame.org/news) library to simulate traffic signals and vehicles moving across a traffic intersection.

Read more about object detection model used, working of the algorithm, and development of simulation
## 🚀 Features
✅ **YOLOv8-Based Vehicle Detection**: Detects vehicles from live traffic video streams.
✅ **LSTM-Based Traffic Prediction**: Forecasts congestion patterns.
✅ **Automated Traffic Signal Control**: Adjusts green light duration dynamically.
✅ **Multiple Simulation Runs**: Executes `simulation.py` multiple times and saves data.
✅ **Excel Output**: Stores final traffic data for analysis.

## 🛠 How It Works
1. **Vehicle Detection**: YOLOv8 detects vehicles from live video feeds.
🎥 [Watch the Object detection demo](vids/10.02.2025_21.34.08_REC.mp4)

2. **Traffic Data Processing**: The detected vehicle counts are stored and analyzed.
3. **Signal Adjustment**: Based on vehicle density, green light durations are dynamically set.
4. **Prediction with LSTM**: Future congestion trends are forecasted.
5. **Simulation Execution**: The traffic signal model is tested through multiple runs.
6. **Result Storage**: Final data is saved in an Excel sheet for further analysis

## 📊 Demo and Results
- **Real-time traffic simulation with vehicle movements**
- **Signal timing adjustments based on YOLO vehicle detection**
- **Excel report (`simulation_results.xlsx`) summarizing results**
🎥 [Watch the Traffic Simulation Demo](vids/10.02.2025_21.30.20_REC.mp4)



## 📂 Project Structure
```
├── simulation.py         # Main traffic simulation logic
├── run_simulation.py     # Runs the simulation 15 times and saves results to Excel
├── signal_results.csv    # Stores vehicle detection results per signal
├── simulation_results.xlsx # Aggregated results from multiple simulation runs
├── README.md             # Project documentation
```

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

