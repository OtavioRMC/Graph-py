from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
  """
  Uma Edge é definida como uma nova conexão entre dois vértices , cada qual
  representado por um índice inteiro. Por convenção "u" é usado para referenciar
  o primeiro vértice e "v" utilizado para representar o segundo
  """
  start_vertex: int # o vértice "de"
  end_vertex: int # o vértice "para"

  def __post_init__(self):
    if not isinstance(self.u, int) or not isinstance(self.v, int):
      raise TypeError("Os Vértices devem ser inteiros.")
    if self.u < 0 or self.v < 0:
      raise ValueError("Os Vértices devem ser números inteiros positivos.")

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
