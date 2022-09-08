import numpy as np
import matplotlib.pyplot as plt

# Arrays
breeds = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
notes = np.array([1, 2, 3, 5, 8, 13])

team1 = np.array([13, 3, 13, 8, 13, 3, 13, 5, 13, 5, 8, 3, 13])
team2 = np.array([8, 2, 13, 3, 8, 3, 8, 5, 13, 8, 5, 2, 8])
team3 = np.array([5, 1, 13, 2, 8, 2, 8, 2, 8, 5, 3, 1, 5])
team4 = np.array([8, 8, 5, 5, 13, 3, 5, 1, 5, 5, 8, 3, 13])

# Team 1 metrics
team1median = np.median(team1)
team1mean = np.mean(team1)
team1stddev = np.std(team1)
team1var = np.var(team1)

#Team 1 plots
plt.figure(figsize=(9, 4))

plt.subplot(131)
plt.scatter(breeds, team1)
plt.xlabel('Breed')
plt.ylabel('Note')
plt.yticks(notes)

plt.subplot(132)
plt.hist(team1)
plt.xlabel('Notes')
plt.ylabel('Apperances')
plt.xticks(notes)

plt.suptitle("Team 1")
plt.show()

# Team 2 metrics
team2median = np.median(team2)
team2mean = np.mean(team2)
team2stddev = np.std(team2)
team2var = np.var(team2)

# Team 3 metrics
team3median = np.median(team3)
team3mean = np.mean(team3)
team3stddev = np.std(team3)
team3var = np.var(team3)

# Team 4 metrics
team4median = np.median(team4)
team4mean = np.mean(team4)
team4stddev = np.std(team4)
team4var = np.var(team4)