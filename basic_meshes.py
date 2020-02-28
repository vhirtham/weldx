import numpy as np

def create_unit_cylinder_mesh(num_segments_radial, num_segments_axial):
    num_segments_radial = np.clip(num_segments_radial, 3, None)
    num_segments_axial = np.clip(num_segments_axial, 1, None)
    delta_angle = 2 * np.pi / num_segments_radial
    delta_axial = 1 / num_segments_axial

    num_points = num_segments_radial * (num_segments_axial + 1)

    points = np.ndarray((3, num_points), float)
    for i in range(num_segments_axial + 1):
        z = i * delta_axial
        for j in range(num_segments_radial):
            angle = j * delta_angle
            x = np.sin(angle)
            y = np.cos(angle)
            points[:, i * num_segments_radial + j] = [x, y, z]

    num_triangles = num_segments_radial * num_segments_axial * 2
    triangles = np.ndarray((num_triangles, 3), int)
    for i in range(num_segments_axial):
        for j in range(num_segments_radial):
            idx_triangle = (i * num_segments_radial + j) * 2

            idx_first_point_axial_0 = i * num_segments_radial
            idx_first_point_axial_1 = idx_first_point_axial_0 + num_segments_radial
            rad_idx_0 = j
            rad_idx_1 = (j + 1) % num_segments_radial

            idx_0_0 = idx_first_point_axial_0 + rad_idx_0
            idx_0_1 = idx_first_point_axial_0 + rad_idx_1
            idx_1_0 = idx_first_point_axial_1 + rad_idx_0
            idx_1_1 = idx_first_point_axial_1 + rad_idx_1

            triangles[idx_triangle] = [idx_0_0, idx_1_0, idx_1_1]
            triangles[idx_triangle + 1] = [idx_0_0, idx_1_1, idx_0_1]

    return [points, triangles]

def create_cone_mesh(num_segments_radial):
    num_segments_radial = np.clip(num_segments_radial, 3, None)
    num_points = num_segments_radial + 1
    num_triangles = num_segments_radial
    delta_angle = 2 * np.pi / num_segments_radial
    
    points = np.ndarray((3, num_points), float)
    triangles = np.ndarray((num_triangles, 3), int)
    z = 0
    
    points[:,0] = [0, 0, 1]
    for i in range(num_segments_radial):        
        angle = i * delta_angle
        x = np.sin(angle)
        y = np.cos(angle)
        points[:, i+1] = [x, y, z]
        triangles[i] = [i+1,0,(i+1) % (num_triangles)+1]
    return [points,triangles]   