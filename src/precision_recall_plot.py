import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Precision and recall based on the number of recommendations:
"""
dfs = [NMF1_all_items,NMF1_train,NMF1_test,NMF2_test,LDA_test,Random_test]
df_names = ['NMF1_all_items','NMF1_train','NMF1_test','NMF2_test','LDA_test','Random_test']


NMF1_all_items = {5: (0.67112970711297082, 2.8932975543375332),
                10: (0.36987447698744774, 3.0525196504322381),
                50: (0.10359832635983263, 3.406360788329641),
                100: (0.07623430962343096, 3.7463182443018508),
                1000: (0.046200836820083691, 5.6493656353412476)}

NMF1_train = {5: (0.54311990282838796, 2.4790496530121131),
                10: (0.29498525073746312, 2.5935514961111688),
                50: (0.093701197293076535, 2.9665360169400707),
                100: (0.067586326566024646, 3.2593841550967695),
                1000: (0.046902654867256643, 5.2377731673122083)}

NMF1_test = {5: (0.27886092402221435, 1.0965125768120489),
                10: (0.15833628736854546, 1.2129859651748385),
                50: (0.087439442278151938, 1.6890386712991603),
                100: (0.068060971286777752, 2.070028932260159),
                1000: (0.062164717003426698, 6.7034848093139017)}

NMF2_test = {5: (0.30958289022805152, 1.2589215651743866),
                10: (0.18905825357438261, 1.3609054544066399),
                50: (0.08200401748788845, 1.92532602326034),
                100: (0.073969041710977193, 2.5084072128755928),
                1000: (0.066016778920004737, 7.7164893354918327)}

LDA_test = {5: (0.23632281696797824, 0.87769726884481036),
                10: (0.1500649887746662, 0.94134966535065756),
                50: (0.074914332978849113, 1.2008915144240544),
                100: (0.066879357201937842, 1.5123044809160289),
                1000: (0.050159517901453385, 4.543244087459283)}

Random_test = {5: (0.066170388751033926, 0.012389405200393614),
                 10: (0.05317263381779512, 0.024031450829209995),
                 50: (0.059317027058962551, 0.12473397943270791),
                 100: (0.055063216353538932, 0.34259814819547318),
                 1000: (0.058773484579936197, 2.8626463979393773)}

# c = pd.DataFrame(NMF1_all_items).T
# c.columns = ['precision', 'recall']
# c['model'] = 'NMF1_all_items'

fig, ax = plt.subplots()
for df, df_name in zip(dfs,df_names):
    d = pd.DataFrame(df).T
    d['model'] = df_name
    d.columns = ['precision', 'recall','model']
    ax.plot(d.precision,d.recall)
plt.xlabel('precision')
plt.ylabel('recall')
plt.xlim(0,0.2)
ax.legend(df_names)
plt.show()
