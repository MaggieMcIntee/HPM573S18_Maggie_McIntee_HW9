# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals

DELTA_T = 1       # years

PSA_ON = False      # if probabilistic sensitivity analysis is on

# the transition probability matrix of the first alternative
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # well
    [0.0,   0.0,    1.0,    0.0],   # stroke state
    [0.0,   0.25,   0.55,   0.2],   # PS
    [0.0,   0.0,    0.0,    1.00] #death
    ]

# treatment relative risk
TREATMENT_RR_PostStroke = 0.65
TREATMENT_RR_BLEEDING = 1.05



