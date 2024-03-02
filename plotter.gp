set terminal  jpeg

set output "plotmm.jpg"

set title "Probability that Bob measures -1 after Alice measures -1"
set grid

set xlabel "p"
set ylabel "Probability"

set yrange [0:1]
set xrange [0.5:1]

plot 'data' u 1:11 t 'ctp method' w p pt 1, \
    '' u 1:12 t 'quantum' w p pt 4