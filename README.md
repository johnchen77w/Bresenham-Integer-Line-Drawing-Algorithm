# Bresenham-Integer-Line-Drawing-Algorithm
<pre>
// This is only Octant 1, for the rest of 7 Octants, look through the code
begin
plot (x1, y1) ;
for (i= x1 to x2 by step of 1) {
    if (i== x1 ) { 
        pi=2Δy−Δx ;
    } else {
        if ( pi<0 ) {
            pi=pi+2Δy ;
        } else {
            pi=pi+2Δy−2Δx; 
            y1 ++ ;
        }
    x1 ++ ;
    plot (x1, y1) ;
    }
}
end
