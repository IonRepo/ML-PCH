# Tests

This folder contains tests for the different routines implemented in the project, namely:

- Identification of composition and concentration from chemical formula.
- Recognition of a point being or not inside a triangle.

being each subroutine tested in the corresponding file.

In order to find all tests from the home directory of the project (parent directory of Tests) just run:

```bash
python3 -m unittest discover -v
```

and to run, for instance VCA composition_concentration funciton, execute:

```bash
python3 -m unittest tests.test_composition_concentration -v
```
