# # # strings task 1
# a_string = 'tcfghilmnoprstuy'
# my_list = sorted(set(a_string))
# print(my_list)
# #
# # # strings task 2
# string = "segev"
# print(string[::-1])
# #
# # # strings task 3
# string_list = 'this is the sentence of segev'
# n = 4
# print([string_list[i:i+n] for i in range(0, len(string_list), n)])
# #
# # # state task 1
# def capital_of_Idaho():
#     return STATES_CAPITALS['Idaho']
# print(capital_of_Idaho())
# #
# # # state task 2
# def all_states():
#     return STATES_CAPITALS.keys()
# print(all_states())
# #
# # # state task 3
# def all_capitals():
#     return STATES_CAPITALS.values()
# print(all_capitals())
# #
# # # state task 4
# def states_capitals_string():
#     single_string = ""
#     for key,value in STATES_CAPITALS.items():
#         single_string += key + " -> " + value + ", "
#     return single_string[:-2]
# print(states_capitals_string())
# #
# # # state task 5
# def test_sorted(single_string):
#     dict1 = {}
#     for state_pair in single_string.split(", "):
#         members = state_pair.split(" -> ")
#         dict1.update({members[0]: members[1]})
#     states = list(dict1.keys())
#     for index in range(len(states) - 1):
#         if states[index] < states[index + 1]:
#             continue
#         else:
#             print("string is not sorted alfabeteclly")
#             return
#     print("string is sorted")
#
#
# test_sorted(states_capitals_string())
#
# # state task 7
# STATES_CAPITALS = {
#     'Alabama' : 'Montgomery',
#     'Alaska' : 'Juneau',
#     'Arizona' : 'Phoenix',
#     'Arkansas': 'Little Rock',
#     'California' : 'Sacramento',
#     'Colorado' : 'Denver',
#     'Connecticut' : 'Hartford',
#     'Delaware' : 'Dover',
#     'Florida' : 'Tallahassee',
#     'Georgia' : 'Atlanta',
#     'Hawaii' : 'Honolulu',
#     'Idaho' : 'Boise',
#     'Illinois' : 'Springfield',
#     'Indiana' : 'Indianapolis',
#     'Iowa' : 'Des Moines',
#     'Kansas' : 'Topeka',
#     'Kentucky' : 'Frankfort',
#     'Louisiana' : 'Baton Rouge',
#     'Maine' : 'Augusta',
#     'Maryland' : 'Annapolis',
#     'Massachusetts' : 'Boston',
#     'Michigan' : 'Lansing',
#     'Minnesota' : 'Saint Paul',
#     'Mississippi' : 'Jackson',
#     'Missouri' : 'Jefferson City',
#     'Montana' : 'Helena',
#     'Nebraska' : 'Lincoln',
#     'Nevada' : 'Carson City',
#     'New Hampshire' : 'Concord',
#     'New Jersey' : 'Trenton',
#     'New Mexico' : 'Santa Fe',
#     'New York' : 'Albany',
#     'North Carolina' : 'Raleigh',
#     'North Dakota' : 'Bismarck',
#     'Ohio' : 'Columbus',
#     'Oklahoma' : 'Oklahoma City',
#     'Oregon' : 'Salem',
#     'Pennsylvania' : 'Harrisburg',
#     'Rhode Island' : 'Providence',
#     'South Carolina' : 'Columbia',
#     'South Dakota' : 'Pierre',
#     'Tennessee' : 'Nashville',
#     'Texas' : 'Austin',
#     'Utah' : 'Salt Lake City',
#     'Vermont' : 'Montpelier',
#     'Virginia' : 'Richmond',
#     'Washington' : 'Olympia',
#     'West Virginia' : 'Charleston',
#     'Wisconsin' : 'Madison',
#     'Wyoming' : 'Cheyenne',
# }
# #
# # capital = input("please enter capital: ")
#
# # # for capital in STATES_CAPITALS.items():
# # while True:
# #     capital == STATES_CAPITALS.values()
# #     print(f"The capital of {STATES_CAPITALS[value]} is {STATES_CAPITALS.keys()}")
#
# key = 2
# my_dict = {"a": 1, "b": 2, "c": 3}
# x = my_dict.get("", key)
# print(my_dict.)
#
# #
# # STATES_CAPITALS.values() //Jerusalem
# # STATES_CAPITALS.keys() //Israel
# #
# # def capital_of_Idaho():
# #     return STATES_CAPITALS['Idaho']
# #
# #
# # print(capital_of_Idaho())
#


def no_duplicates(a_string):
    my_list = sorted(set(a_string))
    return my_list

print(no_duplicates("segevsegev"))