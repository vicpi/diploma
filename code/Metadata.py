# Configuration of project in "metadata".
# Requires: File "metadata.v" existence.

import yaml

stream = file('metadata.yml', 'r')
metadata = yaml.load(stream)
stream.close()

Rules = yaml.load( file("Rules.yml", 'r') )
Types = yaml.load( file("ResultTypes.yml", 'r') )