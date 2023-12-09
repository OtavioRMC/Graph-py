from typing import TypeVar, Generic , List , Optional
from edge import Edge

V = TypeVar("V") # Tipo dos vértice no grafo.

class Graph(Generic[V]):
  """
  O grafo será representado no formato de listas adjacentes.
  """
  def __init__(self, vertices: List[V] = []) -> None:
    """
    O Método init tem um parâmetro adicional vertices que é inicializado
    por padrão como uma lista vazia.
    Se eu tiver um grafo com 3 vértices (0,1,2) a lista de arestas seria inicializada assim
    vertices = [0,1,2]
    _edges agora é [[], [], []] onde cada sublista pode conter arestas para o vértice correspondente.
    Quando quiser adicionar uma aresta o grafo eu adicionaria um objeto Edge à sublista correspondente ao vértice de
    origem.
    Por exemplo para adicionar uma aresta do vértice 0 para o vértice 1: 
    _edges[0].append(Edge(0,1))
    edges agora é [[Edge(0,1)],[],[]]
    """
    self._vertices: List[V] = vertices
    self._edges: List[List[Edge]] = [[] for _ in vertices] 

  @property
  def vertex_count(self) -> int:
    """
    Retorna o número de vértices do grafo.
    """
    return len(self._vertices) 
  
  @property
  def edge_count(self) -> int:
    """
    Retorna o número de arestas do grafo.
    Aplica a função len para cada um dos vértices.
    """
    return sum(map(len,self._edges))