import dspy

class WeatherReport(dspy.Predict):
    def __init__(self):
        super().__init__(signature="temp, city -> summary")

    def forward(self, temp:str, city:str) -> str:
        return f"The temperature is {temp}°C in {city}"
    
weather_report = WeatherReport()
print(weather_report(temp="30", city="Hyderabad"))