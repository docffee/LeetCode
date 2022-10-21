class Solution:
    def uniqueOccurrencesSlow(self, arr: List[int]) -> bool:
        # Runtime 76 ms 25.99% Memory Usage: 14.1 MB 32.38%
        # create dictionary of key-values
        dict = {}
        new_dict = {}
        for element in arr:
            if element in dict:
                dict[element] +=1
            else:
                dict[element] = 1
        print(dict)
        # sort dicitonary by keys
        while len(dict) > 0:
            low_key = min(dict, key=dict.get)
            new_dict[low_key] = dict[low_key]
            del dict[low_key]
        print(new_dict)
        # find unique dictionaries
        prev_key = 0
        for key in new_dict.keys():
            if prev_key == new_dict[key]:
                return False
            else:
                prev_key = new_dict[key]
        return True


class Solution:
    def uniqueOccurrencesFaster(self, arr: List[int]) -> bool:
        # Runtime: 40 ms 90.26% Memory Usage: 14 MB 32.38% 
        dict = {}
        lowest_key='0'
        new_dict = {lowest_key:0}
        for element in arr:
            if element in dict:
                dict[element] +=1
            else:
                dict[element] = 1
        # sort dicitonary by keys
        while len(dict) > 0:
            low_key = min(dict, key=dict.get)
            new_dict[low_key] = dict[low_key]
            if new_dict[lowest_key] == dict[low_key]:
                return False
            lowest_key = low_key
            del dict[low_key]
        del new_dict['0']           
        return True 