"""
In this example, we will use dictionaries to demonstrate the basic usage of KeepDelta.
"""

import keepdelta as kd

# Profile of a person
profile = {
    "info": {
        "name": "Alice",
        "age": 30,
        "is_student": True,
        "grades": [85.5, 90.0, 78],
        "preferences": (
            "chocolate",
            {"sports": {"football", "tennis"}},
        ),
    },
    "meta": {
        "attributes": [{"id": 1, "value": "active"}, {"id": 2, "value": "inactive"}],
        "settings": {"dark_mode": True, "font_size": 14, "scale": 1.25},
    },
}

# Profile of that person one year later
profile_new = {
    "info": {
        "name": "Alice",
        "age": 31,
        "is_student": False,
        "grades": [85.5, 90.0, 78],
        "preferences": (
            "coffee",
            {"sports": {"football", "bodybuilding"}},
        ),
    },
    "meta": {
        "attributes": [{"id": 1, "value": "inactive"}, {"id": 2, "value": "inactive"}],
        "settings": {"dark_mode": True, "font_size": 14, "scale": 1.25},
    },
}

# Create delta
delta = kd.create(profile, profile_new)
print("Delta:", delta)

# Apply delta
profile_reconstructed = kd.apply(profile, delta)
print("Reconstruction is successful:", profile_reconstructed == profile_new)
