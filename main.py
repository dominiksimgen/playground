import random, math

def create_testdata(dataset_size):
    dataset = random.sample(range(1,dataset_size*2),dataset_size)
    dataset.sort()
    return dataset

def binary_search(dataset, target):
    u = 0
    o = len(dataset) -1
    while (u <= o):
        m = math.floor((u + o) / 2) #alternatively floor division could be used: " m = (u + o) // 2 "
        if dataset[m] > target:
            o = m - 1
        elif dataset[m] < target:
            u = m + 1
        else:
            return True


testdata = create_testdata(1024)

if (binary_search(testdata, 2000) == True) :
    print("Found!")
else:
    print("Not found")


for i in range(0,5):
    print(i)

