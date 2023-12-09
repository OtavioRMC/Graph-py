from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
  u: int # o vértice "de"
  v: int # o vértice "para"

  def reversed(self) -> Edge:
    """
    A função reversed é um método de instância, o que significa
    que ele opera em uma instância específica da classe Edge. 
    Ela pega a instância atual (referida por self) e retorna uma nova
    instância da Edge onde os vértices u e v são trocados.
    """
    return Edge(self.v, self.u)
  
  def __str__(self) -> str:
    """
    O método __str__ em Python é um método especial que é usado para fornecer uma representação de string
    de um objeto.
    """
    return f"{self.u} -> {self.v}"
