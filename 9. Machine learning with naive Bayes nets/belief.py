from numbers import Number

network = {
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): ((1+2)/(4+2*2)),
            (False,): ((3+2)/(3+2*2)),
        }
    },

    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): ((1+2)/(4+2*2)),
            (False,): ((2+2)/(3+2*2)),
        }
    },

    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): ((0+2)/(4+2*2)),
            (False,): ((0+2)/(3+2*2)),
        }
    },

    'Y': {
        'Parents': [],
        'CPT': {
            (): ((4+2)/(7+2*2)),
        }
    },
}

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")
