from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


# uvicorn BMI:app --reload


app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
@app.get("/")
def HI():
    return {"message": "Hello, World!"}

@app.get("/bmi_calculator")
def bmi_calculator(weight: float=Query(...,gt=20,lt=200)
                   ,height: float=Query(...,gt=0.5,lt=3)):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return bmi,"Underweight"
    elif 18.5 <= bmi < 25:
        return bmi,"Normal weight"
    elif 25 <= bmi < 30:
        return bmi,"Overweight"
    else:
        return bmi,"Obese"
     