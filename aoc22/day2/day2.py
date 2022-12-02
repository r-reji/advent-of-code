import details
import pandas as pd

# Read the data from the file
try:
    read_strat = pd.read_csv(details.path, sep=' ', header=None, names = ['elf_hand', 'your_hand'], chunksize = 1000)
    df_strat = pd.DataFrame()
    df_strat = pd.concat(read_strat, ignore_index=True)
except:
    raise FileNotFoundError('File not found')

# A, X : ROCK 1
# B, Y : PAPER 2
# C, Z : SCISSORS 3
# Win = 6, Lose = 0, Draw = 3

# Possible round outcomes for Part 1
cases1 = {'A' : {'X' : 3+1, 'Y' : 6+2, 'Z' : 3+0}, 'B' : {'X' : 0+1, 'Y' : 3+2, 'Z' : 3+6}, 'C' : {'X' : 1+6, 'Y' : 2+0, 'Z' : 3+3}}

def calc_score1(hand1, hand2):
    return cases1[hand1][hand2]

# X : Lose
# y : Draw
# Z : Win

# Possible round outcomes for Part 2
cases2 = {'A' : {'X' : 3+0, 'Y' : 3+1, 'Z' : 6+2}, 'B' : {'X' : 0+1, 'Y' : 3+2, 'Z' : 6+3}, 'C' : {'X' : 0+2, 'Y' : 3+3, 'Z' : 6+1}}

def calc_score2(hand1, hand2):
    return cases2[hand1][hand2]

df_strat['score1'] = df_strat.apply(lambda x: calc_score1(x['elf_hand'], x['your_hand']), axis = 1)
df_strat['score2'] = df_strat.apply(lambda x: calc_score2(x['elf_hand'], x['your_hand']), axis = 1)

print(df_strat['score1'].sum())
print(df_strat['score2'].sum())