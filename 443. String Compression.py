class Solution:
    def compress(self, chars: List[str]) -> int:
        # res: write pointer - where to write the next compressed character
        res = 0
        
        # i: start pointer - marks the beginning of current group
        i = 0
        
        # n: total length of input array
        n = len(chars)

        # j: read pointer - scans through the array
        # Goes to n+1 to handle the last group (explained below)
        for j in range(n + 1):
            # Check if current group has ended
            # Group ends when: 
            # 1. We reach the end (j == n), OR
            # 2. Current character differs from group start (chars[j] != chars[i])
            if j == n or chars[j] != chars[i]:
                # Write the character for this group
                chars[res] = chars[i]
                res += 1  # Move write pointer forward
                
                # Calculate how many characters were in this group
                group_length = j - i
                
                # If group has more than 1 character, write the count
                if group_length > 1:
                    # Convert number to string to handle multi-digit counts
                    # e.g., 12 becomes '1' and '2'
                    for digit in str(group_length):
                        chars[res] = digit
                        res += 1  # Move write pointer for each digit
                
                # Move start pointer to beginning of next group
                i = j
        
        # Return the length of compressed array
        return res
