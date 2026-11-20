# 📝 459. Repeated Substring Pattern (LeetCode)

🔗 [Problem Link](https://leetcode.com/problems/repeated-substring-pattern/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Language](https://img.shields.io/badge/Language-Python-blue)

### 💡 Tags
String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm

### 🚀 Performance
- **Runtime:** N/A
- **Memory:** N/A

---

### 📜 Problem Description

Given a string  `s` , check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

OriginalPython3 **Example 1:**

```
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

```

**Example 2:**

```
Input: s = "aba"
Output: false

```

**Example 3:**

```
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

```

**Constraints:**

	
- `1 <= s.length <= 104`
	
- `s`  consists of lowercase English letters.