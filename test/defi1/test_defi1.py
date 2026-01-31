#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import pytest
from xdvyturing.defi1.defi1 import multiples, compute, main

# -------------------
# Tests de la logique
# -------------------

def test_multiples_generator():
    # Vérifie que le générateur produit bien les bons multiples <20
    assert list(multiples(20)) == [0,5,7,10,14,15]

def test_compute_verbose_true():
    values, total = compute(20, verbose=True)
    assert total == 51
    assert values == [0,5,7,10,14,15]

def test_compute_verbose_false():
    values, total = compute(20, verbose=False)
    assert total == 51
    assert values is None

def test_compute_zero():
    # Cas extrême : max_value = 0
    values, total = compute(0, verbose=True)
    assert total == 0
    assert values == []

# -------------------
# Tests CLI
# -------------------

def test_main_no_verbose(capsys):
    main(["20"])
    captured = capsys.readouterr()
    # doit afficher juste la somme
    assert "51" in captured.out
    assert "[" not in captured.out

def test_main_verbose(capsys):
    main(["20", "-v"])
    captured = capsys.readouterr()
    # doit afficher la liste et la somme
    assert "51" in captured.out
    assert "[" in captured.out
    assert "0" in captured.out

# -------------------
# Tests erreurs argparse
# -------------------

def test_main_missing_argument():
    with pytest.raises(SystemExit):
        main([])  # maxValue obligatoire

def test_main_help():
    # --help déclenche SystemExit
    with pytest.raises(SystemExit):
        main(["--help"])

def test_main_invalid_argument():
    with pytest.raises(SystemExit):
        main(["not_an_int"])