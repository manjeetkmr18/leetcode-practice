class Solution {
  String longestPalindrome(String s) {
    if (s.isEmpty) return "";
    if (s.length == 1) return s;
    
    int start = 0;
    int maxLength = 1;
    
    void expandAroundCenter(int left, int right) {
      while (left >= 0 && right < s.length && s[left] == s[right]) {
        int currentLength = right - left + 1;
        if (currentLength > maxLength) {
          maxLength = currentLength;
          start = left;
        }
        left--;
        right++;
      }
    }
    
    for (int i = 0; i < s.length; i++) {
      expandAroundCenter(i, i);
      expandAroundCenter(i, i + 1);
    }
    
    return s.substring(start, start + maxLength);
  }
}