package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func compare(left *TreeNode,right *TreeNode)bool{
	if left == nil && right == nil{
		return true
	}
	if left == nil || right == nil{
		return false
	}
	var lr bool = compare(left.Left,right.Right)
	var rr bool = compare(left.Right,right.Left)
	return lr && rr && left.Val==right.Val
}
func isSymmetric(root *TreeNode) bool {
	return compare(root.Left,root.Right)
}


