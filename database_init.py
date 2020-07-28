from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

sys_db = client.db('_system', username='root', password='naman02')

if not sys_db.has_database('Einstein'):
    sys_db.create_database('Einstein')

db = client.db('Einstein', username='root', password='naman02')


# Create Graph
if db.has_graph('Website'):
    Website = db.graph('Website')
else:
    Website = db.create_graph('Website')


# Create vertices
if Website.has_vertex_collection('Languages'):
    Languages = Website.vertex_collection('Languages')
else:
    Languages = Website.create_vertex_collection('Languages')

if Website.has_vertex_collection('Links'):
    Links = Website.vertex_collection('Links')
else:
    Links = Website.create_vertex_collection('Links')

if Website.has_vertex_collection('Votes'):
    Votes = Website.vertex_collection('Votes')
else:
    Votes = Website.create_vertex_collection('Votes')

if Website.has_vertex_collection('question1'):
    question1 = Website.vertex_collection('question1')
else:
    question1 = Website.create_vertex_collection('question1')

if Website.has_vertex_collection('question2'):
    question2 = Website.vertex_collection('question2')
else:
    question2 = Website.create_vertex_collection('question2')

if Website.has_vertex_collection('question3'):
    question3 = Website.vertex_collection('question3')
else:
    question3 = Website.create_vertex_collection('question3')


# Define Relationships
if Website.has_edge_definition('has_links'):
    has_links = Website.vertex_collection('has_links')
else:
    has_links = Website.create_edge_definition(
        edge_collection='has_links',
        from_vertex_collections=['Languages'],
        to_vertex_collections=['Links']
    )

if Website.has_edge_definition('link_votes'):
    link_votes = Website.edge_collection('link_votes')
else:
    link_votes = Website.create_edge_definition(
        edge_collection='link_votes',
        from_vertex_collections=['Links'],
        to_vertex_collections=['Votes']
    )

if Website.has_edge_definition('question1_votes'):
    question1_votes = Website.edge_collection('question1_votes')
else:
    question1_votes = Website.create_edge_definition(
        edge_collection='question1_votes',
        from_vertex_collections=['question1'],
        to_vertex_collections=['Votes']
    )

if Website.has_edge_definition('question2_votes'):
    question2_votes = Website.edge_collection('question2_votes')
else:
    question2_votes = Website.create_edge_definition(
        edge_collection='question2_votes',
        from_vertex_collections=['question2'],
        to_vertex_collections=['Votes']
    )

if Website.has_edge_definition('question3_votes'):
    question3_votes = Website.edge_collection('question3_votes')
else:
    question3_votes = Website.create_edge_definition(
        edge_collection='question3_votes',
        from_vertex_collections=['question3'],
        to_vertex_collections=['Votes']
    )