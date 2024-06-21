#!/usr/bin/env python
# coding: utf-8

# # Savings (4/4)

# In[10]:


import math
def savings(gross_pay, tax_rate, expenses):
    gross_pay = int(gross_pay)
    tax_rate = float(tax_rate)
    expenses = int(expenses)
    result = math.floor(gross_pay - (gross_pay * tax_rate) - expenses)
    return result


# # Material Waste (4/4)

# In[12]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material = int(total_material)
    material_units = str(material_units)
    num_jobs = int(num_jobs)
    job_consumption = int(job_consumption)
    
    result = total_material - (num_jobs * job_consumption)
    return str(result)+material_units


# # Interest (4/4)

# In[14]:


import math
def interest(principal, rate, periods):
    principal = int(principal)
    rate = float(rate)
    periods = int(periods)
    principal = principal + principal *(periods*rate)
    principal = math.floor(principal)
    return principal


# In[ ]:




