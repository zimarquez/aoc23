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
    if val >= source:
        print(f"True: {val} >= {source}")
        if val - source <= max_range:
            print(f"True: {val - destination} <= {source + max_range}")
            print(f"Res = {destination} + ({val} - {source})")
            return str(destination + (val-source))
        else:
            pass
            print(f"False: {val - source} <= {source + max_range}")
    else:
        pass
        print(f"False: {val} >= {source}")
    return str(val)

def resource_check(input_values, resource):
    out = {}
    for key,val in input_values.items():
        print(f"\nStarting: {val}")
        for branch in val:
            for entry in resource.values():
                new_val = translate(int(branch),entry['source'],entry['destination'],entry['range'])
                if new_val != branch:
                    try:
                        out[key].add(new_val)
                    except:
                        out[key] = {new_val}
                    print(new_val)
            if out.get(key) == None:
                out[key] = {branch}
                print(branch)
    #print(out)
    return out

def part1(seeds, maps):
    seed_locations = seeds
    seed_locations = {}
    for seed in seeds:
        seed_locations[seed] = {seed}

    print(seed_locations)
    seed_locations = resource_check(seed_locations, maps['seed-to-soil map'])
    print(seed_locations)
    seed_locations = resource_check(seed_locations, maps['soil-to-fertilizer map'])
    print(seed_locations)
    seed_locations = resource_check(seed_locations, maps['fertilizer-to-water map'])
    print(seed_locations)
    seed_locations = resource_check(seed_locations, maps['water-to-light map'])
    print(seed_locations)
    seed_locations = resource_check(seed_locations, maps['light-to-temperature map'])
    seed_locations = resource_check(seed_locations, maps['temperature-to-humidity map'])
    seed_locations = resource_check(seed_locations, maps['humidity-to-location map'])
    print(seed_locations)

    smallest = -1
    for seed,locations in seed_locations.items():
        for location in locations:
            if smallest == -1:
                print(f"BOO")
                smallest = int(location)
            if int(location) < int(smallest):
                smallest = int(location)
                print(f"smallest: {location}")

def main():
    my_input = "5_input.txt"
    seeds, maps = parse(my_input)
    print(f"seeds: {seeds}")
    #print_dict(maps)

    part1(seeds, maps)

if __name__ == '__main__':
    main()
