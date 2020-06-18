# pyscanner
Scanner for strings in Python. Based on Java's Scanners.

<h3> Documentation </h3>
Usage of PyScanner is simple. A PyScanner object can be constructed as follows: `scanner = new PyScanner(str)`, where str is the string
you wish to scan. There is an optional parameter, separator, which can be used to define how the scanner partitions strings in
normal usage cases. By default, the separator is a blank space. <br>
To get the next partition from the scanner, use `scanner.next()`. To see if the scanner has another partition, use `scanner.hasNext()`. <br>
There are several built-in variants of next and hasNext, for integers, doubles, and lines. There is also a hasNext and next that take in regex
from the user for easy implementation of other desired items.

<h3> Acknowledgements </h3>
Inspired by Java's scanners. Built with Python3's re library.
