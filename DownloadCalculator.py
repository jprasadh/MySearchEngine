# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

conversion_factors = [["kb", 2. ** 10], ["kB", 2. ** 10 * 8], ["Mb", 2. ** 20], ["MB", 2. ** 20 * 8],
                      ["Gb", 2. ** 30], ["GB", 2. ** 30 * 8], ["Tb", 2. ** 40], ["TB", 2. ** 40 * 8]]


def convert_seconds(time):
    precision = 10
    hours = int(time / 3600)
    time -= hours * 3600
    minutes = int(time / 60)
    time -= minutes * 60
    seconds = round(time, precision)
    hr_string = "hours"
    min_string = "minutes"
    sec_string = "seconds"
    if hours == 1:
        hr_string = "hour"
    if minutes == 1:
        min_string = "minute"
    if seconds == 1:
        sec_string = "second"
    return str(hours) + " " + hr_string + ", " + str(minutes) + " " + min_string + ", " + str(seconds) + " " + sec_string


def download_time(filesize, file_units, bandwidth, bandwidth_units):
    for entry in conversion_factors:
        if entry[0] == file_units:
            filesize_bits = filesize * entry[1]
            break
    for entry in conversion_factors:
        if entry[0] == bandwidth_units:
            bandwidth_bits = bandwidth * entry[1]
            break
    time = filesize_bits / bandwidth_bits
    return convert_seconds(time)




print(download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print(download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
