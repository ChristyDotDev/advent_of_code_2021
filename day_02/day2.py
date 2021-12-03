f = open('input.txt', 'r+')

x = 0
y = 0
for line in f.readlines():
    val = int(line.split()[1])
    direction = line.split()[0]

    if direction == 'forward':
        x += val
    elif direction == 'down':
        y += val
    elif direction == 'up':
        y -= val

print(x * y)
f.close()
