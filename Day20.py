import sys


def get_particles():
    with open("data/day20.txt") as f:
        d = [[[int(part) for part in vector[3:-1].split(",")] for vector in line.strip("\n").split(", ")] for line in f]
    return d


def find_maximum_distance(particles):
    particles_copy = particles[:]
    for _ in range(1000):
        for particle in particles_copy:
            for index in range(len(particle[1])):
                particle[1][index] += particle[2][index]
            for index in range(len(particle[0])):
                particle[0][index] += particle[1][index]

    closest_particle_distance = sys.maxsize
    closest_particle = None
    for index in range(len(particles)):
        distance = find_distance(particles[index][0])
        if distance < closest_particle_distance:
            closest_particle_distance = distance
            closest_particle = index
    return closest_particle


def find_distance(position):
    distance = 0
    for element in position:
        distance += abs(element)
    return distance


def find_particles_remaining(particles):
    particles_copy = particles[:]

    for _ in range(1000):
        positions = []
        duplicate_positions = []
        for particle in particles_copy:
            for index in range(len(particle[1])):
                particle[1][index] += particle[2][index]
            for index in range(len(particle[0])):
                particle[0][index] += particle[1][index]
            if particle[0] in positions:
                if particle[0] not in duplicate_positions:
                    duplicate_positions.append(particle[0])
            else:
                positions.append(particle[0])
        particles_copy_copy = particles_copy[:]
        for particle in particles_copy_copy:
            if particle[0] in duplicate_positions:
                particles_copy.remove(particle)

    return len(particles_copy)


if __name__ == "__main__":
    data = get_particles()
    print(find_particles_remaining(data))
