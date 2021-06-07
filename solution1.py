def covidvvacc(l, a, h):
    t = [float('inf')] * a
    t[0] = 0
    z=0

    for x in range(a):
        for y in range(a):
            if l[x][y] != -1:
              if t[x]+l[x][y] in h[y]:
                z=1
              else:
                z=0
              if t[y] > t[x] +z+l[x][y]:
                t[y] = t[x] + z+l[x][y]
    if t[a-1] !=float('inf'):
      print(t[a-1])
    else:
      print(-1)
if __name__ == '__main__':
  l=input().split()
  a=int(l[0])
  b=int(l[1])
  l=list()
  for i in range(a):
    l1=list()
    for j in range(a):
      l1.append(-1)
    l.append(l1)
  for i in range(b):
    k=input().split()
    c=int(k[0])
    d=int(k[1])
    e=int(k[2])
    l[c-1][d-1]=e
  h=list()
  for i in range(a):
    x=input().split()
    qq=list()
    for j in x:
      qq.append(j)
    h.append(set(qq))

  covidvvacc(l,a,h)