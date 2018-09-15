# rec

CLI for reconciling csv files.

By default, `rec` checks for the following, regardless of header or row order:

- Headers match
- Row lengths match
- All rows match


## usage

```
$ rec a.csv b.csv
```

### example

```
$ cat a.csv
a,b,c
1,2,3
4,5,6
$ cat b.csv
a,b,c
4,2,3
4,5,6
$ cat c.csv
b,a,c
5,4,6
2,1,3
$ rec a.csv b.csv
Different rows detected
(('1', '2', '3'), ('4', '2', '3'))
$ rec a.csv c.csv
$
```

## install

```
$ git clone git@github.com:ryantuck/rec.git
$ pip install -e ./rec
```
