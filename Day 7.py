latencies = [1 * (10**(-3)), 0.4 * (10**(-9)), 12 * (10**(-9))]
latencies.append(7 * (10**(-3)))
speed_of_light = 3 * (10**8)
i = 0
for latency in latencies:
    print(speed_of_light * latency)
print((100/(1*(10**12)*8))*(10**9))