# km-model-05
On August 22, 2022 prediction application based two machine learned models was deployed into heroku server. File name of the application is km-model-05, and it was created by FastAPI library for Python.
The application is turned on POST requests and link is https://km-model-05.herokuapp.com/predict. This application can work with the data within only PMP exam preparation.
First model presents an ordinary Decision Tree Regressor model and predicts how many exam questions are remain for an user point where there is 99,9% of probability of success PMP exam pass for the user.
Second model presents an ordinary Nearest Neighbors Regressor model and predicts what probability of success PMP exam pass for the user with overall mean result for the user by cumulative total (current knowledge level).
========== REQUEST ==============
As input data for the application are json format data and they contains the following three parameters:
•	amount_of_questions_passed - how many questions are passed at current point in total;
•	overal_mean_result - overal mean result for the user by cumulative total;
•	amount_of_exams_passed - how many exam attempts are passed at current point in total.
NOTE #1:
To get “overal_mean_result” you need calculate sum of all mean exam results and divide it by total amount of exams. 
NOTE #2:
To need following conditions for to make correct request:
•	An user should be registered (“user_id” can’t be zero) and an exam should belong to the pmp exam list (case: an user passes own second and more pmp exam);
•	An user isn’t registered (“user_id” can be zero) and an exam should be #24 (case: an user passes own first pmp exam).

input example:
{
    "amount_of_questions_passed": 55,
    "overal_mean_result": 0.5273,
    "amount_of_exams_passed": 1
}

========== ANSWER ==============
As an answer from the application is json format data and it contains the following two parameters:
•	amount_of_questions_lost - how many exam questions are remain for an user point where there is 99,9% of probability of success PMP exam pass for the user;
•	probability - probability of success PMP exam pass for the user with overall mean result (current knowledge level).
answer example:
{
    "amount_of_questions_lost": 2115,
    "probability": 47.76
}

