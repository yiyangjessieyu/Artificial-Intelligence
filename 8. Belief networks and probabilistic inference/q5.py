network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2  # You can change this value
        }

    },
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2  # You can change this value
        }

    },
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2  # You can change this value
        }

    },
    'D': {
        'Parents': ['B'],
        'CPT': {
            (False,): 0.1,
            (True,): 0.1
        }

    },
    'E': {
        'Parents': ['B'],
        'CPT': {
            (False,): 0.1,
            (True,): 0.1
        }

    }
}

print(sorted(network.keys()))
