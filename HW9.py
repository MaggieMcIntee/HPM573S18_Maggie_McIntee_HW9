import InputData as Settings
import ParameterClasses as P
import MarkovModelClasses as MarkCls
import scr.FormatFunctions as F
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import SupportMarkovModel as SupportModel

print ("Question 3")
print ("")
cohort_NoTherapy = MarkCls.Cohort(id= 0, therapy = P.Therapies.NoTherapy)
cohort_Anticoagulant = MarkCls.Cohort(id= 0, therapy = P.Therapies.Anticoagulation)

simOutput_NoTherapy = cohort_NoTherapy.simulate()
simOutput_Anticoagulant = cohort_Anticoagulant.simulate()

SupportModel.print_comparative_outcomes(simOutput_NoTherapy, 'No Therapy')

print ("")
print ("Question 4")
print ("")

print("New Trans Matrix with Bleeding")
print("0.75, 0.15, 0.0, 0.1"
"0.0, 0.0, 1.0, 0.0"
"0.0, 0.1625, 0.701, 0.1365"
"0.0, 0.0, 0.0, 1.0"

print ("")
print ("Question 5")
print ("")

SupportModel.print_comparative_outcomes(simOutput_Anticoagulant, 'Anticoagulation')

print ("")
print ("Question 6")

#Graph without the therapy
print ("")
print ("The survival curves of a patient who start in state “Well” under the first alternative:")
print ("")
# graph survival curve
PathCls.graph_sample_paths(
    sample_paths=simOutput_NoTherapy.get_survival_curve(),
    title='Survival Curve with no therapy intervention',
    x_label='Simulation time step (year)',
    y_label='Number of patients alive',
    )

#Graph with the anticoagulation therapy

PathCls.graph_sample_paths(
    sample_paths=simOutput_Anticoagulant.get_survival_curve(),
    title='Survival Curve with the anticoagulation intervention',
    x_label='Simulation time step (year)',
    y_label='Number of patients alive',
    )

print ("")
print ("Question 7")


print("")
# graph histogram for this no therapy group
Figs.graph_histogram(
    data=simOutput_NoTherapy.get_these_stroke_times(),
    title='Stroke Count if the Patient Does Not Receive  Therapy Intervention',
    x_label='Survival time (years)',
    y_label='Number of strokes (#)',
    bin_width=1
    )


print("")

# graph histogram for this yes drug group
Figs.graph_histogram(
    data=simOutput_Anticoagulant.get_these_stroke_times(),
    title='Stroke Count if the Patient Takes the Anticoagulation Therapy Intervention',
    x_label='Survival time (years)',
    y_label='Number of strokes (#)',
    bin_width=1
    )