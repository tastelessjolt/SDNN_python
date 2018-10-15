# coding: utf-8
from pstats import Stats
from pstats import SortKey

sp = Stats("profiling.txt")
sp = sp.sort_stats(SortKey.CUMULATIVE)
sp.print_stats()  
