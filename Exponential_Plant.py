"""Takahashi is growing a plant. Its height at the time of germination is 
0cm. Considering the day of germination as day 
0, its height increases by 2 i cm day i's night (0≤i).
Takahashi's height is Hcm.
Every morning, Takahashi measures his height against this plant. Find the first day such that the plant's height is strictly greater than Takahashi's height in the morning."""

takahashi_height = int(input("Enter a height : "))

plant_height = 0
day = 0

while True:
    plant_height += 2
    day += 1

    if plant_height > takahashi_height:
        print(f"The plant is taller than Takahashi on day {day}.")
        break
    elif day > 100: 
        print("Plant never taller than Takahashi.")
        break