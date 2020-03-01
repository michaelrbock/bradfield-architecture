# Session 2: Lab: Writing a Virtual Machine

If you're the Python/Java VM, you're executing bytecodes. Bytecodes are machinecode-like instructions. Why use bytecodes?

* Portability: allows you to run on multiple architectures (e.g. Java JVM).
    * vs something compiled directly to a x86 Mach-0 architecture.
* Speed: now you don't have to re-compile every time.

`.pyc` files are caches of the bytecodes.

Big-endian byte ordering = bigger number is on the left (normal).

Little-endian is the opposite.

Intel is little-endian; ARM is big-endian.

LLL = little-endian, low-order, left

