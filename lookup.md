# Using ast_ftns script

Users can also look for specific minor objects in the API using the [ast_ftns.py](https://github.com/ricco-hub/API/blob/main/ast_ftns.py) script. Additionally, we provide functions to search across specific frequencies and arrays. Here, we describe what each function does and example usage. Please note that users must download [asteroid_list.txt](https://github.com/ricco-hub/API/blob/main/asteroid_list.txt) in order to use the `ast_ftns.py` script.

## ast_names

Print available minor objects in the API. This call takes no parameters and prints to the console.

```python
ast_names()

Aaltje
Abastumani
Abnoba
Abundantia
Academia
Achilles
Ada
Adelgunde
Adelheid
Adelinda
...
Zahringia
Zambesia
Zeelandia
Zeissia
Zelia
Zelima
Zelinda
Zenobia
Zerbinetta
Zeuxo
Zwetana
```

## find_ast

Find a user provided minor object in the API for each frequency and array combination. This function only works for known minor objects in the database, so users may have to call `ast_names()` to determine which objects are supported before narrowing down a search. The function takes a capitalized string. The function call prints to the console.

```python
find_ast('Ceres')

Ceres_lc_night_pa4_150.pk
Ceres_lc_night_pa4_220.pk
Ceres_lc_night_pa5_090.pk
Ceres_lc_night_pa5_150.pk
```

## find_arr

Find a user provided ACT array in the API for each frequency and minor object combination. Users can select from the following arrays: `pa4, pa5, pa6`. The function call prints to the console.

```python
find_arr('pa4')

Aaltje_lc_night_pa4_150.pk
Aaltje_lc_night_pa4_220.pk
Abastumani_lc_night_pa4_150.pk
Abastumani_lc_night_pa4_220.pk
Abnoba_lc_night_pa4_150.pk
Abnoba_lc_night_pa4_220.pk
Abundantia_lc_night_pa4_150.pk
Abundantia_lc_night_pa4_220.pk
Academia_lc_night_pa4_150.pk
Achilles_lc_night_pa4_150.pk
...
Zelima_lc_night_pa4_220.pk
Zelinda_lc_night_pa4_150.pk
Zelinda_lc_night_pa4_220.pk
Zenobia_lc_night_pa4_150.pk
Zenobia_lc_night_pa4_220.pk
Zerbinetta_lc_night_pa4_150.pk
Zerbinetta_lc_night_pa4_220.pk
Zeuxo_lc_night_pa4_150.pk
Zeuxo_lc_night_pa4_220.pk
Zwetana_lc_night_pa4_150.pk
Zwetana_lc_night_pa4_220.pk
```

## find_freq

Find a user provided ACT frequency in the API for each array and minor object combination. Users can select from the following frequencies: `090, 150, 220`. The function call prints to the console.

```python
find_freq('150')

Aaltje_lc_night_pa4_150.pk
Aaltje_lc_night_pa5_150.pk
Aaltje_lc_night_pa6_150.pk
Abastumani_lc_night_pa4_150.pk
Abastumani_lc_night_pa5_150.pk
Abastumani_lc_night_pa6_150.pk
Abnoba_lc_night_pa4_150.pk
Abnoba_lc_night_pa5_150.pk
Abnoba_lc_night_pa6_150.pk
Abundantia_lc_night_pa4_150.pk
...
Zelinda_lc_night_pa6_150.pk
Zenobia_lc_night_pa4_150.pk
Zerbinetta_lc_night_pa4_150.pk
Zerbinetta_lc_night_pa5_150.pk
Zerbinetta_lc_night_pa6_150.pk
Zeuxo_lc_night_pa4_150.pk
Zeuxo_lc_night_pa5_150.pk
Zeuxo_lc_night_pa6_150.pk
Zwetana_lc_night_pa4_150.pk
Zwetana_lc_night_pa5_150.pk
Zwetana_lc_night_pa6_150.pk
```
