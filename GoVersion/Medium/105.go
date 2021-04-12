package main

type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder)==0 || len(inorder)==0{
		return nil
	}
	val:=preorder[0]
	index:=find(val,inorder)
	left:=buildTree(preorder[1:index+1],inorder[:index])
	right:=buildTree(preorder[index+1:],inorder[index+1:])
	return &TreeNode{
		Val:   val,
		Left:  left,
		Right: right,
	}
}

func find(target int, nums []int) int {
	for i:=0;i<len(nums);i+=1{
		if nums[i]==target {
			return i
		}
	}
	return -1
}