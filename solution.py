import pandas as pd
import numpy as np


chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x_mean = (3-np.exp(1))/20 # ср. ускорение
    x=x/10
    difference = x-x_mean
    squared_difference = np.square(difference)
    return squared_difference.mean() # Ваш ответ
