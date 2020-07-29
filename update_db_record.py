from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

db = client.db('Einstein', username='root', password='naman02')

# Get the API wrapper for aql
aql = db.aql

# Graph
Website = db.graph('Website')

# Vertices
Languages = Website.vertex_collection('Languages')
text_links = Website.vertex_collection('text_links')
video_links = Website.vertex_collection('video_links')
concepts_well_explained = Website.vertex_collection('concepts_well_explained')
course_depth_coverage = Website.vertex_collection('course_depth_coverage')
quality_of_content = Website.vertex_collection('quality_of_content')

# Edges
l_qoc = Website.vertex_collection('l_qoc')
l_cdc = Website.vertex_collection('l_cdc')
l_cwe = Website.vertex_collection('l_cwe')
t_link = Website.vertex_collection('t_link')
v_link = Website.vertex_collection('v_link')


# All updates

def update_votes_cdc(votes: int, doc: str):
    query = 'UPDATE "python-cdc" WITH { votes: @value } IN ' + '{}'.format(doc)

    cursor = db.aql.execute(
        query,
        bind_vars={'value': votes}
    )


def update_votes_cwe(votes: int, doc: str):
    query = 'UPDATE "python-cwe" WITH { votes: @value } IN ' + '{}'.format(doc)

    cursor = db.aql.execute(
        query,
        bind_vars={'value': votes}
    )


def update_votes_qoc(votes: int, doc: str):
    query = 'UPDATE "python-qoc" WITH { votes: @value } IN ' + '{}'.format(doc)

    cursor = db.aql.execute(
        query,
        bind_vars={'value': votes}
    )
