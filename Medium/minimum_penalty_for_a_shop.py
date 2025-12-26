class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        r_y = customers.count("Y")
        l_n = 0
        min_p_h = 0
        min_p = len(customers)

        for i in range(len(customers)):
            total_p = r_y + l_n
            if total_p < min_p:
                min_p = total_p
                min_p_h = i
        
            if customers[i] == "Y":
                r_y -= 1
            elif customers[i] == "N":
                l_n += 1
        
        if min_p > customers.count("N"):
            min_p_h = len(customers)
    
        return min_p_h
        