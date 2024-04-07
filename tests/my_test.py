import pytest
from hypothesis import given

import minitorch

# from .strategies import med_ints, small_floats

# # Tests for module.py


# ## Website example

# This example builds a module
# as shown at https://minitorch.github.io/modules.html
# and checks that its properties work.


class ModuleA1(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.p1 = minitorch.Parameter(5)
        self.non_param = 10
        self.a = ModuleA2()
        self.b = ModuleA3()


class ModuleA2(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.p2 = minitorch.Parameter(10)


class ModuleA3(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.c = ModuleA4()


class ModuleA4(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.p3 = minitorch.Parameter(15)

#
mod = ModuleA1()

for mod_name, value in mod._modules.items():
    print(mod_name)

def named_params(modules):
    params = []
    
    for mod_name, value in modules.items(): 
        for name, param in modules[mod_name]._parameters.items():
            params.append((f'{mod_name}.{name}', param))

    return params 


def recur_params(): 
    pass