#Augustine
# Assignment Matatu Trips

CAPACITY = 14

fares = [
    ("CBD-Rongai", 120),
    ("CBD-Kitengela", 150),
    ("CBD-Thika", 130),
    ]

trips = [
    ("T01", "CBD-Rongai", 14),
    ("T02", "CBD-Kitengela", 18),
    ("T03", "CBD-Rongai", 11),
    ("T04", "CBD-Thika", 14),
    ("T05", "CBD-Kitengela", 9),
    ("T06", "CBD-Thika", 16),
    ("T07", "CBD-Rongai", 14),
    ("T08", "CBD-Kitengela", 17),
    ("T09", "CBD-Thika", 8),
    ("T10", "CBD-Rongai", 12),
    ]

def fare_for(route, fares):
    for r, f in fares:
        if r == route:
            return f
    return 0

def trip_income(trip, fares):
    trip_num, route, passengers = trip
    fare = fare_for(route, fares)
    return passengers * fare

def unique_routes(trips):
    result = []
    for t, r, p in trips:
        if r not in result:
            result.append(r)
    return result

def route_summary(trips, route, fares):
    route_trips = [t for t in trips if t[1] == route]
    num_trips = len(route_trips)
    passengers = sum([t[2] for t in route_trips])
    income = sum([trip_income(t, fares) for t in route_trips])
    avg = round(passengers / num_trips, 1) if num_trips > 0 else 0
    return (route, num_trips, passengers, income, avg)

def busiest_trips(trips, n):
    trip_list = [(p, t, r) for t, r, p in trips]
    trip_list.sort(reverse=True)
    return trip_list[:n]

print(len(trips), "trips. First", trips[0], ", last", trips[-1])

total_passengers = sum([t[2] for t in trips])
total_income = sum([trip_income(t, fares) for t in trips])
print(total_passengers, "passengers, income", total_income)

for r in unique_routes(trips):
    print(route_summary(trips, r, fares))

print("Busiest:")
for b in busiest_trips(trips, 3):
    print(b)

over_capacity = [t[0] for t in trips if t[2] > CAPACITY]
print("Over capacity:", over_capacity, len(over_capacity), "trips")

under_10 = [t[0] for t in trips if t[2] < 10]
print("Under 10 passengers:", under_10)

highest_route = ""
highest_income = 0

for r in unique_routes(trips):
    summary = route_summary(trips, r, fares)
    income = summary[3]
    if income > highest_income:
        highest_income = income
        highest_route = r
print("Highest income:", highest_route, "with", highest_income)