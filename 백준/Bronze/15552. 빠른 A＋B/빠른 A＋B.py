import sys
i = int(sys.stdin.readline())
for j in range(i):
    x, y = map(int, sys.stdin.readline().split())
    z = x+y
    sys.stdout.write(str(z)+'\n')