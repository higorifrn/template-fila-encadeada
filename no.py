# -*- coding:UTF-8 -*-

class No:
  def __init__(self, dado=None, prox=None):
      self.__dado = dado
      self.__prox = prox

  def __str__(self) -> str:
     return f"Dado: {self.__dado}"
  
  @property
  def dado(self):
     return self.__dado
  
  @dado.setter
  def dado(self, valor):
     self.__dado = valor

  @property
  def prox(self):
     return self.__prox
  
  @prox.setter
  def prox(self, valor):
     self.__prox = valor