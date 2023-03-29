# Timing Array Initialization

**March 2023**

## Description

Here I compare the runtime of initializing a 30,000,000 integer array over 5 trials or array-like data structure in the following languages: 

* C
* C++
* Go
* Java
* Python

## Platform

* 64-bit Ubuntu 22.04.2 LTS
* gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
* g++ (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
* go version go1.20.2 linux/amd64
* OpenJDK Runtime Environment (build 11.0.18+10-post-Ubuntu-0ubuntu122.04)
* Python 3.10.6

## Hardware

* 12th Gen Intel® Core™ i5-1235U × 12
* 8.0 GiB

## Running

* Run `python3 timer.py`.

## Results

Here are the results from one run:

| Operation | Description | Runtime Mean ± Standard Deviation |
|---|---|---|
| malloc | C program that just calls `malloc`. | 0.000220±0.000013 |
| calloc | C program that just calls `calloc`. | 0.000369±0.000104 |
| new | C++ program that just calls `new`. | 0.001252±0.000124 |
| memset | C program that calls `malloc` then 0-initializes with `memset`. | 0.038716±0.005013 |
| array	| go program that makes an `array`. | 0.040204±0.002686 |
| np_empty | Python program that calls `numpy.empty`. | 0.070044±0.000480 |
| np_zeros | Python program that makes a 0-initialized `numpy.ndarray`. | 0.071190±0.001795 |
| jarr | Java program that makes an integer array with `new`. | 0.080597±0.009322 |
| list_init | Python program that initializes a list to be all 0s with the list `*` operator. | 0.150273±0.001312 |

## Contributers 

* [Chami Lamelas](https://sites.google.com/brandeis.edu/chamilamelas) - Author
