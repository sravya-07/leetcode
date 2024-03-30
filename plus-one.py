class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if digits[length-1] != 9:
            digits[length-1] += 1
        else:
            value, carry = 0, 0
            for i in range(length-1, -1, -1):
                if i == length-1:
                    value = digits[i] + 1 + carry
                else:
                    value = digits[i] + carry

                if value == 10:
                    value = 0
                    carry = 1
                else:
                    carry = 0
                    digits[i] = value
                    break
                digits[i] = value
            
            if carry == 1:
                digits.insert(0, 1) # index, value
        return digits