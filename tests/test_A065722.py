from oeis import A065722


def test_A065722():
    from_oeis_org = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        37,
        43,
        47,
        53,
        61,
        71,
        73,
        79,
        83,
        97,
        103,
        107,
        109,
        113,
        131,
        149,
        151,
        157,
        163,
        167,
        181,
        191,
        193,
        197,
        227,
        233,
        241,
        251,
        277,
        293,
        307,
        311,
        313,
        317,
        349,
        359,
        373,
        389,
        401,
        419,
        421,
        433,
        443,
        449,
        463,
        467,
        503,
    ]

    assert A065722[: len(from_oeis_org)] == from_oeis_org
