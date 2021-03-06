Code that numerically integrates the n-body problem, based on a rudimentary scheme for 2nd order ode (an euler method). Can plot sections of the configuration space, and
the trajectories of all the coordinates of all n bodies.

Example usage of config_plot3D(code) function:

This function is essentially a projection of the trajectory of the system in its 3n dimensional configuration space to 3 dimensions (here, being the axes of the ith, jth, kth bodies) (only 3 of the dimensions of the configuration space can be plotted, obviously)

For 3 bodies (0, 1, 2), config_plot3D([0,2,1,1,2,0]) plots the section of the configuration space with the trajectory of the z coordinate of the 0th body, yth coordinate of the 1st body and x coordinate of the 2nd body.

The 'code' parameter is the list [ith body, coordinate of ith body to plot, jth body, coordinate of jth body to plot, kth body, coordinate of kth body to plot].


A consequence of this is that the actual trajectory of a single body in space can be plotted.

For example config_plot3D([0,0,0,1,0,2]) plots the trajectory of the 0th body in 3D space. 

There is so much information in the configuration space and its projections!
