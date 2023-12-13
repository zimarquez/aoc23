import os

def print_dict(my_dict):
    for key,value in my_dict.items():
        print(f"\n{key}:")
        for a,b in my_dict[key].items():
            print(f"{a}: {b}")

def parse(filepath):
    maps = {}
    seeds = []
    title = "seeds"
    resource_count = 0
    with open(filepath) as input_file:
        for line in input_file:
            if 'seeds:' in line:
                seeds = line.split(':')[1].split()
            elif ':' in line:
                new_title = line.split(':')[0]
                maps[new_title] = {}
                title = new_title
                resource_count = 0
            elif line[0].isdigit():
                entry = {}
                nums = line.split()
                entry['destination'] = int(nums[0])
                entry['source'] = int(nums[1])
                entry['range'] = int(nums[2])
                maps[title][str(resource_count)] = entry
                resource_count = resource_count + 1
    return seeds, maps

def translate(val, source, destination, max_range):
    print(f"{val=} {source=}, {destination=}, {max_range=}")
    if val >= destination:
        #print(f"True: {val} >= {destination}")
        if (val - destination) <= max_range:
            #print(f"True: {val - destination} <= {max_range}")
            return destination + (val-source)
        else:
            pass
            #print(f"False: {val - destination} <= {max_range}")
    else:
        pass
        #print(f"False: {val} <= {destination}")
    return val

def resource_check(input_values, resource):
    out = []
    for val in input_values:
        print(f"\nStarting: {val}")
        for entry in resource.values():
            out.append(translate(int(val),entry['source'],entry['destination'],entry['range']))
            #print(f"{val}: {new_val}")
    print(out)
    return out

def part1(seeds, maps):
    seed_locations = seeds
    seed_locations = {}
    for seed in seeds:
        seed_locations[seed] = seed

    seed_locations = resource_check(seed_locations, maps['seed-to-soil map'])
    seed_locations = resource_check(seed_locations, maps['soil-to-fertilizer map'])
    seed_locations = resource_check(seed_locations, maps['fertilizer-to-water map'])
    seed_locations = resource_check(seed_locations, maps['water-to-light map'])
    seed_locations = resource_check(seed_locations, maps['light-to-temperature map'])
    seed_locations = resource_check(seed_locations, maps['temperature-to-humidity map'])
    seed_locations = resource_check(seed_locations, maps['humidity-to-location map'])
def main():
    my_input = "5_test.txt"
    seeds, maps = parse(my_input)
    print(f"seeds: {seeds}")
    #print_dict(maps)

    part1(seeds, maps)

if __name__ == '__main__':
    main()
