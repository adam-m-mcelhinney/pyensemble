#-------------------------------------------------------------------------------
# Name:        PyEnsemble Cookbook, Dataset #1
# Purpose:     Test out hte PyEnsemble Pcakage
#
# Author:      amcelhinney
#
# Created:     05/07/2013
# Copyright:   (c) amcelhinney 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
SVM datasets available at:
    http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/

"""
import sys
path = 'C:/Local_Files/pyensemble/'
sys.path.append(path)
import subprocess



if __name__ == '__main__':

    prog = path + 'ensemble_train.py'
    data = path + 'Cookbook/heart'
    db = path + 'test.db'
    args = ['python ',prog, '-D', db, '-d',data]
    e = subprocess.check_output(args
    , stderr = subprocess.STDOUT)
    print e



    """
    # OLD CRAP
    #sys.argv = [ '-D ' + db, ' -d ' + data]
    sys.argv = [db, data]
    args = {'-D':db, '-d':data}
    #execfile(prog, {'-D ' + db, ' -d ' + data})
    execfile(prog, args)

    subprocess.call([prog, '-D ' + db, ' -d ' + data])

    subprocess.call(prog)
    #subprocess.Popen([prog, '-D ' + db, ' -d ' + data])
    e = subprocess.Popen(prog, shell = True)
    e = subprocess.Popen(['python ',prog, '-D ' + db, ' -d ' + data], shell = True)
    e = subprocess.Popen(['python ',prog, '-D ' + db, ' -d ' + data], std)
    e = subprocess.call(['python ',prog, '-D ' + db, ' -d ' + data], stdout= PIPE)
    e = subprocess.Popen(['python ',prog, '-D ' + db, ' -d ' + data], stdout = subprocess.PIPE)
    e = subprocess.Popen(['python ',prog, '-D ' + db, ' -d ' + data])
    result = e.communicate()
    subprocess.check_output(['python ',prog, '-D ' + db, ' -d ' + data])
    """


