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

    # Train the data

    prog = path + 'ensemble_train.py'
    data = path + 'Cookbook/heart'
    db = path + 'test.db'
    args = ['python ',prog, '-D', db, '-d',data]
    e = subprocess.check_output(args
    , stderr = subprocess.STDOUT)
    print e

    # Predict
    prog = path + 'ensemble_predict.py'
    data = path + 'Cookbook/heart'
    db = path + 'test.db'
    args = ['python ',prog, '-D', db, '-d',data]
    e = subprocess.check_output(args
    , stderr = subprocess.STDOUT)
    print e






