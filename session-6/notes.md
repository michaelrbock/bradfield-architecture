# Session 6: Sequential Circuit Components

With cross-connected NOR gates, the initial state is non-deterministic, but it's stable! Have to add additional inputs (S & R) to be able to choose saved state.

At first, you have to "hold" the input to keep the output. We don't want to have to do that though.

Every time you click R, Q is 0, every time you click S, Q is 1 (Q-bar is the opposite of Q).

Instead of two inputs (S & R), we'd prefer one input: data (D) that sets the output, along with an Enable (E) input (that we'll connect to the clock tick): this is a D Latch.

D flip flops makes up SRAM. DRAM is simpler (and used for main memory). SRAM is used for CPU caches.

On a hot day, your CPU runs slower than on a cold day. (It's OK that the clock isn't perfectly consistent).

We use a quartz cyrstall oscillator to create the clock ticks. We then turn a sine wave into a square wave: take each rising or falling edge to equal the clock cycle (want transition period to be as short as possible).

How to actually detect the rising/falling edge of the clock signal?

TODO: diagram of detection circuit. There's a little bit of propogation delay in the NOT gate, so very briefly, we get a 1 on the output.

The clock tick is sent into any *stable* component (register).
