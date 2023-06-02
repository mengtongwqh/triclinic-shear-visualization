import numpy as np
import math

def Fts(pa,Φ,t):
    ε = 1
    Fts_matrix = np.array([[1,  (pa)*math.cos(Φ) *(1-math.exp(-ε*t)), 0],
                            [0, math.exp(-ε*t), 0],
                            [0, (pa)*math.sin(Φ) *math.sinh(ε*t), math.exp(ε*t)]])  
    return Fts_matrix  

def Fps(pa,Φ,t):
    ε = 1
    Fps_matrix = np.array([[1,  (pa)*math.cos(Φ)*(math.exp(-ε*t)-1), 0],
                           [0, math.exp(-ε*t), 0],
                           [0, (pa)*math.sin(Φ)*math.sinh(ε*t), math.exp(-ε*t)]])  
    return Fps_matrix 

def ffT_eigh(F_matrix):
    F_matrix_tr = np.transpose(F_matrix)
    FFt = np.dot(F_matrix, F_matrix_tr)
    eighvalue,eighvector = np.linalg.eigh(FFt)
    max_direction = eighvector[-1]
    return  max_direction

def calculate_plunge_and_trend(vector):
    # 将向量归一化为单位向量
    unit_vector = vector / np.linalg.norm(vector)
   
    # 计算倾伏角（plunge）
    plunge = np.arcsin(unit_vector[2])  # 使用反正弦函数计算倾伏角，结果以弧度表示

    # 计算倾伏向（trend）
    trend = np.arctan2(unit_vector[1], unit_vector[0])  # 使用反正切函数计算倾伏向，结果以弧度表示
    # trend += math.pi
    # 将弧度转换为度数
    plunge_deg = np.degrees(plunge)
    trend_deg = np.degrees(trend)
    
    # 返回倾伏角和倾伏向的度数表示
    return plunge_deg, trend_deg



