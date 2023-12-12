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
  weight: float # peso da aresta
  
  def __post_init__(self):
    if not isinstance(self.start_vertex, int) or not isinstance(self.end_vertex, int):
      raise TypeError("Os Vértices devem ser inteiros.")
    if self.start_vertex < 0 or self.end_vertex < 0:
      raise ValueError("Os Vértices devem ser números inteiros positivos.")
    if not isinstance(self.weight, (int,float)):
      raise TypeError("Os pesos devem ser um número.")

  def reversed(self) -> Edge:
    """
    A função reversed é um método de instância, o que significa
    que ele opera em uma instância específica da classe Edge. 
    Ela pega a instância atual (referida por self) e retorna uma nova
    instância da Edge onde os vértices u e v são trocados.
    """
    return Edge(self.end_vertex, self.start_vertex,self.weight)
  
  def __str__(self) -> str:
    """
    O método __str__ em Python é um método especial que é usado para fornecer uma representação de string
    de um objeto.
    """
    return f"{self.start_vertex} --[{self.weight}]--> {self.end_vertex}"

  def copy(self) -> Edge:
    """
    Returns a copy of the current edge.
    """
    return Edge(self.start_vertex,self.end_vertex,self.weight)