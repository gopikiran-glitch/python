import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd


    return students.loc[students['student_id']==101,['name','age']]
    