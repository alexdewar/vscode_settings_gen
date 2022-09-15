#!/usr/bin/env python3
"""Generate the settings_template.json from current settings.json file.

Any options specified in overrides.py will be ignored.
"""
import json

import common
from overrides import overrides

# Load existing settings
with open(common.get_settings_path(), 'r') as file:
    settings = json.load(file)

# Delete any keys that we have overridden
for key in list(settings.keys()):
    if key in overrides:
        del settings[key]

# Save remaining settings as a template
with open(common.template_path, 'w') as file:
    json.dump(settings, file, sort_keys=True, indent=4)
