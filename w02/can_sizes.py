def compute_volume(r, h):
    return 3.14159 * (r ** 2) * h

def compute_surface_area(r, h):
    return 2 * 3.14159 * r * (r + h)

def compute_storage_efficiency(r, h):
    volume = compute_volume(r, h)
    surface_area = compute_surface_area(r, h)
    return volume / surface_area

def main():
    names = []
    radii = []
    heights = []
    costs = []

    with open('C:\\Users\\Danny\\Documents\\cse111\\w02\\csvs\\can_sizes.csv') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(",")
            names.append(parts[0])
            radii.append(float(parts[1]))
            heights.append(float(parts[2]))
            costs.append(parts[3].strip())

    for i in range(len(names)):
        efficiency = compute_storage_efficiency(radii[i], heights[i])
        print(f"Item name: {names[i]} | Storage efficiency: {efficiency:.2f} | Cost per can: {costs[i]}")

main()