# Session 1: The Fetch-Decode-Execute Cycle

Computers have many leaky abstractions.

Examples:

* NPE, of errors/bugs that actually point to things below the language you're working in.
* Segfault (segment ~= page in modern parlance): trying to write to somewhere in memory that you're not allowed to (maybe the instruction segment).
* Overflow error (go over the size of your registers).
    * Underflow errors in floats = getting too close to 0 (e.g. when you divide by 2 too many times), it's too small.
    * You can do this with positive or negative numbers. This is how you get `-0`.
* Exceeding the call stack (stack overflow). Running out of space that stores the state of your function. Use stack for: function calls, closures, recursion.
    * To "pop" the stack, just increment the *stack pointer* to poin to the next frame (don't zero-out the frame itself).
    * The OS smartly doesn't zero-out data until its needed next.

The ALU operates on *input* registers and outputs to registers as well.

Your ints can't be larger than the size of your registers (e.g. 64).

2^32 = 4 billion.

1 << 64 = shift a 1 bit to the left 64 times. (Each shift is doubling).

Python/Ruby hide this from you under the hood: they do the handling of the larger-than-register value for you (more than 1 add ALU procedure). Or e.g. Karatsuba's for multiplication.

Floats: `0.1 + 0.2 = 0.30...04` <- IEEE 754 floating point. hardware does this because we have a *limited* number of bits to represent our floats. Analogy to representing `1/3` as a decimal.

Floats, instead of having a 1's, 2's, 4's place, we have `1/2`, `1/4`, `1/8` places.

`NaN` is a special floating point value.

* Threads run inside processes.
    * Each process has it's own memory space. E.g. address 20 is different in each process (even if it's the another process instance of the same program).
    * There is a feature to allow you to run processes across multiple CPU cores while sharing the same address space.
    * Threads have separate stacks (so they can call functions).

* CPU core = independent set of registers/ALUs, to allow us to run things in parallel.
* SMP = symmetric multiprocessing. 

```
int n = 0;

// Run in two threads:
for (int i = 0; i < 5; i++) {
    n += 1;
}
```

There is a race condition above because an increment is actually *not* a single *atomic* operation (it's a read, increment, write).

## A program

`file /bin/ls` = 64-bit, x86. This executable is compiled for a 64-bit computer. x86_64 = the instruction set architecture Intel uses. This program can't run on other architecutres. `Mach-0` = kernal name for Mac OS.

This course uses MIPS.

Why go from 32 to 64 bits?

* Beacuse we store pointers in registers to do reads/writes from registers.
* So you could only address ~4B bytes ~= 4GB.
* A byte = how much data you get from 1 adress in RAM (almost always 8 bits now).

Why not go to 128?

* Would need to have really large buses.
* Don't really need to get bigger than 2^64 RAM.

`cat /bin/ls` = a bunch of garbage because it's all machine code (instructions to be sent to the CPU). `cat` is a mis-interpretation of machine code as ASCII/utf-8.

007 = bel in ASCII.

`strings /bin/ls` gives you useful strings in a file.

* `/bin/ls` lives on persistent storage, so we *ask* the OS to load the program into memory.
    * API for a process to call to start a new process, e.g. `bash` to start `ls`: make a *system call* to the OS to *ask* for it to do something for you.
    * Exec is the system call for starting a new process.
        * First `fork` starts a new copy of the same process, then `exec` replaces the current program with a new program.
* Read the program from disk, load it (instructions and data) into memory.
* How does the OS/kernal start the program? Right now, the OS is fetching/decode/executing...
    * The PC gets set to the first instruction address of the program.
    * And now the program is off and running, with the PC pointing to the next instructions.
* When does the PC *not* go to the immediate next instruction *sequentially* in memory?
    * When you call a function.
        * You need a calling convention (instructions just to set up the call/stack to the function correctly).
    * Decisions (if/switch).
        * There are low-level instructions (branch-if).
    * Loops.
    * Actually a GOTO.

How many times/second does the FDE cycle happen per-second? 4GHz = 4 billion cycles or ticks per second. Clock happens every 1/4 of a nanosecond.

1 clock tick ~= F/D/E.

Really, there is a pipeline of instructions happening at the same time. So an instruction moves through a F, D, E cycle over a few clock ticks (while others are going at the same time).

Moores law = every ~18 months the # of transistors you can fit in the same amount of space doubles. Dennard scaling = making transistors smaller. This is done.

*Timer interrupt* = a *hardware* mechanism to periodically the PC points to the kernal instead of the program. So the program can be stopped/paused by the OS.
