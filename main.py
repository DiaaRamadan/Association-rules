import pandas as pd

data = pd.read_excel('CoffeeShopTransactions.xlsx', 'Sheet1')
item1 = data['Item 1'].tolist()
item2 = data['Item 2'].tolist()
item3 = data['Item 3'].tolist()
allitems = []
allitems.extend(item1 + item2 + item3)
support = input("Enter Support: ")
confidence = input("Enter Confidence: ")


def first_item_set():
    count = 0
    freq_item = []
    uniqe_item = []
    while count < len(allitems):
        count2 = 0
        sum = 0
        item = allitems[count]
        if item not in uniqe_item:
            uniqe_item.append(item)
            while count2 < len(allitems):
                compare_item = allitems[count2]
                if compare_item == item:
                    sum += 1
                count2 += 1
            if support <= sum:
                freq_item.append(item)
        count += 1
    return freq_item


def Second_frequent_items():
    first = first_item_set()
    freq_list =[]
    count = 0
    while count < len(first):
        count1 = count+1
        while count1 < len(first):
            if first[count1] != first[count]:
                newstr = first[count] + ";" + first[count1]
                freq_list.append(newstr)
            count1 += 1
        count += 1

    return freq_list


def merge_data_freq():
    second = Second_frequent_items()
    count = 0
    count2 = 0
    count3 = 0
    second_freq_list = []

    while count < len(item1):
        newstr = item1[count] + ";" + item2[count]
        if newstr in second:
            second_freq_list.append(newstr)
        count += 1

    while count2 < len(item1):
        newstr2 = item2[count2] + ";" + item3[count2]
        if newstr in second:
            second_freq_list.append(newstr2)
        count2 += 1

    while count3 < len(item1):
        newstr3 = item1[count3] + ";" + item3[count3]
        if newstr in second:
            second_freq_list.append(newstr3)
        count3 += 1
    return second_freq_list


def get_second():
    merge_data = merge_data_freq()
    second = Second_frequent_items()
    second_items = []
    count1 = 0
    while count1 < len(second):
        count2 = 0
        sum = 0
        while count2 < len(merge_data):
            if merge_data[count2] == second[count1]:
                sum += 1
            if support <= sum:
                if second[count1] not in second_items:
                    second_items.append(second[count1])
            count2 += 1
        count1 += 1
    return second_items


def third_frq_item():
    third = get_second()
    count = 0
    list = []
    third_list = []
    fthird_list = []
    while count < len(third):
        item = third[count]
        str = item.split(';')
        list.append(str)
        count += 1
    count2 = 0
    while count2 < len(list):
        count3 = count2 + 1
        while count3 < len(list):
            for item in list[count3]:
                ilist = []
                if item not in list[count2]:
                    ilist.append(item)
                    for item2 in list[count2]:
                        ilist.append(item2)
                    third_list.append(ilist)
            count3 += 1
        count2 += 1
    for list in third_list:
        str = ";".join(list)
        fthird_list.append(str)
    return fthird_list

# def get_third_frquent():
#     count = 0
#     third = third_frq_item()
#     third_freq_list = []
#     result = []
#     sumCount = []
#     while count < len(item1):
#         newstr = item1[count] + ";" + item2[count] + ";" + item3[count]
#         third_freq_list.append(newstr)
#         count += 1
#     for item in third:
#         sum = 0
#         for compareitem in third_freq_list:
#             if item == compareitem:
#                 sum += 1
#         if support <= sum:
#             str_item = item + ":" + str(sum)
#             if str_item not in result:
#                 result.append(str_item)
#     return result


def get_third_frquent():
    count = 0
    third = third_frq_item()
    third_freq_list = []
    result = []

    while count < len(item1):
        newstr = item1[count] + ";" + item2[count] + ";" + item3[count]
        third_freq_list.append(newstr)
        count += 1
    for item in third:
        sum = 0
        for compareitem in third_freq_list:
            if item == compareitem:
                sum += 1
        if support <= sum:
            str_item = item + ":" + str(sum)
            if str_item not in result:
                result.append(str_item)
    return result

# def get_association_conf():
#     freq_item = get_third_frquent()
#     secend_merge = merge_data_freq()
#     count1 = 0
#     count2 = 0
#     split_list = []
#     for item in freq_item:
#         split_list.append(item.split(":", 1))
#     for sitem in split_list:
#         sum1 = 0
#         sum2 = 0
#         all_sum = 0
#         count2 = count1+1
#         if count2 <len(sitem):
#             all_sum = int(sitem[count2])
#         while count1 < len(sitem):
#             for Aitem in allitems:
#                 if sitem[count1] == Aitem:
#                     sum1 += 1
#         print sum1
#         print all_sum
#         count1 += 1
#
#
#
# get_association_conf()

print "first frequent itemset"
print "---------------------------------------"

for item in first_item_set():
    print item

print "Second frequent itemset"
print "---------------------------------------"
for item in get_second():
    print item


print "Third frequent itemset"
print "---------------------------------------"

for item in get_third_frquent():
    print item
