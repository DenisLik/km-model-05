# ======== model_2.5 ==== 08/22/2022 ====

# Importing Necessary modules

import uvicorn
from fastapi import Request, FastAPI
from pydantic import BaseModel
import pickle as pkl
import numpy as np
import pandas as pd
import json

# Declaring our FastAPI instance for further application start
app_for_models = FastAPI()

# Creating class to define the request body
# and the type hints of each attribute
class request_body(BaseModel):
    amount_of_questions_passed : int
    overal_mean_result: float
    amount_of_exams_passed : int



# Creating an Endpoint to receive the data to make prediction on
@app_for_models.post('/predict')
def predict(data: request_body):
    
    # LEVEL 1. Gettig df from input request
    a = data
    b = data.json()
    c = json.loads(b)
    amount_of_questions_passed = c["amount_of_questions_passed"]
    overal_mean_result = c["overal_mean_result"]
    amount_of_exams_passed = c["amount_of_exams_passed"]

    # Loading predict models and last database
    predict_model_1 = pkl.load(open("saved_model.pkl","rb"))
    predict_model_2 = pkl.load(open("prob_model_2.pkl","rb"))
    
    
    input_values = {
        "base_1": amount_of_questions_passed,
        "result_1": overal_mean_result,
        "try_id_1": amount_of_exams_passed
    }
    
    
    # input data for model 1
    df_input_values = pd.DataFrame(input_values, index = range(1))
    
    # input data for model 2
    input_value = np.array(input_values["result_1"]).reshape(-1, 1)

    # STEP D. Predictions via Machine Learning
    prediction_1 = predict_model_1.predict(df_input_values)
    prediction_2 = predict_model_2.predict(input_value)
    
    output_1 = int(prediction_1[0])    
    pre_output_2 = round(float(prediction_2[0]), 2)
    
    def creating_output_2(x1, y1, x2, y2):

        if (x1 < 250 and y1 > 0.6) or (x2 < 10 and y1 > 0.6):
            output_2 = round(y2 * 0.8, 2)
        elif (250 <= x1 < 500  and y1 > 0.61) or (10 <= x2 < 20 and y1 > 0.61):
            output_2 = round(y2 * 0.85, 2)
        elif (500 <= x1 < 750  and y1 > 0.62) or (20 <= x2 < 30 and y1 > 0.62):
            output_2 = round(y2 * 0.9, 2)
        elif (750 <= x1 < 1000 and y1 > 0.63) or (30 <= x2 < 40 and y1 > 0.63):
            output_2 = round(y2 * 0.95, 2)
        else:
            output_2 = y2
            
        return output_2
    
    # STEP E. Creating answer for KnowLedgemap

    dict_output = {"amount_of_questions_lost": output_1,                     "probability": creating_output_2(amount_of_questions_passed, overal_mean_result, amount_of_exams_passed, pre_output_2)}
    
     
    return dict_output

#uvicorn.run(app_for_models)
