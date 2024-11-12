'''Util will consists all the common things that we are going to probabl try to import or use'''

import os
import sys
import dill #library which helps us to create pickle file
import numpy as np
import pandas as pd

from src.exception import CustomException

def sve_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)