from abc import ABC, abstractmethod
from math import cos, sin, exp, radians, sinh, pi
import numpy as np


def calculate_trend_and_plunge(vector):
    # 将向量归一化为单位向量
    unit_vector = vector / np.linalg.norm(vector)
    # 计算倾伏角（plunge）
    plunge = np.arcsin(unit_vector[2])  # 使用反正弦函数计算倾伏角，结果以弧度表示
    # 计算倾伏向（trend),使用反正切函数计算倾伏向，结果以弧度表示
    trend = pi + np.arctan2(unit_vector[1], unit_vector[0])
    return trend, plunge


class TriclinicBase(ABC):
    """
    描述三斜剪切带的变形抽象基类
    Transpression和Transtension是该抽象基类的具体实现
    """

    def __init__(self, gamma_dot, epsilon_dot, phi):
        self.gamma_dot = gamma_dot
        self.epsilon_dot = epsilon_dot
        self.phi = phi

    @abstractmethod
    def F_matrix(self, t):
        """
        变形梯度张量，由子类实现
        """
        return

    def lineation(self, time_points):
        """
        在一系列时间点time_points上求线理的倾伏向和倾伏角
        """
        trends = []
        plunges = []

        for t in time_points:
            F = self.F_matrix(t)
            FFt = F.dot(F.T)
            _, eig_vectors = np.linalg.eigh(FFt)
            trd, plg = calculate_trend_and_plunge(eig_vectors[:, 2])
            trends.append(trd)
            plunges.append(plg)
        return trends, plunges

    def foliation_normal(self, time_points):
        """
        在一系列时间点time_points上求面理法线的倾伏向和倾伏角
        """
        trends = []
        plunges = []

        for t in time_points:
            F = self.F_matrix(t)
            FFt = F.dot(F.T)
            _, eig_vectors = np.linalg.eigh(FFt)
            trd, plg = calculate_trend_and_plunge(eig_vectors[:, 0])
            trends.append(trd)
            plunges.append(plg)
        return trends, plunges


class Transpression(TriclinicBase):
    def __init__(self, gamma_dot, eps_dot, phi):
        super().__init__(gamma_dot, eps_dot, phi)

    def F_matrix(self, t):
        et = self.epsilon_dot * t
        ge = self.gamma_dot / self.epsilon_dot
        phi = radians(self.phi)

        return np.array(
            [
                [1, ge * cos(phi) * (1 - exp(-et)), 0],
                [0, exp(-et), 0],
                [0, ge * sin(phi) * sinh(et), exp(et)],
            ]
        )

class Transtension(TriclinicBase):
    def __init__(self, gamma_dot, eps_dot, phi):
        super().__init__(gamma_dot, eps_dot, phi)

    def F_matrix(self, t):
        et = self.epsilon_dot * t
        ge = self.gamma_dot / self.epsilon_dot
        phi = radians(self.phi)

        return np.array(
            [
                [1, ge * cos(phi) * (exp(et) - 1), 0],
                [0, exp(et), 0],
                [0, ge * sin(phi) * sinh(et), exp(-et)],
            ]
        )
