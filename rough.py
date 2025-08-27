# import numpy as np
# pcd = o3d.io.read_point_cloud("./data/toothless.ply")
# pcd2 = o3d.io.read_point_cloud("./data/toothless.ply")

# rm = o3d.geometry.get_rotation_matrix_from_zyx((np.pi / 2, 0, 0))

# def doICP(x, y):

#     x0 = np.mean(x, axis=0)
#     y0 = np.mean(y, axis=0)

#     # print((y - y0).shape,(x - x0).T.shape )
    
#     # print(x0, y0)
#     # print("hi")
#     # print((x - x0).T)
#     # print(y - y0)
    
#     H = (x - x0).T @ (y - y0)
#     # print(H)
#     # print("H", H)
#     eig1, evecU = np.linalg.eig(H @ H.T)
#     eig2, evecV = np.linalg.eig(H.T @ H)
#     # print(eig1, eig2)
#     # print(eig1)
#     U, D, Vt = np.linalg.svd(H)
#     # print("hi")
#     # # print(D)
#     # print(U)
#     # print(D ** 2)
#     # # print("hi")
#     # print(evecU)
#     # print(np.roll(evecU, 1, 1))
#     # # print("hi")

#     # # print("hi")
#     # print("hi")
#     # # print(np.linalg.eig(Vt.T)[0], eig2)
#     # print("hi")

#     # print(U)

#     # print(D)
#     # print(Vt)
#     a = np.copy(evecV[:, 1])
#     evecV[:, 1] = evecV[:, 2].copy()
#     evecV[:, 2] = a
#     print(evecV)
#     print(Vt.T)
#     print(np.roll(evecU, 1, 1))
#     print(U)
#     R = evecV @ np.roll(evecU, 1, 1).T
#     r = (Vt.T @ U.T)
#     print(r)
#     # print(r)
#     # print("iiiii")
#     # print(R)
#     # print(D)
#     # R = (U @ Vt).T
#     # R = Vt @ U.T
#     T = y0 - x0 @ R.T
    
#     return R, T

# pcd2.rotate(rm, center=(0,0,0))                     # Arbitrary Transformation
# pcd2.translate((200, 300, -200))
# # print(np.asarray(pcd2.points))
# x = np.asarray(pcd.points)
# y = np.asarray(pcd.points)
# # x = np.array([[1, 0, -1],
# #             [0, -2, 2],
# #             [20,-1, 2],
# #             [1, 1, 1]])


# # x = np.random.randn(100000, 3)
# # x2 = np.random.randn(10)

# y = x @ rm.T + [200, 300, -200]
# # print(y)

# # print(x)
# # print(y)

# R, T = doICP(x, y)
# # print(R.shape)
# print(R)
# pcd.rotate(R)
# print(T)

# pcd.translate(T)