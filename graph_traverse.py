from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

db = client.db('Einstein', username='root', password='naman02')

# Graph
Website = db.graph('Website')


def gtraverse():
    trv = Website.traverse(
        start_vertex='Languages/python',
        direction='outbound',
        strategy='bfs',
        edge_uniqueness='global',
        vertex_uniqueness='global',
        # min_depth=2,
        # max_depth=2
    )

    vertices = trv['vertices']

    return vertices
