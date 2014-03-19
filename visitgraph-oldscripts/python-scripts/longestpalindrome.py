
# This is longest "subsequent" palindrome NOT substring. Substring can be done in O(n) using a suffix tree. The runtime of this is : 0(n^2) where n is the size of th word

def calculateLCS(X, Y):
    m = len(X)
    n = len(Y)
    #Use DP to create a similarity matrix.
    C = [[0] * (n+1) for i in range(m+1)] # initialize the first row anc column as zero

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: #recurrence relations
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

def findWordReverseLook(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return findWordReverseLook(C, X, Y, i-1, j-1) + X[i-1] # add the charecter that is the same
    else:
        if C[i][j-1] > C[i-1][j]:  #other wise return the maximum of the two options in the arr C
            return findWordReverseLook(C, X, Y, i, j-1)
        else:
            return findWordReverseLook(C, X, Y, i-1, j)


X = "CBSPALINDROMEQUESTIONSADABUTUTFINDTHISSHITHTUBA"
Y = X[::-1] #Reverse the String.
C = calculateLCS(X, Y)
print C

palindrome = findWordReverseLook(C, X, Y, len(X), len(Y))
print len(palindrome)
print "Longest subsequent palindrome in "+X+" '%s'" % palindrome # Longest palindrome will be the longest common subsequence in two strings.
