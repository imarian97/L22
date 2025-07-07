from mate import medie

def test_normal():
    assert medie([9,8,7])==8.0
    # if not medie([9,8,7])==8.0:
    #     raise AssertionError("media numerelor 9,8,7 trebuia sa fie 8 si a fost alt numar")

def test_listaGoala():
    assert medie([])==0
    # if not medie([])==0:
    #     raise AssertionError()