#!/usr/bin/env python3
"""Regenerate VS code's settings.json based on the template and our overridden options."""
import json

import common
from overrides import overrides

# Load template
with open(common.template_path, 'r') as file:
    settings = json.load(file)

# Copy options from overrides. Options can be set to None to signify they shouldn't be
# included.
for key, val in overrides.items():
    if val is not None:
        settings[key] = val

# Write settings back out again
with open(common.get_settings_path(), "w") as file:
    json.dump(settings, file, sort_keys=True, indent=4)
