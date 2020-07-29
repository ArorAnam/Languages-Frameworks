from arango import ArangoClient

# Initialize the Arango Client
client = ArangoClient(hosts='http://localhost:8529')

db = client.db('Einstein', username='root', password='naman02')

# Graph
Website = db.graph('Website')


def gtraverse(lang: str):
    language = 'Languages/{}'.format(lang)
    trv = Website.traverse(
        start_vertex=language,
        direction='outbound',
        strategy='bfs',
        edge_uniqueness='global',
        vertex_uniqueness='global',
        # min_depth=2,
        # max_depth=2
    )

    vertices = trv['vertices']

    vert_dict = {}
    for i in range(len(vertices)):
        if 'Languages' in vertices[i]['_id']:
            vert_dict['name'] = vertices[i]['name']
            continue
        if 'course_depth_coverage' in vertices[i]['_id']:
            vert_dict['votes1'] = vertices[i]['votes']
            continue
        if 'concepts_well_explained' in vertices[i]['_id']:
            vert_dict['votes2'] = vertices[i]['votes']
            continue
        if 'quality_of_content' in vertices[i]['_id']:
            vert_dict['votes3'] = vertices[i]['votes']
            continue
        if 'text_links' in vertices[i]['_id']:
            vert_dict['text_links'] = vertices[i]['link']
            continue
        if 'video_links' in vertices[i]['_id']:
            vert_dict['video_links'] = vertices[i]['link']
            continue

    return vert_dict
