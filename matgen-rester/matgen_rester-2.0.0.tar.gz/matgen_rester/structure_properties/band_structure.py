# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:12:04 2020

@author: LENOVO
"""
class BandStructure:
  def __init__(self, entries: dict={}):
    self.__dict__.update(entries)
  
  def get_spin_state(self):
    return self.spin_state
  
  def get_high_kpoints(self):
    index = 0
    res = {}
    while index < self.high_kpoints_label:
      res[self.high_kpoints_label[index]] = self.high_kpoints_data[index]
    return res
  
  def get_band_gap(self):
    return self.band_gap[0] + '(' + self.band_gap[1] + ')'
  
  def get_energy_len(self):
    return len(self.energy_data)
  
  def get_energy_data_labels(self):
    return self.energy_data_labels
  
  def get_energy_data(self, index=-1):
    if index is -1:
      return self.energy_data
    else:
      return self.energy_data[index]
  
  def as_dict(self):
    res = {}
    res["band_gap"] = self.get_band_gap()
    res["energy_data_labels"] = self.get_energy_data_labels()
    res["energy_data"] = self.get_energy_data()
    res["high_kpoints"] = self.get_high_kpoints()
    res["spin_state"] = self.get_spin_state()
    return res
  
  def __eq__(self, other):
    return (self.band_gap, self.energy_data_labels,self.energy_data,self.spin_state,self.high_kpoints_label,self.high_kpoints_data) is (other.band_gap, other.energy_data_labels,other.energy_data,other.spin_state,other.high_kpoints_label,other.high_kpoints_data)
  
  def obj_to_string(self):
    if not isinstance(self, BandStructure):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(BandStructure.__name__) + "("
    items = self.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + ":" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(BandStructure.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"
  
  def __str__(self):
    return self.obj_to_string()
  
    
    
  