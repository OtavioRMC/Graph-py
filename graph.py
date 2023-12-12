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

  def add_edge_by_indices(self, start_vertex:int, end_vertex:int,weight:float) -> None:
    """
    Adiciona uma aresta usando índices dos vértices(método auxiliar)
    """
    edge: Edge = Edge(start_vertex, end_vertex, weight)
    self.add_edge(edge)

  def add_edge_by_vertices(self, first: V, second: V,weight:float) -> None:
    """
    Adiciona uma aresta consultando os índices dos vértices (método auxiliar)
    """
    start_vertex: int = self._vertices.index(first)
    end_vertex: int = self._vertices.index(second)
    self.add_edge_by_indices(start_vertex, end_vertex, weight)

  def vertex_at(self, index:int) -> V:
    """
    Encontra o vértice em um índice específico.
    """
    return self._vertices[index]
  
  def index_of(self, vertex: V) -> int:
    """
    Encontra o índice de um vértice de um grafo.
    """
    return self._vertices.index(vertex)
  
  def neighbors_for_index(self,index:int) -> List[V]:
      """
      Encontra os vértices aos quais um vértice com determinado índice está conectado.
      """
      return list(map(self.vertex_at, [e.end_vertex for e in self._edges[index]]))
  
  def neighbors_for_vertex(self, vertex: V) -> List[V]:
    """
    Consulta o índice de um vértice e econtra seus vizinhos (método auxiliar)
    """
    return self.neighbors_for_index(self.index_of(vertex))
  
  def edges_for_index(self,index:int) -> List[Edge]:
    """
    Retorna todas as arestas associadas a um vértice em um índice.
    """
    return self._edges[index]
  
  def edges_for_vertex(self, vertex: V) -> List[Edge]:
    """
    Consulta o índice de um vértice e retorna suas arestas(método auxiliar)
    """
    return self.edges_for_index(self.index_of(vertex))
  
  def __str__(self) -> str:
    """
    Facilita a exibição do grafo.
    """
    desc: str = ""
    for i in range (self.vertex_count):
      desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
    return desc
  
if __name__ == "__main__":
  
  # Create an instance of the Graph class
  graph = Graph[str]()

  # Add vertices to the graph
  graph.add_vertex("A")
  graph.add_vertex("B")
  graph.add_vertex("C")

  # Add edges to the graph
  graph.add_edge_by_vertices("A", "B", 1.0)  # Edge from "A" to "B" with weight 1.0
  graph.add_edge_by_vertices("B", "C", 2.0)  # Edge from "B" to "C" with weight 2.0
  graph.add_edge_by_vertices("C", "A", 3.0)  # Edge from "C" to "A" with weight 3.0

  # Print the graph
  print(graph)

  # Print the neighbors of a vertex
  print(graph.neighbors_for_vertex("A"))

  # Print the edges of a vertex
  print(graph.edges_for_vertex("A"))