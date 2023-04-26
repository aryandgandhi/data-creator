import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import random
import math
import datetime
from datetime import date, timedelta


def statoperation(max_val,test_df,try_list,vals_list):
     for k in range (1,max_val):
            #includes 1 and 10
            for q in (test_df['ORDER_QTY'].values.tolist()): #q is each value in the ordre_qty
                rand_val = random.randint(0,k)
                if rand_val != 1:
                    try_list.append(math.floor(q * (1 + l/100))) 
                if rand_val == 1:
                    try_list.append(math.ceil(q * (1 + l/100)))
            
            vals_list.append(abs(sum(try_list) - (sum((test_df['ORDER_QTY'].values.tolist())) * (1 + l/100))))
            try_list.clear()

def percentincrease(intIncrease):

    orig_sum = sum(test_df['ORDER_QTY'].values.tolist())


    try_list = []
    vals_list = []

    l = intIncrease
    j = 0
    k_range_middle = int(1/(abs(l) * .01))
    k_range_first = k_range_middle - 15
    print(k_range_first)
    k_range_last = k_range_middle + 15
    print(k_range_last)
    #lets say you want 50 percent increase
    if (k_range_first) < 1:
        k_range_first = 1


    if l > 0:
        for k in range (1,85):
            #includes 1 and 10
            for q in (test_df['ORDER_QTY'].values.tolist()): #q is each value in the ordre_qty
                rand_val = random.randint(0,k)
                if rand_val != 1:
                    try_list.append(math.floor(q * (1 + l/100))) 
                if rand_val == 1:
                    try_list.append(math.ceil(q * (1 + l/100)))
            
            vals_list.append(abs(sum(try_list) - (sum((test_df['ORDER_QTY'].values.tolist())) * (1 + l/100))))
            try_list.clear()
            
    elif l < 0:
        for k in range (1,85):
            for q in (test_df['ORDER_QTY'].values.tolist()):
                rand_val = random.randint(0,k)
                if rand_val == 1:
                    try_list.append(math.floor(q * (1 + l/100))) 
                if rand_val != 1:
                    try_list.append(math.ceil(q * (1 + l/100)))

            vals_list.append(abs(sum(try_list) - (sum((test_df['ORDER_QTY'].values.tolist())) * (1 + l/100))))
            try_list.clear()
        
    min_index = vals_list.index(min(vals_list))
    print(vals_list)

    k_val = min_index + 1
    print(k_val)
    print("moved on ")

    if l > 0:
        for q in (test_df['ORDER_QTY'].values.tolist()):
            rand_val = random.randint(0,k_val)
            if rand_val == 1:
                try_list.append(math.ceil(q * (1 + l/100))) 
            if rand_val != 1:
                try_list.append(math.floor(q * (1 + l/100)))

                
        while (abs(sum(try_list) - (orig_sum * (1 + l/100))) > ((orig_sum) * 0.0025)):
            
    
            try_list.clear()
            for q in (test_df['ORDER_QTY'].values.tolist()):
                rand_val = random.randint(0,k_val)
                if rand_val == 1:
                    try_list.append(math.ceil(q * (1 + l/100))) 
                if rand_val != 1:
                    try_list.append(math.floor(q * (1 + l/100)))
            print(abs(sum(try_list) - orig_sum * (1 + l/100)))
            print(orig_sum * .001)
        
        
            
        test_df['ORDER_QTY'] = try_list


    elif l < 0:
        for q in (test_df['ORDER_QTY'].values.tolist()):
            rand_val = random.randint(0,k)
            if rand_val == 1:
                try_list.append(math.floor(q * (1 + l/100))) 
            if rand_val != 1:
                try_list.append(math.ceil(q * (1 + l/100)))

                

        
        while (abs((sum(try_list) - (orig_sum * (1 + l/100)))) > ((orig_sum) * 0.0025)):
    
            try_list.clear()
            for q in (test_df['ORDER_QTY'].values.tolist()):
                rand_val = random.randint(0,k_val)
                if rand_val == 1:
                    try_list.append(math.floor(q * (1 + l/100))) 
                if rand_val != 1:
                    try_list.append(math.ceil(q * (1 + l/100)))
            print(abs(sum(try_list) - (orig_sum * (1 + l/100))))
            print(orig_sum * .001)

        test_df['ORDER_QTY'] = try_list
    
    return test_df




