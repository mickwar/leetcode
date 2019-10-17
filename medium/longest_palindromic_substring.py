# https://leetcode.com/problems/longest-palindromic-substring/
# At time of submission
#   performed 90% faster
#   used less than 22% memory
# than other solutions
#
# Check out Manacher's algorithm for an optimized solution

class Solution:
    def longestPalindrome(self, string: str) -> str:
        current_left = 0
        current_right = len(string)
        current_length = 0
        best_left = 0
        best_right = len(string)
        best_length = -1
        #for i in range(int(len(string) // 2 + 0.5)):
        for i in range(len(string)):
            # If max lengthed palindrome starting at index i is smaller
            # than best_length, then break out of the for loop
            if len(string) - i < best_length:
                break
            
            # Start with the largest substring beginning with index i
            s = string[i]
            current_left  = i
            current_right = len(string)
            current_length = current_right - current_left
            
            # Keep looping until a palindrome is found
            while string[current_left:(current_right+1)] != string[current_left:(current_right+1)][::-1]:
                # Move `current_right` to the left until it finds string[i]
                current_right = string.rfind(s, current_left, current_right)
                current_length = current_right - current_left
                
                # Matching character from the right is not found
                # i.e. there is no palindrome
                if current_right == -1:
                    break
                    
                # Don't need to continue searching if the substring length is smaller
                if current_length <= best_length:
                    break
                       
            # Update the largest found palindrome
            if current_length > best_length:
                best_length = current_length
                best_left = current_left
                best_right = current_right
            
        return string[best_left:(best_right+1)]
    
