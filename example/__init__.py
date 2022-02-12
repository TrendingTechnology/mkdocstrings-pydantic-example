"""Module level docstring"""

import pydantic

def fn(arg: pydantic.BaseModel) -> None:
    """Function docstring

    Args:
        arg (pydantic.BaseModel): This is going to break!
    """
    # This bit doesn't matter
    print(arg)
