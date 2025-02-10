# Import necessary libraries for the application
import streamlit as st
import pandas as pd
import plotly.express as px


# Load the simulation results from the specified Excel sheet
# This function attempts to read data from an Excel file and returns a DataFrame.
# If the file is not found, it shows an error message in the Streamlit app.
def load_data(sheet_name):
    try:
        # Attempt to read the Excel file
        df = pd.read_excel("simulation_results.xlsx", sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        # Handle the case where the file is not found
        st.error("No results found! Run the simulation first.")
        return None


# Streamlit UI setup
st.title("🚦 AI-Powered Traffic Signal Simulation Dashboard")

# Sidebar navigation for user interface
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select Page", ["Problem Statement", "Graphical Representation"])

if page == "Problem Statement":
    # Display the problem definition
    st.header("Problem Definition")
    st.write(
        "In urban environments, inefficient traffic signal timings contribute to congestion, increased fuel consumption, and environmental pollution. The goal of this project is to develop an AI-driven approach to optimize traffic light durations based on real-time vehicle detection.")
    st.header("Approach to Solve the Problem")
    st.write(
        "The system utilizes YOLOv8 for vehicle detection, combined with LSTM-based predictive analysis. The model dynamically adjusts traffic signal timings based on real-time traffic density and predicted congestion patterns.       Additionally, an LSTM model is implemented to predict future traffic flow based on historical data. This predictive capability allows the system to anticipate congestion and adjust signal timings proactively, improving overall traffic management.")
    # Display how the system works
    st.header("How It Works")
    st.write("The AI-powered traffic signal system works through the following steps:")
    
    st.subheader("1. Vehicle Detection Using YOLOv8")
    st.write("The system processes real-time video feeds from traffic cameras using the YOLOv8 deep learning model. YOLO (You Only Look Once) is an object detection algorithm capable of identifying and classifying multiple vehicles, including cars, trucks, buses, and motorcycles, in a single frame. The detected vehicles are assigned bounding boxes, which provide precise locations of each vehicle within the frame.")
    
    st.subheader("2. Traffic Data Collection and Analysis")
    st.write("Once the vehicles are detected, the system counts the number of vehicles in each lane and categorizes them based on their type. This data is stored in a structured format, allowing for real-time monitoring of vehicle density. The traffic data is then analyzed to determine congestion levels and traffic flow patterns.")
    
    st.subheader("3. Dynamic Traffic Signal Adjustment")
    st.write("Using the collected vehicle data, an AI-based algorithm calculates the optimal duration for the green light. The more congested a lane is, the longer the green light remains active to allow traffic to pass efficiently. The system ensures that each direction receives an appropriate amount of time, preventing unnecessary delays and reducing idle vehicle time at intersections.")
    
    st.subheader("4. Continuous Learning and Optimization")
    st.write("The AI model continuously learns from historical traffic patterns using an LSTM (Long Short-Term Memory) network, a type of recurrent neural network (RNN). This allows the system to predict future congestion levels and adjust signal timings accordingly. Multiple simulations are run to fine-tune the model and optimize performance over time.")
    
    st.video("vids/10.02.2025_21.34.08_REC.mp4")  # Replace with actual video link

    # Display the demo
    st.header("Demo")
    st.write(
        "Below are demonstration videos showcasing the AI-powered traffic signal simulation in action. These videos illustrate the effectiveness of the system in managing traffic flow and optimizing signal timings.")
    # Placeholder for video links
    st.video("vids/10.02.2025_21.30.20_REC.mp4")  # Replace with actual video link

    # Display the approach to solve the problem


elif page == "Graphical Representation":
    # Display the demo
   

    st.header("Comparison of Traffic Control Approaches")
    st.write("This section compares the total vehicle counts for YOLO-based and manual traffic control approaches.")

    # Load signal results data
    signal_df = pd.read_csv("signal_results.csv")

    # Create two columns for side-by-side display
    col1, col2 = st.columns(2)

    with col1:
        # Create a bar chart for total vehicle counts
        fig_bar = px.bar(signal_df, x="Exp No", y=["Total", "Manual"],
                         title="Total Vehicle Counts: YOLO vs Manual", labels={"value": "Vehicle Count", "Exp No": "Experiment Number"})
        st.plotly_chart(fig_bar)

    with col2:
        # Create a line chart for total vehicle counts
        fig_line = px.line(signal_df, x="Exp No", y=["Total", "Manual"],
                           title="Trend of Total Vehicle Counts: YOLO vs Manual", labels={"value": "Vehicle Count", "Exp No": "Experiment Number"})
        st.plotly_chart(fig_line)

    # Select the dataset type for visualization
   

    
    st.header("Results and Conclusion")
    st.write(
        "The comparison of total vehicle counts between the YOLO-based and manual traffic control approaches demonstrates the effectiveness of the AI-driven system.\n      Key findings include:\n        - The YOLO-based approach consistently shows higher total vehicle counts across all experiments, indicating improved traffic flow management.\n        - The dynamic adjustments made by the AI system lead to reduced congestion and optimized traffic signal timings compared to the manual approach.\n        Overall, the results highlight the potential of AI technologies in enhancing urban traffic management and reducing delays.")

# Notify the user that the dashboard has successfully loaded
st.success("Dashboard successfully loaded!")
