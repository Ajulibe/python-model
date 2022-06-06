from pydantic import BaseModel


class LoanSchema(BaseModel):
    Loan_ID: str
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

    class Config:
        env_file = "../.env"
        orm_mode = True


class RetrieveSchema(BaseModel):
    Loan_ID: str

    class Config:
        env_file = "../.env"
        orm_mode = True
