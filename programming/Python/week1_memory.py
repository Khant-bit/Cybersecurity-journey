failed_logins = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.10",
    "192.168.1.30",
    "192.168.1.10",
    "192.168.1.20"
]

counts = {}

for ip in failed_logins:
    if ip in counts:
        counts[ip] += 1
    else:
        counts[ip] = 1

print(counts)

most_frequent = max(counts, key=counts.get)

print("Most frequent:", most_frequent)
print("Attempts:", counts[most_frequent])