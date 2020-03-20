import sys

assert len(sys.argv) == 3
source = sys.argv[1]
target = sys.argv[2]
assert len(source) == len(target)

map = dict()

for i in range(len(source)):
    if source[i] in map and map[source[i]] != target[i]:
        print("false")
        exit(0)
    map[source[i]] = target[i]

print("true")
