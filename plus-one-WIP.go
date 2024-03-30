func plusOne(digits []int) []int {
	lenght := len(digits)
	if digits[lenght-1] != 9 {
		digits[lenght-1] += 1
	} else {
		var carry, value int = 0, 0
		for i := lenght - 1; i >= 0; i-- {
            value = digits[i] + 1 + carry
            if value == 10 {
                value = 0
                carry = 1
            } else {
                carry = 0
            }
            digits[i] = value
		}
        if carry == 1 {
            
        }
	}
    return digits
}