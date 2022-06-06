# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Float
# from pydantic import BaseModel
#
# Base = declarative_base()
#
#
# class LoanApplication(Base):
#     __tablename__ = "loan_eligibility"
#     Loan_ID = Column(String, primary_key=True)
#     Gender = Column(String)
#     Married = Column(String)
#     Dependents = Column(String)
#     Education = Column(String)
#     Self_Employed = Column(String)
#     ApplicantIncome = Column(Integer, default=0)
#     CoapplicantIncome = Column(Integer)
#     LoanAmount = Column(Float, default=0)
#     Loan_Amount_Term = Column(Float, default=0)
#     Credit_History = Column(Float, default=0)
#     Property_Area = Column(String)
#     loan_eligibile = Column(String)
#
# class loanSchema(BaseModel):
#     Loan_ID: str
#     Gender: str
#     Married: str
#     Dependents: str
#     Education: str
#     Self_Employed: str
#     ApplicantIncome: int
#     CoapplicantIncome: int
#     LoanAmount: float
#     Loan_Amount_Term: float
#     Credit_History: float
#     Property_Area: str
#     loan_eligibile: str