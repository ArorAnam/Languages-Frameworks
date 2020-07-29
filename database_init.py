from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

# get the system database API wrapper
sys_db = client.db('_system', username='root', password='naman02')

# Create data base
if not sys_db.has_database('Einstein'):
    sys_db.create_database('Einstein')

db = client.db('Einstein', username='root', password='naman02')

# Create Graph
if db.has_graph('Website'):
    Website = db.graph('Website')
else:
    Website = db.create_graph('Website')

# Create vertices

# Language vertex to have all languages
if Website.has_vertex_collection('Languages'):
    Languages = Website.vertex_collection('Languages')
else:
    Languages = Website.create_vertex_collection('Languages')
Languages.truncate()

# Links vertices for all links
if Website.has_vertex_collection('text_links'):
    text_links = Website.vertex_collection('text_links')
else:
    text_links = Website.create_vertex_collection('text_links')
text_links.truncate()

# Links vertices for all links
if Website.has_vertex_collection('video_links'):
    video_links = Website.vertex_collection('video_links')
else:
    video_links = Website.create_vertex_collection('video_links')
video_links.truncate()

# Create Questions vertices
# Question 1
if Website.has_vertex_collection('concepts_well_explained'):
    concepts_well_explained = Website.vertex_collection('concepts_well_explained')
else:
    concepts_well_explained = Website.create_vertex_collection('concepts_well_explained')
concepts_well_explained.truncate()

# Question 2
if Website.has_vertex_collection('course_depth_coverage'):
    course_depth_coverage = Website.vertex_collection('course_depth_coverage')
else:
    course_depth_coverage = Website.create_vertex_collection('course_depth_coverage')
course_depth_coverage.truncate()
course_depth_coverage.truncate()

# Question 3
if Website.has_vertex_collection('quality_of_content'):
    quality_of_content = Website.vertex_collection('quality_of_content')
else:
    quality_of_content = Website.create_vertex_collection('quality_of_content')
quality_of_content.truncate()

# Define Relationships
# Relations go from every language to every other thing
if Website.has_edge_definition('l_qoc'):
    l_qoc = Website.vertex_collection('l_qoc')
else:
    l_qoc = Website.create_edge_definition(
        edge_collection='l_qoc',
        from_vertex_collections=['Languages'],
        to_vertex_collections=['quality_of_content']
    )
l_qoc.truncate()

if Website.has_edge_definition('l_cdc'):
    l_cdc = Website.vertex_collection('l_cdc')
else:
    l_cdc = Website.create_edge_definition(
        edge_collection='l_cdc',
        from_vertex_collections=['Languages'],
        to_vertex_collections=['course_depth_coverage']
    )
l_cdc.truncate()

if Website.has_edge_definition('l_cwe'):
    l_cwe = Website.vertex_collection('l_cwe')
else:
    l_cwe = Website.create_edge_definition(
        edge_collection='l_cwe',
        from_vertex_collections=['Languages'],
        to_vertex_collections=['concepts_well_explained']
    )
l_cwe.truncate()

if Website.has_edge_definition('t_link'):
    t_link = Website.vertex_collection('t_link')
else:
    t_link = Website.create_edge_definition(
        edge_collection='t_link',
        from_vertex_collections=['Languages'],
        to_vertex_collections=['text_links']
    )
t_link.truncate()

if Website.has_edge_definition('v_link'):
    v_link = Website.vertex_collection('v_link')
else:
    v_link = Website.create_edge_definition(
        edge_collection='v_link',
        from_vertex_collections=['Languages'],
        to_vertex_collections=['video_links']
    )
v_link.truncate()


