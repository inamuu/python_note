# conding: utf-8

from ruamel.yaml import YAML

inp = """\
- &CENTER {x: 1, y: 2}
- &LEFT {x: 0, y: 2}
- &BIG {r: 10}
- &SMALL {r: 1}

# All the following maps are equal:
# Explicit keys
- x: 1
  y: 2
  r: 10

# Merge one map
- <<: *CENTER
  r: 10

# Merge multiple maps
- <<: [*CENTER, *BIG]

# Override
- <<: [*BIG, *LEFT, *SMALL]
  x: 1
"""

yaml = YAML()
data = yaml.load(inp)
#assert data[7]['y'] == 2

for i in data:
    print(i)