

# BMI Calculator

This project is a simple BMI (Body Mass Index) calculator built using FastAPI as the backend and a minimal HTML interface for user input. It allows users to calculate their BMI by entering their weight and height, and returns a result indicating whether the user is underweight, of normal weight, overweight, or obese.

## Features
- **BMI Calculation**: Calculates BMI based on the formula `BMI = weight / (height^2)` using inputs for weight (in kilograms) and height (in meters).
- **User Interface**: A simple, user-friendly HTML interface for entering weight and height.
- **API**: A FastAPI-based backend that processes the input and returns the BMI value along with its corresponding category.

## Technologies Used
- **FastAPI**: Python framework for building APIs.
- **HTML/CSS**: For the front-end interface.
- **JavaScript**: To send requests from the front-end to the FastAPI server and display the result.

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/bmi-calculator.git
   cd bmi-calculator
   ```

2. **Install the dependencies:**

   You can install the necessary Python packages using `pip`:

   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the FastAPI server:**

   Run the following command to start the FastAPI server locally:

   ```bash
   uvicorn BMI:app --reload
   ```

   The server will be available at: `http://127.0.0.1:8000`

## Usage

1. **Access the API**:
   
   Open your browser and visit `http://127.0.0.1:8000/`. You should see a basic "Hello, World!" message confirming that the server is running.

2. **BMI Calculation via the API**:

   To calculate BMI, you can use the following API endpoint:

   - **Endpoint**: `/bmi_calculator`
   - **Method**: GET
   - **Query Parameters**:
     - `weight` (float): The weight in kilograms (must be between 20 and 200).
     - `height` (float): The height in meters (must be between 0.5 and 3).
   
   Example API call:
   ```
   http://127.0.0.1:8000/bmi_calculator?weight=70&height=1.75
   ```

3. **Using the HTML interface**:
   
   Open the provided `index.html` file in your browser. Enter your weight and height into the form, and it will use the FastAPI backend to fetch and display your BMI and category.

## Example

### Request:
```
http://127.0.0.1:8000/bmi_calculator?weight=68&height=1.75
```

### Response:
```
{
  "BMI": 22.2,
  "Category": "Normal weight"
}
```

