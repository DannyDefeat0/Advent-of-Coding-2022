file = open("Day2RawData", "r")
lines = file.readlines()

#We're told for us Rock, Paper, Scissors are called X,Y,Z and are worth 1, 2, and 3 points respectively.
#We're told a loss, draw, and win are worth 0, 3, and 6 respectively.
#To find the told score, I am going to create two functions, one that determines the points based solely on the sign
#and a separate one that sums up the points for draws and wins

sign_points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}



outcomes = {
    "A X": 3,
    "B X": 0,
    "C X": 6,
    "A Y": 6,
    "B Y": 3,
    "C Y": 0,
    "A Z": 0,
    "B Z": 6,
    "C Z": 3
}

rigged_sign_points = {
    "A X": 3,
    "B X": 1,
    "C X": 2,
    "A Y": 1,
    "B Y": 2,
    "C Y": 3,
    "A Z": 2,
    "B Z": 3,
    "C Z": 1
}
#This approach runs into scaling problems. For instance if this was 20 RPS this would be much harder

rigged_outcomes = {
    "A X": 0,
    "B X": 0,
    "C X": 0,
    "A Y": 3,
    "B Y": 3,
    "C Y": 3,
    "A Z": 6,
    "B Z": 6,
    "C Z": 6
}



def points_for_signs():
    sign_score = 0
    for line in lines:
        print(rigged_sign_points[line[0:3]])
        sign_score += rigged_sign_points[line[0:3]]
        #sign_score += sign_points[line[2]]
    return sign_score
def points_for_outcomes():
    outcome_score = 0
    for line in lines:
        print(rigged_outcomes[line[0:3]])
        outcome_score += rigged_outcomes[line[0:3]]
        #outcome_score += outcomes[line[0:3]]

    return outcome_score

print(points_for_signs()+points_for_outcomes())
