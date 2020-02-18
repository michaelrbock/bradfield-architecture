# Session 1 Pre-Work: The Fetch-Decode-Execute Cycle

Prior to class, please do two things:

1. A diagram you have drawn of the main components of a computer, and how they are connected; and,
1. A paragraph or two of prose describing your understanding of the fetch-decode-execute cycle, and how the relevant components of the computer are involved in each step.


## 1. Main Components of a Computer

### CPU

Consists of two parts:

* Control Unit
* Arithmetic/logic unit

The CPU interacts closely with primary storage, aka main memory, which holds temporary data.

Secondary storage holds permanent or semi-permanent data.

#### Control Unit

The Control Unit of the CPU uses electrical signals to direct the entire computer system to execute stored program instructions. The control unit does not execute program instructions; rather, it directs other parts of the system to do so. The control unit must communicate with both the arithmetic/logic unit and memory.

#### The Arithmetic/Logic Unit (ALU)

The Arithmetic/Logic Unit (ALU) executes all arithmetic and logical operations. It can perform:

* Four kinds of arithmetic/mathematical operations:
    * addition, subtraction, multiplication, division
* Logical operations:
    * Can compare numbers, letters, or special characters:
    * equal-to, less-than, or greater-than
    * Can simultaneously test for more than one condition, giving us six logical relationships

#### Registers: Temporary Storage Areas

Registers are temporary storage areas for instructions or data. They are not part of main memory and offer a speed advantage.

Registers work under the direction of the control unit to accept, hold, and transfer instructions or data and perform arithmetic or logical comparisons at high speed.

Computers usually assign special roles to certain registers:

* An **accumulator**, which collects the result of computations.
* An **address register**, which keeps track of where a given instruction or piece of data is stored in memory.
* A **storage register**, which temporarily holds data taken from or about to be sent to memory.
* A **general-purpose register**, which is used for several functions.

### Memory and Storage (RAM)

Memory is the part of the computer that holds data and instructions for processing. Memory is separate from the CPU. Memory stores program instructions/data for only as long as the program they pertain to is in operation:

* Memory only stores items while the computer is turned on.
* When several programs are running, a single program cannot lay exclusive claim to memory.
* Memory may run out of room.

The control unit sends data/instructions from input to memory and from memory to the ALU. After being processed by an operation on the ALU, the info is sent to memory.

Memory allows very fast access to instructions and data, no matter where the items are within it.

#### RAM Details

Most data goes into RAM first (from permanent storage or an input device).

RAM speed is controlled by **bus width** (the number of bits that can be sent to the CPU) and **bus speed** (the number of times a group of bits can be sent each second). A **bus cycle** occurs every time data travels from memory to the CPU. For example, a 100-MHz 32-bit bus is theoretically capable of sending 4 bytes of data to the CPU 100 million times per second.

In reality, RAM doesn't usually operate at optimum speed. **Latency** changes the equation radically. Latency refers to the number of clock cycles needed to read a bit of information. The first bit takes extra time to read. For example, RAM rated at 100 MHz is capable of sending a bit in 0.00000001 seconds, but may take 0.00000005 seconds to start the read process for the first bit.

**Burst mode** compensates for latency and depends on the expectation that data requested by the CPU will be stored in sequential memory cells. The memory controller anticipates that whatever the CPU is working on will continue to come from this same series of memory addresses, so it reads several consecutive bits of data together. This means that only the first bit is subject to the full effect of latency; reading successive bits takes significantly less time.

The **rated burst mode** of memory is normally expressed as four numbers separated by dashes. The first number tells you the number of clock cycles needed to begin a read operation; the second, third and fourth numbers tell you how many cycles are needed to read each consecutive bit in the row, also known as the **wordline**. For example: 5-1-1-1 tells you that it takes five cycles to read the first bit and one cycle for each bit after that. Lower = better performance.

**Pipelining** also minimizes the effect of latency by simultaneously reading one or more words from memory, sending the current word or words to the CPU and writing one or more words to memory cells.

The speed and width of the memory's bus should match the system's bus. Even with a wide and fast bus, it still takes longer for data to *get* from the memory card to the CPU than it takes for the CPU to actually *process* the data.

#### Caches

**Caches** allieviate the bottleneck of sending data between the CPU and RAM.

The **primary/level 1 (L1)** cache is small and built into the CPU. They are usually split into L1d (for data) and L1i (for instructions). There are also L2-L4 caches.

