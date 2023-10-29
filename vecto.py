import matplotlib.pyplot as plt
import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

vector_sum = vector1 + vector2

#tạo một hình ảnh 
fig = plt.figure()
#giúp thêm một trục vào hình ảnh với đặc tính 3D
ax = fig.add_subplot( projection='3d')

# Vẽ vector1 (điểm xuất phát)
ax.quiver(0, 0, 0, vector1[0], vector1[1], vector1[2], color='b', label='Vector 1')

# Vẽ vector2 (điểm xuất phát từ cuối của vector1)
ax.quiver(vector1[0], vector1[1], vector1[2], vector2[0], vector2[1], vector2[2], color='r', label='Vector 2')

# Vẽ vector tổng (điểm xuất phát từ gốc tọa độ)
ax.quiver(0, 0, 0, vector_sum[0], vector_sum[1], vector_sum[2], color='g', label='Vector tổng')

#Mở rộng trục
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_zlim(0,10)

# Đặt nhãn cho các trục
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')

# Hiển thị các vector trên cùng một đồ thị 3D
plt.legend()
plt.show()
