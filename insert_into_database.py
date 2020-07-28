from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

db = client.db('Einstein', username='root', password='naman02')

# Graph
Website = db.graph('Website')

# Vertices
Languages = Website.vertex_collection('Languages')
Links = Website.vertex_collection('Links')
Votes = Website.vertex_collection('Votes')

# Edges
has_links = Website.vertex_collection('has_links')
link_votes = Website.edge_collection('link_votes')


# Language 1
# -----------------------------------------------------------------
Languages.insert({'_key': 'python'})
Links.insert({'_key': 'fastapi'})
Votes.insert({'_key': 'fastapi-votes', 'votes': 0})

has_links.insert({
    '_key': 'python-fastapi',
    '_from': 'Languages/python',
    '_to': 'Links/fastapi'
})

link_votes.insert({
    '_key': 'fastapi-votes',
    '_from': 'Links/fastapi',
    '_to': 'Votes/fastapi-votes'
})
