# Estimating pi by throwing darts at a dart board.

We assume that darts are thrown at a square board with an equally likely probability of hitting all points on the board. If we count the number of darts that hit an inscribed circle we can estimate pi:

> The ratio of A/B will in fact be $\pi/4$ if A is the number of darts in the circle and B is the number of darts thrown.

This repo contains some code that simulates the throwing of the darts.

## Usage

    python Estimate_pi.py 500

This returns:

    ----------------------
    500 darts thrown
    pi estimated as:
        3.112
    ----------------------

*but* also outputs a plot:

![500 darts thrown](500_darts.png)

If we throw 5000 darts we get:

![5000 darts thrown](5000_darts.png)

If we throw 50000 darts we get:

![50000 darts thrown](50000_darts.png)

# License Information

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/us/) license.  You are free to:

* Share: copy, distribute, and transmit the work,
* Remix: adapt the work

Under the following conditions:
