import numpy as np

def f_read_npzF(p_pathFile):
    with np.load(p_pathFile) as npz_file:
        npz_data = dict(npz_file.items())

    #print('Data loaded. ', 'Dict keys:', npz_data.keys())
    # Create X/y arrays
    x_feat = npz_data['features']
    y_targ = npz_data['category']
    x_data = npz_data['data']
    f_names = npz_data['filenames']
    y_targNames = npz_data['categorynames']
    
    return x_feat, y_targ, x_data, f_names, y_targNames


#Add an index column at the beginning, it can start from p_idx_start
def f_addIdxFeat(p_features, p_idx_start=0):
    return np.concatenate((np.arange(0, p_features.shape[0]).reshape(-1,1)+p_idx_start, p_features), axis=1).astype(np.float32)

#Append new line in the file "results09.csv"
def f_fileApp(p_file, p_idx, p_model, p_test_acc):
    import fileinput
    import sys

    newLine = True
    for line in fileinput.input(p_file, inplace=True): #inplace=1):
        if str(p_idx) == line[0:1]: #line.split(',')[0] :
            line = str(p_idx)+','+p_model+','+str(p_test_acc)+'\r\n'
            newLine = False
            #print("found in: "+line)
        sys.stdout.write(line)
        
    if newLine:
        fRes = open(p_file, 'a')
        fRes.write(str(p_idx)+','+p_model+','+str(p_test_acc)+'\r\n')
        fRes.close()


# function to return key for any value in a dictionnary
def f_get_key(p_dic, p_val): 
    for key, value in p_dic.items(): 
         if p_val == value: 
             return key 
  
    return "Not exist"

#
def f_saySth(p_sth):
    print(p_sth)

