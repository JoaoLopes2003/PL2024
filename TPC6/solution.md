## Produções

```
P -> A P 
   | ε
```
```
A -> ? var
    | var = B
    | ! B
```
```
B -> B + B
    | B - B
    | B * B
    | B / B
    | ( B )
    | num
    | var
```

## Lookahead Sets

- LA(P -> A P): `?`, `var`, `!`
- LA(P -> ε): `EOF`
- LA(A -> ? var): `?`
- LA(A -> var = B): `var`
- LA(A -> ! B): `!`
- LA(B -> B + B): `num`, `var`
- LA(B -> B - B): `num`, `var`
- LA(B -> B * B): `num`, `var`
- LA(B -> B / B): `num`, `var`
- LA(B -> ( B )): `(`
- LA(B -> num): `num`
- LA(B -> var): `var`
