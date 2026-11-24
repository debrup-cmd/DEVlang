# DebLang Mini Tutorial

This short tutorial introduces the basic language features. Save each example in a `.deb` file and run it with DebLang.

## 1. Display text

```python
bolo("Hello, world!")
```

`bolo()` displays output, like Python's `print()`.

## 2. Get input

```python
naam = pucho("Enter your name: ")
bolo("Hello", naam)
```

`pucho()` asks the user for input, like Python's `input()`.

## 3. Make decisions

```python
marks = 80

agar marks >= 90:
    bolo("Excellent")
warna_agar marks >= 60:
    bolo("Good")
warna:
    bolo("Keep practising")
```

The conditions are checked from top to bottom. The first true branch runs.

## 4. Repeat with a for loop

```python
har number mein range(1, 6):
    bolo(number)
```

This prints numbers 1 through 5. `har` means `for`; `mein` means `in`.

## 5. Repeat with a while loop

```python
count = 3

jabtak count > 0:
    bolo(count)
    count = count - 1
```

The loop repeats while its condition is true.

## 6. Create a function

```python
karya greet(name):
    wapas "Hello " + name

bolo(greet("Debrup"))
```

`karya` defines a function and `wapas` returns a result.

## 7. Use Boolean values and logic

```python
is_ready = sach

agar is_ready aur nahi jhooth:
    bolo("Ready!")
```

`sach` means `True`, `jhooth` means `False`, `aur` means `and`, and `nahi` means `not`.

## 8. Remember Python syntax rules

DebLang translates its listed keywords, but it still follows Python's syntax rules:
- Use `:` after `agar`, `warna`, `karya`, loops, and classes.
- Indent the code inside a block (normally four spaces).
- Close brackets and quotation marks.
- Use `#` for comments.

## Practice

Try changing the examples:
1. Ask for two numbers and print their sum.
2. Print the even numbers from 2 to 20.
3. Write a function that returns the cube of a number.
4. Check whether a number is positive, negative, or zero.
