# Lesson 4 - Recursion and Dynamic Programming

# https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-4-recursion-and-dynamic-programming 

T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]

l = []

from jovian.pythondsa import evaluate_test_cases

def lcs_recurssive(seq1 , seq2 , idx1 = 0, idx2 = 0 , depth = 0):
    # print("  "*depth,seq1[idx1:] , seq2[idx2:])
    count = 0
    if idx1 == len(seq1) or idx2 == len(seq2):
        return count
    
    elif seq1[idx1] == seq2[idx2]:
        l.append(seq1[idx1])
        count = (1 + lcs_recurssive(seq1 , seq2 , idx1+1 , idx2 + 1 , depth+1))
    
    else:
        count = max(lcs_recurssive(seq1 , seq2 , idx1 + 1 , idx2,depth+1) , lcs_recurssive(seq1 , seq2 , idx1 , idx2+1,depth+1))

    return count


def lcs_memoised(seq1 , seq2):
    memo = {}
    l = [] 
    def recurs(idx1 , idx2):
        key = (idx1 , idx2)
        if key in memo:
            return memo[key]
                
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0

        elif seq1[idx1] == seq2[idx2]:
            l.append(seq1[idx1])
            memo[key] = 1 + recurs(idx1 + 1 , idx2 + 1)

        else:
            memo[key] = max(recurs(idx1+1 , idx2) , recurs(idx1 , idx2 + 1))

        return memo[key]

    return recurs(0,0) , l

def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]

evaluate_test_cases(lcq_dp , lcq_tests)


# question

test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}
tests = [test0, test1, test2, test3, test4, test5]

def knapsack(capacity , weights , profits , idx = 0):
    if idx == len(weights):
        return 0
    
    elif weights[idx] <= capacity:
        return max(profits[idx] + knapsack(capacity - weights[idx] , weights , profits , idx + 1) , knapsack(capacity , weights , profits , idx+1)) 

    else:
        return knapsack(capacity , weights , profits , idx + 1)


def knapsack_dp(capacity , profits , weights):
    result = [[0 for _ in range(capacity + 1)] for _ in range(len(weights))]

    for idx in range(len(weights)):
        for c in range(capacity + 1):
            if idx == 0:
                result[idx][c]  = 0 if weights[idx] > c else profits[idx]

            elif weights[idx] > c :
                result[idx][c] = result[idx-1][c]
            else:
                result[idx][c] = max(result[idx-1][c] , profits[idx] + result[idx-1][c-weights[idx]])

    return result[-1][-1]

evaluate_test_cases(knapsack_dp , tests)
