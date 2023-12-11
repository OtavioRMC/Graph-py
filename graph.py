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
  
  def add_vertex(self, vertex: V) -> int:
    """
      Adiciona um vértice ao gráfo e retorna o seu índice.
      self._edges.append([]) adiciona uma lista vazia para conter as arestas.
      returna: O índice do vértice adicionado.
    """
    self._vertices.append(vertex)
    self._edges.append([])
    return self.vertex_count - 1 
  
  def add_edge(self, edge: Edge) -> None:
    """
    Este é um grafo não direcionado portanto sempre
    adicionamos arestas nas duas direções.
    """
    self._edges[edge.start_vertex].append(edge)
    self._edges[edge.end_vertex].append(edge.reversed())

  def add_edge_by_indices(self, start_vertex:int, end_vertex:int) -> None:
    """
    Adiciona uma aresta usando índices dos vértices(método auxiliar)
    """
    edge: Edge = Edge(start_vertex,end_vertex)
    self.add_edge(edge)

  def add_edge_by_vertices(self, first: V, second: V) -> None:
    """
    Adiciona uma aresta consultando os índices dos vértices (método auxiliar)
    """
    start_vertex: int = self._vertices.index(first)
    end_vertex: int = self._vertices.index(second)
    self.add_edge_by_indices(first, second)

  def vertex_at(self, index:int) -> V:
    """
    Encontra o vértice em um índice específico.
    """
    return self._vertices[index]
  
  