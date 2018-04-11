import InputData as Settings
import scr.FormatFunctions as F
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import scr.EconEvalClasses as Econ


def print_outcomes(simOutput, therapy_name):
    """ prints the outcomes of a simulated cohort
    :param simOutput: output of a simulated cohort
    :param therapy_name: the name of the selected therapy
    """
    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # mean and confidence interval text of time to post-stroke
    time_to_stroke_death_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_time_to_post_stroke().get_mean(),
        interval=simOutput.get_sumStat_time_to_post_stroke().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # print outcomes
    print(therapy_name)
    print("  Estimate of mean survival time and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          survival_mean_CI_text)
    print("  Estimate of mean time to death and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          time_to_stroke_death_CI_text)

def draw_survival_curves_and_histograms(simOutputs_no_therapy, simOutputs_anticoagulation):
    """ draws the survival curves and the histograms of time until stroke deaths
    :param simOutputs_no_therapy: output of a cohort simulated under no therapy
    :param simOutputs_anticoagulation: output of a cohort simulated under anticoagulation therapy
    """

    # get survival curves of both treatments
    survival_curves = [
        simOutputs_no_therapy.get_survival_curve(),
        simOutputs_anticoagulation.get_survival_curve()
    ]

    # graph survival curve
    PathCls.graph_sample_paths(
        sample_paths=survival_curves,
        title='Survival curve',
        x_label='Simulation time step (year)',
        y_label='Number of alive patients',
        legends=['No Therapy', 'Anticoagulation Therapy']
    )

    # histograms of survival times
    set_of_survival_times = [
        simOutputs_no_therapy.get_survival_times(),
        simOutputs_anticoagulation.get_survival_times()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_survival_times,
        title='Histogram of patient survival time',
        x_label='Survival time (year)',
        y_label='Counts',
        bin_width=1,
        legend=['No Therapy', 'Anticoagulation Therapy'],
        transparency=0.6
    )


def print_comparative_outcomes(simOutputs_no_therapy, simOutputs_anticoagulation):
    """ prints average increase in survival time, discounted cost, and discounted utility
    under combination therapy compared to no therapy
    :param simOutputs_no_therapy: output of a cohort simulated under no therapy
    :param simOutputs_anticoagulation: output of a cohort simulated under anticoagulation therapy
    """

    # increase in survival time under anticoagulation therapy with respect to no therapy
    if Settings.PSA_ON:
        increase_survival_time = Stat.DifferenceStatPaired(
            name='Increase in survival time',
            x=simOutputs_anticoagulation.get_survival_times(),
            y_ref=simOutputs_no_therapy.get_survival_times())
    else:
        increase_survival_time = Stat.DifferenceStatIndp(
            name='Increase in survival time',
            x=simOutputs_anticoagulation.get_survival_times(),
            y_ref=simOutputs_no_therapy.get_survival_times())

    # estimate and CI
    estimate_CI = F.format_estimate_interval(
        estimate=increase_survival_time.get_mean(),
        interval=increase_survival_time.get_t_CI(alpha=Settings.ALPHA),
        deci=2)
    print("Average increase in survival time "
          "and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          estimate_CI)