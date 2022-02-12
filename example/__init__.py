"""Module level docstring"""

import pydantic

def fn(arg: pydantic.fields.ModelField) -> None:
    """Function docstring

    Args:
        arg (pydantic.fields.ModelField): This is going to break!
    """
    # This bit doesn't matter
    print(arg)
