1. Choose you base
between 3 to 13

2. Choose your symbols
Base 13
0
1
2
3
4
5
6

3. write upto 3 digits in your base
Base - 7
00
01
02
03
04
05
06
10
11
12
13
14
15
16
20
21
22
23
24
25
26
30
..
..
66
100

4. Add/subtract single digit in your base
base - 12
0, 1, .... 9, A, B
10,        19, 1A, 1B, 
20, 

1 + 1 = 2
8 + 1 = 9
9 + 1 = A
9 + 2 = B
9 + 3 = 10


9 + 9 = 9 + 3 + 6 = 10 + 6 = 16
A + A = A + 2 + 8 = 10 + 8 = 18
9 + 1 + 9 + 1 = 16 + 2 = 18
8 + 7 = 13

B - 1 = A
B - 2 = 9
A - 1 = 9
A - 2 = 8

5. Base64
0-9, A-Z, a-z, =, +

6. Write strategy to print next number in a number system. A system is a sequence of symbols
next_number(symbols="0123456789AB", "1") -> 2
next_number(symbols="0123456789AB", "B") -> 10
next_number(symbols="0123456789AB", "111") -> 112
next_number(symbols="0123456789AB", "BB") -> 100
next_number(symbols="0123456789AB", "ABAB") -> ABB0

0123456789AB
    A + 1 = B
    B + 2 = 11

print first n digits in symbols="0123456789AB"
    next_number(symbols="0123456789AB", "0") -> 1
    next_number(symbols="0123456789AB", "1") -> 2
    ..
    n times

7. Add two numbers at least 5 pairs.
# Base 12

[1]
1 1
1 B
------
3 0

A 1
B 2
----
19 3
----


8. Write an strategy to add two numbers of multiple digits in your base.

Prompt: 
    Write an code to add two numbers of multiple digits in any base represented by symbols
    add_two_numbers(symbols="0123456789AB", "11", "1B") -> "30"
    add_two_numbers(symbols="0123456789AB", "1119", "BB") -> "1218"

add_two_numbers(symbols="0123456789AB", "11", "1B") -> "30"
add_two_numbers(symbols="0123456789AB", "1119", "BB") -> "1218"

# Base4
add_two_numbers(symbols="0123", "11", "12") -> "23"
add_two_numbers(symbols="0123", "11", "33") -> "110"

9. Subtract two numbers at least 5 pairs.

10. Multiplication
A. Multiply single digits
Base 7
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 11 = 6 + 2
2 * 5 = 13 = 11 + 2
2 * 6 = 15 = 13 + 2

3 * 1 = 3
    2 = 6
    3 = 12
    4 = 15
    5 = 21
    6 = 24

4
11
15
22
26
33

5
13
21
26


[2, 3, 4, 5, 6] * [2, 3, 4, 5, 6]

2 * 3 = 3 * 2

B. Multiply multiple digits

base 7
15 * 34 = 606
26 * 14 = 433
45 * 34 = 2256

Q: Write code to prepare the tables as array of base * base - 2D list containing your table.
base 7 - 0*0 to 6*6 (49)

If you are not good with code yet,
    1. Write down the strategy to solve a problem
    2. Get chatgpt to code it for you. Make the code run. 
    3. Go through stepwise in the code and try to understand what's going on there  - put the print statements.
    4. Compare your strategy in step 1 with chatgpt's strategy.

Q: Write code to multiply numbers, you can use the tables and add_two_numbers()

multiply("15", "34") -> 606

Q: What is the minimum base possible? Is the negative base makes sense? Is base 0 makes sense? 
Justify your answers.

Ans: 
A. 2
0
1
10
11
100
101
110
111
...

B. 1 (Tally)
1
11
111
1111
...

Note: Information Theory - We will learn how to convert our Input into base 2 such that we use minimum digits.

Q: In base 10, with one digit how many numbers can you represent?
10

Q: In base 10, with 2 digits how many numbers can you represent?
100

Q: In base 10, with 3 digits how many numbers can you represent?
1000


Q: In base 12, with 3 digits how many numbers can you represent?
12**3 = 12 * 12 * 12

Q: In base b, with 3 digits how many numbers can you represent?
B ** 3

Q: In base b, with d digits how many numbers can you represent?
B ** d

B**d = N
d = logB(N)

Q: You have a base 12 and to represent 1 million numbers, how many maximum digits do you need?
12 ** n = 1000_000
n = log12(1000_000)

Q: How would you find n?
16 ** n = 1000_000

n = log16(1000_000)

Q: How would find square root of 456. Try guessing and verifying starting a from l= 1 and right = 50. Use python as your calculator.

Q: Which all kind of problems can be solved with binary search?
A: Try various problems: 
    - finding cube root
    - square root
    - find that value of x for which x**2 - 10x + 4 is minimum, Can you use binary search.
    - find if a number exists in a sorted and unsorted list of numbers.
    - 

Q: What is Log?
log10(10) = 1
log10(100) = 2

log(N) = number of zeros in a number.
2000 -> 3.3

A**B = N
B = logA(N)

# 
B ** d = N

d = logB(N)

B ** logB(N) = N

log(A*B) = log(A) + log(B) # zeros get added when we are multiplying - 10 * 100 = 1000

# Information theory say:
To representing an ambiguity of p = -log(p) bits
- log(1) -> 0 bits

# Sound
Sensitivity was proportion to the log of sound.
decibel log10(actual_sound)

- virus spread
- nuclear reactions

- Take a paper and keep folding it half. The thickness
1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8k, 16k, ....

