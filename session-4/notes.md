# Session 4: Introduction to Assembly Programming

In some languages, like C, you can write inline C.

Nowadays, the most common reason to understand assembly to be able to read dissambly of a binary to understand what it's doing. Very few people write assembly, because compilers are really good.

There are some narrow cases, like certain  parts of the kernel that need to be written in Assembly.

`li` - just put a value in a register.

When you "Assemble", you'll notice that the real instructions are different than what you wrote (e.g. `li` becomes `addiu` after assembling - `li` is a pseudo-instruction).

RISC (MIPS, ARM) vs CISC: instruction sets were growing in size & complexity, so hardware was getting very complex to implement. Therefore, folks made RISC, which means some instructions required multiple instructions, but everything was faster.

RISC has around 100 instructions vs ~1000 for x86 (CISC).

[TODO: photo of MARS here]

"Address" = address where code resides. "Code" = the actual machine code for the instruction (e.g. `0x24080005` for `addiu $8 5`).

Each Address is going up by 4, which makes sense for 4 byte instructions.

MIPS Registers:

* `$zero` = always points to 0
* `$v` = return values
* `$a` = arguments to a function
* `$t` = temp
* `$s` = saved (push to stack when calling a function)
* `$sp` = top of the last frame of the stack
* `$fp` = top of the stack
* `pc` = Program Counter

`jal X` = initiate a function call

`jr` = jump back at end of a function

What if you call a function inside a function? Save `$ra` on the stack.

Programs only becoming interesting if we can branch.

Notice that `beq $t1 7 foo` is a pseudo instruction that puts `7` in a register first with an `addi`, then runs `beq`.

Inf loop:

```
foo:
    addiu   $t0 $zero   5
    addiu   $t1   $zero 7
    beq $t1 7   foo
    add $t2 $t0 $t1
```

While loop to 5: (do while loops 

```
	addiu  $t0 $zero   0
loop:
	beq	   $t0 5   end
	addi   $t0 $t0 1
	j  loop
end:
```

Loops are high-level constructs that only exist in higher-level languages.

For a very small loop, like in sum-to-10, a compiler with optimizations would use "loop unrolling" and run the contents of the loop 10 times without the branch.

Programs aren't just intstructions, they are also *constants*/*statics* (just hard-coded data included in the program).

`la` = Load Address
`lb` = Load Byte
