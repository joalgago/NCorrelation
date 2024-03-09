set terminal  jpeg

set output "plotpm.jpg"

set title "Probability that Bob measures -1 after Alice measures +1"
set grid

set xlabel "p"
set ylabel "Probability"
set key right top

set yrange [0:1]
set xrange [0.5:1]

plot 'data' u 1:6 t 'classical teleportation' w p pt 1, \
    '' u 1:7 t '1 bit for maxent' w p pt 4, \
    '' u 1:8 t '1 bit for weakent' w p pt 6, \
    '' u 1:9 t 'quantum' w p pt 8