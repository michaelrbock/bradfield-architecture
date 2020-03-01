# Session 3 Pre-Work: Binary Encoding

#### Binary to Hex:

* 9 = 0x9
* 136 = 0x88
* 247 = 0xf7

* In CSS, how many colors can be represented in the hexadecimal form?
    * 16^6 = 16,777,216
* How about in the RGB form?
    * 255^3 = 16,777,216

#### Decimal to Binary:

* 12 = 1100
* 9 = 1001
* 1100 + 1001 = 10101 = 21
    * What would the result be if it were constrained to 4 bits?
        * 0101 = 5
* How many numbers can be represented in total with this many bits:
    * 4 -> 16
    * 8 -> 256
    * 16 -> 65,536 ~= 64k
    * 32 -> 4,294,967,296 ~= 4bil

#### Two's Complement:

* 12 = 01100 
* -9 = 10101
* -3 - 4 = 1101 - 0100 = 1001 (add and ignore carries)

* What are the largest and smallest numbers representable in 32 bit 2’s complement?
    * -2,147,483,648 to 2,147,483,647

#### Big vs. little-endiand

* If you saw port 8000 represented as 0x1f40, would you conclude that TCP uses big-endian or little-endian integers?
    * big-endian
* 3000 = 0xbb8

#### Floating point numbers

* What are the largest and smallest values representable with 64-bit floats?
    * Largest: `0x7FEF FFFF FFFF FFFF × 2^1023` = `1.7976931348623157 × 10^308`
    * Smallest: `-1.7976931348623157 × 10^308`

#### UTF-8

* Is there any additional space cost to encoding a purely ASCII document as UTF-8?
    * No.
* What are the pros and cons detriments of UTF-8 compared to another encoding for Unicode such as UTF-32?
    * UTF-8 is variable-length encoded.
    * UTF-32 is a fixed-length encoding.
