

import random
import time

names = ['Saiprabhu', 'Madhu', 'Mani', 'Yogesh']
subjects = ['Python', 'Java', 'Blockchain','C#','SQL','spring']

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(subjects)
        }
        yield person

t1 = time.perf_counter()
people = people_list(100000)
t2 = time.perf_counter()

print("Time taken for List: ", t2 - t1)

t1 = time.perf_counter()
people = people_generator(100000)
t2 = time.perf_counter()

print("Time taken for generator: ", t2 - t1)
