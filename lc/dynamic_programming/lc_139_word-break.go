/**
139. 单词拆分
难度 中等
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
*/

/**
dp[i] 表示 s[:i] 能否成功拆分，如果能，设“上一个”可能拆分的点为 j，
s[:i] 拆分为 s[:j] 和 s[j:i]
其中 s[j:i] 为 wordDict 的单词，s[:j] 为空或者也能成功拆分
base case
dp[0] = True
最终需要的就是 dp[len(s)]的值
*/
package main

func wordBreak(s string, wordDict []string) bool {
	wordMap := make(map[string]int, len(wordDict))
	for _, word := range wordDict {
		wordMap[word] = 0
	}
	dp := make([]bool, len(s)+1)
	dp[0] = true
	i := 1
	for i <= len(s) {
		j := 0
		for j < i {
			word := s[j:i]
			if _, found := wordMap[word]; found {
				if dp[j] {
					dp[i] = true
					break
				}
			}
			j++
		}
		i++
	}
	return dp[len(s)]
}
