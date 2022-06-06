# from fastapi import FastAPI
# import uvicorn
# import pandas as pd
# from pydantic import BaseModel
# from loan_prediction.inference import make_prediction
# app=FastAPI(title='Loan Prediction', version='1.0', description='fastapi for loan pred')
# class Data(BaseModel):
#     Loan_ID:str
#     Gender : str
#     Married : str
#     Dependents : str
#     Education : str
#     Self_Employed : str
#     ApplicantIncome : int
#     CoapplicantIncome : int
#     LoanAmount : float
#     Loan_Amount_Term: float
#     Credit_History : float
#     Property_Area : str
# @app.post('/fileType')
# def predict(myfiles):
#     myfiles = myfiles[3:]
#     df=pd.read_csv(myfiles)
#     a=make_prediction(df)
#     strings= ' '.join(str(i) for i in a)
#     return strings
# @app.post('/individualEntry')
# def predict_indiviual(data : Data):
#     data_dict = data.dict()
#     data_df = pd.DataFrame.from_dict([data_dict])
#     pred=make_prediction(data_df)
#     return {'predict':pred[0]}
#
#
# if __name__=='__main__':
#     uvicorn.run("FastAPI:app",host="0.0.0.0",port=8000, reload=True)
#
#
#
