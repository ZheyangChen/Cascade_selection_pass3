import numpy
from icecube import dataclasses
def change_names(frame, version):
    old_name_list = ['OfflineCscd_24__Bayesian16',
                     'OfflineCscd_24__Bayesian16FitParams',
                     'OfflineCscd_24__CascadeContainmentTagging',
                     'OfflineCscd_24__CascadeFillRatio',
                     'OfflineCscd_24__CascadeLast',
                     'OfflineCscd_24__CascadeLastParams',
                     'OfflineCscd_24__CascadeLineFit',
                     'OfflineCscd_24__CascadeLineFitParams',
                     'OfflineCscd_24__CascadeLlhVertexFit',
                     'OfflineCscd_24__CascadeLlhVertexFitParams',
                     'OfflineCscd_24__CascadeLlhVertexFit_IC',
                     'OfflineCscd_24__CascadeLlhVertexFit_ICParams',
                     'OfflineCscd_24__CascadeLlhVertexFit_IC_CLastSeed',
                     'OfflineCscd_24__CascadeLlhVertexFit_IC_CLastSeedParams',
                     'OfflineCscd_24__CascadeRecos_CascadeLinefit_rusage',
                     'OfflineCscd_24__Cscd_Cont_Tag',
                     'OfflineCscd_24__Cscd_Topo1stPulse_HLC0',
                     'OfflineCscd_24__Cscd_Topo1stPulse_HLCSplitCount',
                     'OfflineCscd_24__Cscd_Topo_HLC0',
                     'OfflineCscd_24__Cscd_Topo_HLCFirstPulses',
                     'OfflineCscd_24__Cscd_Topo_HLCSplitCount',
                     'OfflineCscd_24__LineFit',
                     'OfflineCscd_24__LineFitParams',
                     'OfflineCscd_24__MonopodAmpFit',
                     'OfflineCscd_24__MonopodAmpFitFitParams',
                     'OfflineCscd_24__MonopodFit4_AmptFit',
                     'OfflineCscd_24__MonopodFit4_AmptFitFitParams',
                     'OfflineCscd_24__NCh_OfflinePulses',
                     'OfflineCscd_24__NCh_OfflinePulsesHLC',
                     'OfflineCscd_24__NString_OfflinePulses',
                     'OfflineCscd_24__NString_OfflinePulsesHLC',
                     'OfflineCscd_24__SPEFit16',
                     'OfflineCscd_24__SPEFit16FitParams',
                     'OfflineCscd_24__SplitRTCleanedInIcePulses_IC_SinglesCleanedKeys',
                     'OfflineCscd_24__TimeSplitPulses_0',
                     'OfflineCscd_24__TimeSplitPulses_1']
    new_name_list = ['CscdL3_Bayesian16','CscdL3_Bayesian16FitParams','CascadeContainmentTagging','CascadeFillRatio','CascadeLast','CascadeLastParams','CascadeLineFit','CascadeLineFitParams','CascadeLlhVertexFit_L2','CascadeLlhVertexFit_L2Params','CascadeLlhVertexFit_IC','CascadeLlhVertexFit_ICParams','CascadeLlhVertexFit_IC_CLastSeed','CascadeLlhVertexFit_IC_CLastSeedParams','CascadeRecos_CascadeLinefit_rusage','Cscd_Cont_Tag','Cscd_Topo1stPulse_HLC0','Cscd_Topo1stPulse_HLCSplitCount','Cscd_Topo_HLC0','Cscd_Topo_HLCFirstPulses','Cscd_Topo_HLCSplitCount','LineFit','LineFitParams','MonopodAmpFit','MonopodAmpFitFitParams','L3_MonopodFit4_AmptFit','L3_MonopodFit4_AmptFitFitParams','NCh_OfflinePulses','NCh_OfflinePulsesHLC','NString_OfflinePulses','NString_OfflinePulsesHLC','CscdL3_SPEFit16','CscdL3_SPEFit16FitParams','SplitRTCleanedInIcePulses','TimeSplitPulses_0','TimeSplitPulses_1']
    for i in range(len(old_name_list)):
        if frame.Has(old_name_list[i]):
            print('old name is ',old_name_list[i])
            print('new name is ',new_name_list[i])
            obj = frame[old_name_list[i]]
            frame[new_name_list[i]] = obj
        else:
            print('no ',old_name_list[i])
    return True