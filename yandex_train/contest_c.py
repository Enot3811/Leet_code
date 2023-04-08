n_homes = int(input())
towns_rooms = {}
schedules = {}
answers = []

for _ in range(n_homes):
    town_name, n_rooms = input().split()
    n_rooms = int(n_rooms)
    if town_name not in towns_rooms:
        towns_rooms[town_name] = {}

    for _ in range(n_rooms):
        room_schedule, room_name = input().split()
        towns_rooms[town_name][room_name] = [
            True if hour == '.' else False
            for hour in room_schedule]

n_calls = int(input())
for _ in range(n_calls):
    call_towns = input().split()[1:]
    
    schedule = []
    for town in call_towns:
        if town not in schedules:
            schedules[town] = [
                any(hour) for hour in zip(*list(towns_rooms[town].values()))]
        schedule.append(schedules[town])

    for i in range(0, 24):
        if all([town_schd[i] for town_schd in schedule]):
            answer = ['Yes']
            for town in call_towns:
                for room_name, room_schedule in towns_rooms[town].items():
                    if room_schedule[i]:
                        answer.append(room_name)
                        break
            answers.append(' '.join(answer))
            break
    else:
        answers.append('No')

print(*answers, sep='\n', end='')
