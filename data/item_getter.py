import random

# a simulated database store
data = {
    1: [
        {"content": "बाख्रा", "category": "जनाबर"},
        {"content": "कालीज", "category": "पन्छि"},
        {"content": "लौका", "category": "तरकारी"},
        {"content": "सुन्तला", "category": "फलफुल"},
        {"content": "मकै", "category": "अन्नबाली"},
        {"content": "फापर", "category": "अन्नबाली"},
        {"content": "स्याउ", "category": "फलफुल"},
        {"content": "घोडा", "category": "जनाबर"},
        {"content": "गाई", "category": "जनाबर"},
        {"content": "कुकुर", "category": "जनाबर"},
        {"content": "बिरालो", "category": "जनाबर"},
        {"content": "जौ", "category": "अन्नबाली"},
        {"content": "चामल", "category": "अन्नबाली"},
        {"content": "बदाम", "category": "अन्नबाली"},
        {"content": "सिमी", "category": "तरकारी"},
        {"content": "भेडा", "category": "जनाबर"},
        {"content": "मुजुर", "category": "पन्छि"},
        {"content": "काफल", "category": "फलफुल"},
    ],
    2: [
        {"content": "गाई", "category": "जनाबर"},
        {"content": "मुजुर", "category": "पन्छि"},
        {"content": "टमाटर", "category": "तरकारी"},
        {"content": "केरा", "category": "फलफुल"},
        {"content": "गहुँ", "category": "अन्नबाली"},
        {"content": "कुकुर", "category": "जनाबर"},
        {"content": "काग", "category": "पन्छि"},
        {"content": "बन्दा", "category": "तरकारी"},
        {"content": "अंगुर", "category": "फलफुल"},
        {"content": "जौ", "category": "अन्नबाली"},
    ],
    3: [
        {"content": "भेडा", "category": "जनाबर"},
        {"content": "डाँफे", "category": "पन्छि"},
        {"content": "ककडी", "category": "तरकारी"},
        {"content": "काफल", "category": "फलफुल"},
        {"content": "चामल", "category": "अन्नबाली"},
    ],
    4: [
        {"content": "बाख्रा", "category": "जनाबर"},
        {"content": "गाई", "category": "जनाबर"},
        {"content": "घोडा", "category": "जनाबर"},
        {"content": "कुकुर", "category": "जनाबर"},
        {"content": "कालीज", "category": "पन्छि"},
        {"content": "मुजुर", "category": "पन्छि"},
        {"content": "काग", "category": "पन्छि"},
        {"content": "लौका", "category": "तरकारी"},
        {"content": "टमाटर", "category": "तरकारी"},
        {"content": "ककडी", "category": "तरकारी"},
        {"content": "बन्दा", "category": "तरकारी"},
        {"content": "सुन्तला", "category": "फलफुल"},
        {"content": "स्याउ", "category": "फलफुल"},
        {"content": "केरा", "category": "फलफुल"},
        {"content": "अंगुर", "category": "फलफुल"},
        {"content": "मकै", "category": "अन्नबाली"},
        {"content": "फापर", "category": "अन्नबाली"},
        {"content": "गहुँ", "category": "अन्नबाली"},
        {"content": "जौ", "category": "अन्नबाली"},
    ],
}


def get_single_item_set():
    """chooses one record from ths list and returns it.
    objective is to return a new set of data everytime when the user requests data.
    shuffles the data to create a random set on every request.

    Returns:
        _type_: [dict]
    """
    return_data = data[random.choice(list(data.keys()))]

    random.shuffle(return_data)

    return return_data