These days the L2 is basically always integrated into the CPU, as is L3 and if it exists L4. For instance a brand new Intel CPU will have dedicated L1 and L2 per CPU core, and then a shared L3 across cores (and for some CPUs, also an L4 shared between all the cores as well as the onboard GPU).

**Static randon access memory (SRAM)** is used for caches. SRAM uses multiple transistors for each memory cell. It has an external gate array known as a **bistable multivibrator** that switches between two states. This means that it does not have to be continually refreshed like DRAM. Each cell will maintain its data as long as it has power. Without the need for constant refreshing, SRAM can operate more quickly.

The SRAM in the cache can be **asynchronous** or **synchronous**. Synchronous SRAM is designed to exactly match the speed of the CPU.

#### Other points about Memory/Storage

Memory is **tiered**: by using expensive memory in small quantities and then backing it up with larger quantities of less expensive memory.

The **bit size** of a CPU tells you how many bytes of information it can access from RAM at the same time. For example, a 16-bit CPU can process 2 bytes at a time (1 byte = 8 bits, so 16 bits = 2 bytes), and a 64-bit CPU can process 8 bytes at a time.

**Megahertz (MHz)** is a measure of a CPU's processing speed, or **clock cycle**, in millions per second. For example, a 32-bit 800-MHz CPU can potentially process 4 bytes simultaneously, 800 million times per second (possibly more based on pipelining).

## 2. How the CPU Executes Program Instructions

### Overview

Before an instruction can be executed, program instructions and data must be placed into memory. Once the necessary data and instruction are in memory, the central processing unit performs the following four steps for each instruction:

1. The control unit fetches (gets) the instruction from memory.
1. The control unit decodes the instruction (decides what it means) and directs that the necessary data be moved from memory to the arithmetic/logic unit.
1. The arithmetic/logic unit executes the arithmetic or logical instruction. That is, the ALU is given control and performs the actual operation on the data.
1. Thc arithmetic/logic unit stores the result of this operation in memory or in a register.

The control unit eventually directs memory to release the result to an output device or a secondary storage device.

Each central processing unit has an internal clock that produces pulses at a fixed rate to synchronize all computer operations. A single machine-cycle instruction may be made up of a substantial number of sub-instructions, each of which must take at least one clock cycle.

The location in memory for each instruction and each piece of data is identified by an address. A memory location can hold only a fixed amount of data.

### Details

#### Components

* **Program Counter (PC)**: stores the memory address of the *next* instruction.
* **Memory Address Register (MAR)**: stores the address of the memory to-be-loaded/stored.
* **Memory Data Register (MDR)**: the contents pointed at by the MAR are loaded here.
    * It is a two-way register that stores data being *loaded from* or *stored into* memory.
* **Current Instruction Register (CIR)**: if an instruction is loaded into the MDR, it is copied here.

#### Cycle

Fetch:

1. The PC points to the address of the next instruction to execute.
1. The address stored in the PC is copied into the MAR.
1. The CPU takes the instruction stored at the address in the MAR and copies it into the MDR.
    * A signal is sent through the **address bus** to the RAM.
    * The CU sends a memory read signal and the contents of the address are copied through the **data bus** to the MDR.
1. The instruction in the MDR is copied into the CIR.
1. The PC increments to point to the next instruction to be executed.

Decode:

The Control Unit (CU) decodes the instruction in the CIR:

1. The instruction is sent via the data bus to the CU where it is split into two parts.
    * The first part is the **opcode**, the command.
    * The second part is the **operand**, the address in RAM where data will be read/written.
1. The CU can translate opcodes into instructions.

Execute:

The CU oversees this process.

1. If the instruction is a load/store, the MAR and MDR are used as temporary storage between the CPU and memory.
1. If the instruction is requires the ALU (or floating point unit, FPU), they do the required work by instruction from the CU via the control bus.
1. Most instructions write the result of some computation into a register (except store/branch/jump).

## Feynman Computer Heuristics Lecture

[Video](https://www.youtube.com/watch?v=EKWGGDXe5MA)

Which actual physical components correspond to each of Feynman’s metaphors. For instance, what are the physical equivalents of the "cards" that Feynman describes, and what hardware is used to "file" as opposed to "process" these cards?

* Cards = instructions & data in memory.
* "File" = CPU loading/storing data from memory.
* "Process" = CPU, CU, ALU.
* Basement = secondary storage.

## Two's Complement

How to get from a positive representation to a negative representation? E.g. 3 to -3?

Invert all bits (bitwise complement) and add 1.

3 = `0011`

-3 = `1101`
