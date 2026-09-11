""" 
Data class fields can have default values.

Syntax
  @dataclass
  class ClassName:
    field1: type
    field2: type = default_value

1. Fields can have default values.
2. Fields without default values must come before fields with default values.
3. This rule is similar to function parameters.
"""