# Session 4 Pre-Work: Introduction to Assembly Programming

## CS 61C MIPS Intro Lectures

### [Lecture 1](https://archive.org/details/ucberkeley_webcast_zUYCZYKaUrk)

RISC = Reduced Instruction Set Computing (backlash against adding tons of instructions, limits the number of instructions and optimizes hardware to execute those).

Unlike in C, assembly cannot use variables; it uses registers instead, which are limited in number, but *very* fast.

32 registers in MIPS. Each MIPS register is 32 bits wide (a "word").

Registers are numbered from 0 to 31: $0 to $31:

* $16-$23 = $s0-$s7 (corresponds to C variables)
* $8-$15 = $t0-$t7 (temporary variables)

In Assembly, there are no types or type checking.

Addition in MIPS Assembly: `add $s0,$s1,$s2`.

Subtraction: `sub $s3,$s4,$s5`.

To write, `a = b + c + d - e;`, break it down:

```
add $t0, $s1, #s2 # comment
add $t0, $t0, $s3
sub $s0, $t0, $s4
```

Use temporary registers instead of overwritting saved registers.

*Immediates* are numerical constants that appear in code:

`addi $s0,$s1,-10` == `f = g - 10`

`add $s0,$s1,$zero` (hardcoded 0 register, this equals assign: `f = g`).

Remember overflow can occur with the limit size of registers.

`add`, `addi`, and `sub` cause overflow to be detected.

`addu`, `addiu`, `subu` (unsigned) does not cause overflow to be detected.

#### Data Transfer: Load from and Store to memory

Write data = store to memory. Read data = load from memory. (From the perspective of the CPU).

Memory Addresses are in Bytes (8 bits), *not* words (1 word = 4 bytes). Word addresses are 4 bytes apart (same as leftmost byte in big-endian).

Transfer *from* memory to register: `lw` (load).

C code: `int A[100]; g = h + A[3];`

MIPS: `lw $t0,12($s3) # Temp reg $t0 gets A[3]`. The contents of `$s3` becomes a pointer to the start of the array in memory, with a 12 byte (3 words) offset to point to element 3. Then `add $s1,$s2,$t0`. `$s3` = base register (pointer), `12` = offset in bytes.

Transfer from register *to* memory: `sw` (store).

C code: `int A[100]; A[10] = h + A[3];`

MIPS: 

```
lw $t0,12($s3)  # Temp reg $t0 gets A[3]
add $s1,$s2,$t0 # Temp reg $t0 gets h + A[3]
sw $t0, 40($s3) # A[10] = h + A[3]
```

Address offsets *must* be in multiples of 4 (e.g. `$s3+12` and `$s3+40`).

`lb` = Load byte. e.g. `lb $s0, 3($s1)` - top bit is "sign extended" with top bit of byte copied to rest of word. `lbu` just fills with 0's.
`sb` = Store byte.

Registers are about 100-500 times faster than going to memory in terms of latency of access.

**MIPS Logical Instructions**

Bit-by-bit:

* AND `&` `and` 
* OR `|` `or`
* NOT `^` `not`
* Shift left `sll` (`sll $s1,$s2,2`, inserting 0's on the right).
* Shift right `srl`.
* Shift right arithmetic (maintaining sign bit) `sra`.

**Computer Decision Making**

MIPS *if-statement*: `beq reg1,reg2,L1` (branch if equivalent, jump to label L1, each instruction has an optional label, otherwise go to next statement). `if (reg1 == reg2)`.

`bne` = branch if not equal.

Types of Branches:

* Branch = change of control flow
* Conditional Branch: `beq`, `bne`.
* Unconditional Branch: `j` (jump) - always branch.

## [Lecture 2](https://archive.org/details/ucberkeley_webcast_DEqOkfYhDS4)

A program is stored in Memory itself. One MIPS instruction = 32 bits (4 bytes).

The Assembler converts human-readable (.S) code into machine code files (.o), combined with pre-built object files by a Linker into a machine-code executable file (.out).

Executing a program = the PC points to the next instruction in memory, loads it, and moves the PC to the next instruction.

**Decision Making**: (see above). Example *if statement*:

```
if (i == j)
    f = g + h;
```

```
      bne $s3,$s4,Exit
      add $s0,$s1,$s2  # Falls through if it doesn't jump to Exit.
Exit: ...
```

Example *if-else statement*:

```
if (i == j)
    f = g + h;
else
    f = g - h;
```

```
      bne $s3,$s4,Else
      add $s0,$s1,$s2
      j Exit
Else: sub $s0,$s1,$s2
Exit: ...   
```

More than `==` and `!=`, use "Set on less than": `slt reg1,reg2,reg3` means:

```
if (reg2 < reg3)
    reg1 = 1;
else reg1 = 0;
```

`if (g < h) goto Less;` = `slt $t0,$s0,$s1` `bne $t0,$zero,Less` (often use `bne`/`beq` after a `slt`).

`sltu` treats input registers as unsigned.

`slti` tests against constants: `slti $t0,$s0,1`

**Six Steps for Calling a Function**

1. Put params in a place where function can access them.
1. Transfter control to function.
1. Acquire local storage resources needed for function.
1. Perform desired task of function.
1. Put result value in a place where calling code can access it and restore any registers you used.
1. Return control to point of origin (since functions can be called from many places).

**MIPS Function Calling Conventions**

* `$a0` - `$a3`: four *argument* registers to pass params.
* `$v0` - `$v1`: two *value* registers to return values.
* $ra: return address to return to point of origin.

Example:

```
... sum(a, b); ...
}
int sum(int x, int y) {
    return x + y;
}
```

```
add $a0,$s0,$zero # x = a
add $a1,$s1,$zero # y = b
addi $ra,$zero,1016 # return address of caller.
j sum
...
sum: add $v0,$a0,$a1
jr $ra # jump register
```

`jal` = Jump And Link (writes return address `$ra` with *following* instruction and goes to label, replaces `addi` and `j`). This was built to make the common case faster.

`jr` = Sets PC to address specified in the register.

The *caller* of a function puts arguments in registers `$a0` - `$a3` and uses `jal X` to invoke *callee*. `jal X` puts *next* instruction (e.g. current instruction address + 4) in `$ra`.

Where are old register values saved to restore them after function call? 

* Need a place to save old values before call function, restore when return, and delete.
* We use the *stack* for this: last-in-first-out queue.
    * Push and pop
    * The stack is in memory, so we need to point to it.
    * `$sp` is the stack pointer in MIPS.
    * By convention, push decrements `$sp`, pop increments.

TODO: Insert Figures here.

To call a function:

1. Adjust stack by decrementing `$sp`.
1. Save registers for use afterwards.
1. Do function.
1. Restore registers.
1. Adjust stack back by incrementing `$sp`.
1. Jump back to calling routine.

How about a funciton calling a function or recursion? E.g. nested functions, so need to know where to return to and then where to return from *that*.

* Save this info on the *stack*.

**Optimized Function Convention**

MIPS divides registers into two categories:

* Preserved across function calls
    * Caller can rely on.
* Not preserved across function calls
    * Caller cannot rely on them: return value registers, argument registers, temp regisers.

Allocating space on the stack with each function call is called a *stack frame*.
