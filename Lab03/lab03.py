P_S = {1: 0.4, 0: 0.6}
P_O_given_S = {(1, 1): 0.7, (1, 0): 0.1}
P_L_given_S = {(1, 1): 0.8, (1, 0): 0.3}
P_M_given_S_L = {(1, 1, 1): 0.9, (1, 1, 0): 0.5, (0, 1, 1): 0.6, (0, 1, 0): 0.2}

#prbabilitate S pentru
def prob_S(O, L, M):
  #S=1
  P_O_given_S1 = P_O_given_S[(1, O)]
  P_L_given_S1 = P_L_given_S[(1, L)]
  P_M_given_S1_L = P_M_given_S_L[(1, L, M)]
  P_S1_O_L_M = P_S[1] * P_O_given_S1 * P_L_given_S1 * P_M_given_S1_L

  #S=0
  P_O_given_S0 = P_O_given_S[(0, O)]
  P_L_given_S0 = P_L_given_S[(0, L)]
  P_M_given_S0_L = P_M_given_S_L[(0, L, M)]
  P_S0_O_L_M = P_S[0] * P_O_given_S0 * P_L_given_S0 * P_M_given_S0_L

  # P(S=1 | O, L, M)
  total_prob = P_S1_O_L_M + P_S0_O_L_M

  P_S1_given_O_L_M = P_S1_O_L_M / total_prob
  P_S0_given_O_L_M = P_S0_O_L_M / total_prob

  return P_S1_given_O_L_M, P_S0_given_O_L_M

def classify_email(O, L, M):
    P_S1_given_O_L_M, P_S0_given_O_L_M = prob_S(O, L, M)
    if P_S1_given_O_L_M > P_S0_given_O_L_M:
        return "Spam", P_S1_given_O_L_M
    else:
        return "Non-Spam", P_S0_given_O_L_M

#exemplu
O = 1
L = 1
M = 1

result, probability = classify_email(O, L, M)
print(f"Emailul este clasificat ca: {result} cu probabilitatea {probability:.4f}")