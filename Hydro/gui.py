import tkinter as tk
from threading import Thread
import matplotlib.pyplot as plt
from sensors import SensorManager
from controller import ControlManager

class HydroponicsGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hydroponics Control System")
        self.sensor_manager = SensorManager()
        self.control_manager = ControlManager()
        self.setup_ui()

    def setup_ui(self):
        # Create UI components
        self.temp_label = tk.Label(self.window, text="Temperature: --")
        self.temp_label.pack()

        self.humidity_label = tk.Label(self.window, text="Humidity: --")
        self.humidity_label.pack()

        self.water_quality_label = tk.Label(self.window, text="Water Quality: --")
        self.water_quality_label.pack()

        self.update_button = tk.Button(self.window, text="Update Data", command=self.update_data)
        self.update_button.pack()

        # Start background thread for real-time updates
        self.update_thread = Thread(target=self.update_sensor_data)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update_sensor_data(self):
        while True:
            temp, humidity, water_quality = self.sensor_manager.get_sensor_data()
            self.temp_label.config(text=f"Temperature: {temp:.2f} °C")
            self.humidity_label.config(text=f"Humidity: {humidity:.2f} %")
            self.water_quality_label.config(text=f"Water Quality: {water_quality:.2f} pH")
            self.window.after(1000)  # Update every second

    def update_data(self):
        # Trigger manual update if needed
        self.update_sensor_data()

    def run(self):
        self.window.mainloop()
