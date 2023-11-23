class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __summation__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __subtraction__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __scalar_product__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __vector_product__(self, other):
        if isinstance(other, Vector):
            return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                          self.x * other.y - self.y * other.x)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return f'x = {self.x:.{2}f} y = {self.y:.{2}f} z = {self.z:.{2}}'


print('Enter vector as: x y z')
x1, y1, z1 = map(float, input().split())
v1 = Vector(x1, y1, z1)
print(f'Vector length: {abs(v1):.{2}f}')
print('Enter a second vector in the same format or a number')
vector = list(map(float, input().split()))
if len(vector) == 1:
    v2 = vector
    print('What action do you want to perform on a vector and a number?: -,+,*?')
else:
    v2 = Vector(*vector)
    print('What action do you want to perform on the vectors?: -,+,*,x?')
print(f'Enter "break" if you want to finish')
while True:
    operator = input()
    if operator == 'break':
        break
    elif operator == '+':
        print(f'Answer: {Vector.__summation__(v1, v2)}')
    elif operator == '-':
        print(f'Answer: {Vector.__subtraction__(v1, v2)}')
    elif operator == '*':
        print(f'Answer: {Vector.__scalar_product__(v1, v2)}')
    elif operator == 'x':
        print(f'Answer: {Vector.__vector_product__(v1, v2)}')
    else:
        print('Try again...')
print('Enter the number of points to calculate the center of mass')
n = int(input())
print('Enter the coordinates of the points and the masses of these points as: x y z m')
M = 0
Set_of_vectors = []
center = Vector(0, 0, 0)
for _ in range(n):
    options_of_vector = list(map(float, input().split()))
    v = Vector(*options_of_vector[:3])
    m = options_of_vector[-1]
    Set_of_vectors.append(v)
    center = Vector.__summation__(center, (Vector.__scalar_product__(v, m)))
    M += m
print(f'Сenter of mass coordinates: {Vector.__scalar_product__(center, (1 / M))}')
print('Enter the number of points to calculate maximum triangle area')
n = int(input())
Set_of_vectors = []
print('Enter the coordinates of the points as: x y z')
for _ in range(n):
    v = list(map(float, input().split()))
    Set_of_vectors.append(v)
S_max = 0
if n > 2:
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                v1 = Vector.__subtraction__(Vector(*Set_of_vectors[j]), Vector(*Set_of_vectors[i]))
                v2 = Vector.__subtraction__(Vector(*Set_of_vectors[k]), Vector(*Set_of_vectors[i]))
                S = abs(Vector.__vector_product__(v1, v2))
                if S > S_max:
                    S_max = S
print(f'Maximum triangle area is: {S_max:.{2}f}')

