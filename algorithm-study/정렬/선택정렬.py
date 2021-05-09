array = [7,5,9,0,3,1,6,2,4,8]    

for i in range(len(array)):
    m_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[m_index]:
            m_index = j
    array[m_index], array[i] = array[i], array[m_index]

print(array)