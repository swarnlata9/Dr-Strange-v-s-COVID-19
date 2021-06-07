# Dr-Strange-v-s-COVID-19

Input file: standard input\
Output file: standard output\
Time limit: 1 second Memory limit: 256 megabytes\
<br>
A COVID-19 vaccine has finally been found but it’s in a different universe.
There are a total of n universes in this multiverse and Dr Strange can make portals between any of them. They are numbered 1 to n and travelling between any two is only possible through these specially created portals. Earth is in the 1st universe whereas the vaccine is known to be on the nth universe.
Due to the complexity of multiverse space-time continuum, different portals can take an unequal amount of travelling time (in minutes). Dr Strange is too important to leave Earth right now, so he sends Spiderman instead to hop from universe to universe.
Also, some of the universes are captured by Dark Forces and are patrolled by demons at specific time instances. In order to pass through them, Spiderman has to hide there until it’s safe. If Spiderman arrives at a universe at time t and it is marked unsafe at time t, then Spiderman would have to hide until the next safe minute arrives.
Since Earth is in dire need of the vaccine, Dr Strange decides to get it at the earliest. With information about the portal travel time and unsafe minutes for each universe, help Dr Strange make the fastest route for Spiderman to take, in order to reach the vaccine.
Input
The first line contains two space-separated integers: n, the number of universes and m, the number of portals.
Then m lines follow, ith line contains three integers, universe ai and bi, connected through the ith portal
and ci, the travelling time between the mentioned universes.
Then n lines follow, ith line contains ki, number of time instances when the demons are patrolling the ith universe. Then ki space separated integers tij follow in sorted order. tij means that at this timestamp some demon was patrolling on the ith universe and the spiderman had to wait for this second (if he is at this universe at this timestamp).\
Constraints:\
2 ≤ n ≤ 105\
0 ≤ m ≤ 105 1 ≤ a,b ≤ n 1 ≤ c ≤ 104\
0 ≤ ki ≤ 105 ; sum of ki < 105\
0 ≤ tij ≤ 109\
Output\
Print a single number — the least amount of time spiderman needs to get from universe 1 to universe n. If spiderman can’t get to universe n in any amount of time, print number -1.

<br>
<br>
<br>
solution:

The file "solution.py" contain the code for it.\
when we run code it ask for input.\
<br>

The first line contains two space-separated integers: n, the number of universes and m, the number of portals.\
Then m lines follow, ith line contains three integers, universe ai and bi, connected through the ith portal
and ci, the travelling time between the mentioned universes.\
Then n lines follow, ith line contains ki, number of time instances when the demons are patrolling the ith universe. Then ki space separated integers tij follow in sorted order.tij means that at this timestamp some demon was patrolling on the ith universe and the spiderman had to wait for this second (if he is at this universe at this timestamp).
