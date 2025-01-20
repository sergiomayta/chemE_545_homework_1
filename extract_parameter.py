unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}}

def extract_parameter(unit_name,parameter_name,value): #first we will define the function
    try: #then if the input is found we will extract the value from the dictionary this way>
        unit = unit_operations_data [unit_name]
        parameter = unit[parameter_name]
        numerical_value = parameter[value]
        return f"{unit_name}_{parameter_name}_{numerical_value}" #we return as result the formated values.. 
        #for each category from our dictionary#

    except(KeyError, IndexError): #in the case there is an error we will use except to return invalid input
        return "invalid input"