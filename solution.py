import pandas as pd
import numpy as np


chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a=x.mean()+(3.5*(3-np.exp(1)))
    return a # Ваш ответ
