# Session 3: Binary Encodings of Data

## Notes

RGB values in hex = RRGGBB, so pure red = `0xff00000`.

`xxd -b` gives binary representation.

`xxd -g 1` groups output by 1 byte.

The checksum for IPv4 TCP is the 16bit 1's complement sum of all 16-bit words in the header and text. Can only detect *single-bit* errors (if two bits flip oppositely, the checksum will say it's "correct").

Unicode = organization that decides what character = what number.

UTF-8 is an *encoding* for unicode.

UTF-32 = take unicode codepoint as a 32-bit integer (which wastes a lot of space because everything is 4 bytes).

* How to encode a 1-byte (ASCII) char in UTF-8?
    * It's just the ASCII char.
* 2-byte?
    * `110..... 10......`
* 3-byte?
    * `1110.... 10...... 10......`
* 4-byte?
    * `11110... 10...... 10...... 10......`

## Hex

* You have been given a file named hellohex. What is its length in bytes?
    * 17
* If you were to view a hexadecimal representation of the file, how many hexadecimal characters would you expect?
    * 34

`stat -x [file]` gives info about a file.

`xxd -p [file]` gives the "plain" hexadecimal output of a file.

| hex | binary |
|-----|--------|
| `0x68` | `0110 1000` |
| `0x65` | `0110 0101` |
| `0x6c` | `0110 1100` |
| `0x6c` | `0110 1100` |
| `0x6f` | `0110 1111` |

## Integers

### Basic

| decimal | binary     |
|---------|------------|
| 4       | `100`      |
| 65      | `1000001`  |
| 105     | `1101001`  |
| 255     | `11111111` |

| binary    | decimal |
|-----------|---------|
| `10`      | 2       |
| `11`      | 3       |
| `1101100` | 108     |
| `1010101` | 85      |

### Unsigned binary addition

```
  11111111 (255)
+ 00001101  (13)
----------
 100001100 (268)
```

* If my registers are only 8 bits wide, what is the value returned from that binary addition?
    * `00001100` = 12 = `268 % 256`
* What is this phenomenon called?
    * Overflow.

### Two’s complement conversions

| decimal | two's complement |
|---------|------------------|
| 127     | `01111111`       |
| -128    | `10000000`       |
| -1      | `11111111`       |
| 1       | `00000001`       |
| -14     | `11110010`       |

| two's complement | decimal |
|------------------|---------|
| `10000011`       | -125    |
| `11000100`       | -60     |

### Addition of two’s complement signed integers

```
  01111111  (127)
+ 10000000 (-128)
-----------------
  11111111   (-1)
```

* What is the value of the most significant bit in 8-bit two’s complement?
    * -128 
* What about 32-bit two’s complement?
    * -2,147,483,648
    * In general, `-2^(n-1)`
* How do you negate a number in two’s complement?
    * Flip the bits and add 1.
* How can we compute subtraction of two’s complement numbers?
    * Negate the number we want to subtract and add the two numbers.

## Byte ordering and numbers in the wild

* We’ve encoded the number 9001 in the file 9001. Did we use big-endian or little-endian encoding?
    * big-endian.

### TCP

* What is some of the data you’d expect to see in a TCP header in order for TCP to do its job?
    * Source, destination port, Sequence number, Ack number, Data offset, Reserved, Flags, Window size, Checksum, etc.
* What’s the byte ordering of the numbers in a TCP header?
    * big-endian.
* Why is byte ordering a part of the protocol?
    * So different computers agree on what numbers the bits represent.
* Could byte ordering have been encoded in the header? How would you do so?
    * Sure, could have used a bit to represent that?

* What are the values of the sequence number,
    * `0b01000100000111100111001101101000` = 1142846312
* acknowledgment number,
    * `0b11101111111100101010000000000010` = 4025655298
* source port,
    * `10101111 00000000` = 44800
* and destination port?
    * `10111100 00000110` = 48134
* What is the specified length of the TCP header?
    * High order 4 bits of 12 byte: `1000` = 8. 8 * 4 = 32 (number of 32-bit words of header).

## IEEE Floating Point

Decode 32-bit float: `01000010001010100000000000000000`

* Sign bit: `0`
* Exponent: `10000100` (132)
* Significand: `01010100000000000000000` (1.010101[0...] in binary = 1 + 1/4 + 1/16 + 1/64 = 1.328125)

`2^(132-127) * 1.328125` = `2^5 * 1.328125` = 42.5

* For the largest fixed exponent, 11111110 == 254 - 127 = 127 (exponent 11111111 is reserved for the special purpose of encoding infinity), what is the smallest (magnitude) incremental change that can be made to a number?
    * `0 11111110 00000000000000000000000` (`2^127 * 1`) to
    * `0 11111110 00000000000000000000001` (`2^126 * 1 + 1/(2^23)`)
    * = `2^127 / 2^23` = `2^104`
* For the smallest (most negative) fixed exponent, what is the smallest (magnitude) incremental change that can be made to a number?
    * `0 00000000 00000000000000000000000` (`2^-127 * (1 + 0)`) to
    * `0 00000000 00000000000000000000001` (`2^-127 * (1 + 1/(2^23))`)
    * = `2^-127 / 2^23 == 2^-150` = `1/2^150`
* What does this imply about the precision of IEEE Floating Point values?
    * The accuracy of the numbers is much better the closer we are to zero.

## Character encodings

* If you `echo ☃ > snowman.txt` how large do you expect this file to be, considering that the corresponding Unicode code point is U+2603?
    * 3 bytes (not including newline).

`☃ = U+2603`

* If you were to hexdump or xxd the file, what exactly do you expect to see?
    * The code point is `0x26 0x03` or `00100110 00000011`
    * The 3-byte UTF-8 pattern is `1110.... 10...... 10......`
    * So: `11100010 10011000 10000011` (`e2 98 83`)
    * `echo -n ☃ | xxd -b`: `11100010 10011000 10000011`
    * `echo -n ☃ | xxd -g 1`: `e2 98 83`

`echo -n`: `-n` does not print the trailing newline character.

## Encoding MIPS instructions

* `add     $a2 $a0 $a1  // compute $a0 + $a1 and store in $a2`
    * `R` code instruction: opcode (6 bits), rs (5), rt (5), rd (5), shamt (5), funct (6)
    * opcode: `000000`
    * rs: `$a0` = 4 = `00100`
    * rt: `$a1` = 5 = `00101`
    * rd: `$a2` = 6 = `00110`
    * shamt (unused): `00000`
    * funct: `0x20` = `100000`
* `addi    $v1 $v0 25   // compute $v0 + 25 and store in $v1`
    * `I` code instruction: opcode (6 bits), rs (5), rt (5), immediate (16)
    * opcode: `0x8` = `001000`
    * rs: `$v0` = 2 = `00010`
    * rt: `$v1` = 3 = `00011`
    * immediate: 25 = `0000 0000 0001 1001`
