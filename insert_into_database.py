from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

db = client.db('Einstein', username='root', password='naman02')

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

# Language 1
# --------------------------------------------------------------------------------------------
# insert values into vertices
Languages.insert({'_key': 'lang1', 'name': 'Python', 'votes': 0})
quality_of_content.insert({'_key': 'python-qoc', 'votes': 0})
course_depth_coverage.insert({'_key': 'python-cdc', 'votes': 0})
concepts_well_explained.insert({'_key': 'python-cwe', 'votes': 0})
text_links.insert({'_key': 'python-text_links', 'link': 'https://www.google.com'})
text_links.insert({'_key': 'python-video_links', 'link': 'https://www.google.com'})

# define relationships
l_qoc.insert({
    '_key': 'lang1-qoc',
    '_from': 'Languages/lang1',
    '_to': 'quality_of_content/python-qoc'
})

l_cdc.insert({
    '_key': 'lang1-cdc',
    '_from': 'Languages/lang1',
    '_to': 'course_depth_coverage/python-cdc'
})

l_cwe.insert({
    '_key': 'lang1-cwe',
    '_from': 'Languages/lang1',
    '_to': 'concepts_well_explained/python-cwe'
})

t_link.insert({
    '_key': 'lang1-text-link',
    '_from': 'Languages/lang1',
    '_to': 'text_links/python-text_links'
})

v_link.insert({
    '_key': 'lang1-video-link',
    '_from': 'Languages/lang1',
    '_to': 'text_links/python-video_links'
})
