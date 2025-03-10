/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {

    if (!s || s.length === 0) return "";
       
       let start = 0;
       let maxLength = 1;
       
       const expandAroundCenter = (left, right) => {
           while (left >= 0 && right < s.length && s[left] === s[right]) {
               const currentLength = right - left + 1;
               if (currentLength > maxLength) {
                   maxLength = currentLength;
                   start = left;
               }
               left--;
               right++;
           }
       };
       
       for (let i = 0; i < s.length; i++) {
           expandAroundCenter(i, i);
           expandAroundCenter(i, i + 1);
       }
       
       return s.substring(start, start + maxLength);
   
   };