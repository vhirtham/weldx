

import weldx.transformations as tf
import weldx.utility as ut


import numpy as np
from scipy.spatial.transform import Rotation as rot


def create_lcs(angles,coordinates):
    orientation = rot.from_euler("xyz", angles, degrees=True).as_matrix()
    return tf.LocalCoordinateSystem(orientation, coordinates)

def get_setup(idx):
    setup = lambda:0
    if idx == 2:
        setup.system_data_index = 17519
        setup.measurement_data_id = 18208
        setup.scan_data_scan_idx = [17507, 17513]
        setup.scan_data_tcp_idx = [17518, 17519]
        setup.origin_ref = ut.to_float_array([67.311, 1055.137, -132.694])
        setup.offset_ox_ref = ut.to_float_array([157.345, 1054.486, -132.949])
        setup.offset_oy_ref = ut.to_float_array([69.149, 1366.014, -131.962])
        setup.groove_angle_start = 40
        setup.groove_angle_end = 60
        list_coordinates_temp_in_ref = [[-9.96, 89.47, -0.489]]
        list_coordinates_temp_in_ref += [[10.92, 89.97, -0.27]]
        list_coordinates_temp_in_ref += [[-8.5, 255.6, -0.2]]
        
        setup.coordinates_temp_1_in_base = [-9.96, 89.47, -0.489]
        setup.coordinates_temp_2_in_base = [10.92, 89.97, -0.27]
        setup.coordinates_temp_3_in_base = [-8.5, 255.6, -0.2]
        
        orientation_sp_in_ref = np.matmul(tf.rotation_matrix_y(np.pi / 2),tf.rotation_matrix_z(np.pi / 2))
        coordinates_sp_in_ref = [-20, -10, -8]
    elif idx == 5:        
        setup.system_data_index = 18204
        setup.measurement_data_id = 18202
        setup.scan_data_scan_idx = [18189, 18194]
        setup.scan_data_tcp_idx = [18203, 18204]
        setup.origin_ref = ut.to_float_array([67.311, 1055.137, -132.694])
        setup.offset_ox_ref = ut.to_float_array([157.345, 1054.486, -132.949])
        setup.offset_oy_ref = ut.to_float_array([69.149, 1366.014, -131.962])
        setup.groove_angle_start = 60
        setup.groove_angle_end = 40
        
        list_coordinates_temp_in_ref = [[-8.299, 84.298, -0.019]]
        list_coordinates_temp_in_ref += [[7.307, 85.235, -0.042]]
        list_coordinates_temp_in_ref += [[-9.331, 233.894, -0.014]]
        
        setup.coordinates_temp_1_in_base = [-8.299, 84.298, -0.019]
        setup.coordinates_temp_2_in_base = [7.307, 85.235, -0.042]
        setup.coordinates_temp_3_in_base = [-9.331, 233.894, -0.014]
        
        
        orientation_sp_in_ref = np.matmul(tf.rotation_matrix_y(np.pi / 2),tf.rotation_matrix_z(np.pi / 2))
        coordinates_sp_in_ref = [-18.9, -15, -8]
        
        # correct angle - reference coordinate was not perfectly orthogonal to specimen 
        offset_x = 0.42
        offset_y = setup.offset_oy_ref[1] - setup.origin_ref[1]
        angle_corr = np.arcsin(offset_x / offset_y)
        rotation_matrix = tf.rotation_matrix_z(angle_corr)
        orientation_sp_in_ref = np.matmul(rotation_matrix, orientation_sp_in_ref)


    
    # create coordinate systems
    setup.cs_sp_in_ref = tf.LocalCoordinateSystem(orientation_sp_in_ref, coordinates_sp_in_ref)
    setup.cs_scan_in_scanner_tcp = tf.LocalCoordinateSystem([[1, 0, 0], [0, 1, 0], [0, 0, -1]], [0, 0, 260])    
    setup.cs_scanner_tcp_in_flange = create_lcs(angles=[21.9714, -0.7410, -89.7500], coordinates=[-47.949, -105.258, 479.690])
    setup.cs_torch_tcp_in_flange =  create_lcs(angles=[-22.0474, 0.5659, 90.7092], coordinates=[-49.325, -0.410, 477.208])
    setup.cs_cam_in_flange = create_lcs(angles=[82, 0, -90], coordinates=[325, 0,  427])
    
    setup.list_cs_temp_in_ref = []
    for i in range(len(list_coordinates_temp_in_ref)):
        setup.list_cs_temp_in_ref += [tf.LocalCoordinateSystem(origin=list_coordinates_temp_in_ref[i])] 

    
    return setup