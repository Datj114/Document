import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,1],[2,2],[1,1]])
print((A@B))
# tao ma tran đường chéo np.eye()

# np.linalg.pinv()tìm ma trận nghịch đảo
# np.linalg: module trong np cho phép toán đại số tuyến tính và ma trận
# pinv viết tắt pseudo inverse
# tính định thức np.linalg.det(A)

#   np.transpose(A) hoặc A.T mt chuyển vị 

#.size(A,0 or 1) in số dòng hoặc cột

#.sum, .max, .min(A,0 or 1)

# ma tran đường chéo np.diag([1,2,3])