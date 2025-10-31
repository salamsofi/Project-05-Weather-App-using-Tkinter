# 🌦️ My Weather App

A simple and elegant desktop weather application built with Python and Tkinter. It fetches real-time weather data using the OpenWeatherMap API and displays temperature, humidity, pressure, and more — all wrapped in a clean GUI.

---

## 🚀 Features

- 🌍 Select a city from a dropdown menu
- 📡 Fetch live weather data via OpenWeatherMap API
- 🌡️ Display temperature, humidity, pressure, and weather conditions
- 🕒 Show current date and time (auto-updates every minute)
- ⌨️ Keyboard support: Press Enter to trigger weather fetch
- 🎨 Custom background image and styled UI

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/salamsofi/my-weather-app.git
   cd my-weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install requests
   ```

3. **Add your background image**
   - Place your image in the `used_images` folder
   - Update the `image_path` in the code:
     ```python
     image_path = r"D:\Python Projects\pr-05\used_images\weather_image.png"
     ```

4. **Run the app**
   ```bash
   python weather_app.py
   ```

---

## 🔑 API Key

This app uses the [OpenWeatherMap API](https://openweathermap.org/api).  
Make sure to replace the placeholder API key in the code with your own:

```python
api_key = "your_api_key_here"
```

You can get a free API key by signing up at [openweathermap.org](https://openweathermap.org/).

---

## 📸 Screenshot

### 🌤️ Weather Result Display
![Weather Result](project_ui/main_screen.png)

### 🌤️ Weather Result Display
![Weather Result](project_ui/weather_result.png)

---

## ✨ Future Enhancements

- Add weather icons dynamically
- Support for typing city names manually
- Save recent searches
- Add auto-complete or search history

---

## 🙌 Credits

Developed by [Md](https://github.com/salamsofi)  
Powered by Python, Tkinter, and OpenWeatherMap

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and share!
```