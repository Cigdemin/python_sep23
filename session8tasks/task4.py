connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
lead_to = []
duration = []
for items in connections:
	duration.append(items[2]), lead_to.append(items[1])
lead_to_rome = lead_to.count('Rome')
average_duration = round(sum(duration)/len(duration))
# print(lead_to)
# print(duration)
# print(lead_to_rome)
# print(average_duration)
print(f"{lead_to_rome} connections lead to Rome with an average flight time of {average_duration} minutes")