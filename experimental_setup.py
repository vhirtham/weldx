import weldx.transformations as tf
import weldx.utility as ut

import numpy as np

def get_setup(idx):
    setup = lambda:0
    if idx == 2:
        setup.system_data_index = 17519
        setup.measurement_data_id = 18208
        setup.scan_data_layer_0_scan_idx = 17507
        setup.scan_data_layer_0_tcp_idx = 17518
        setup.scan_data_layer_1_scan_idx = 17513
        setup.scan_data_layer_1_tcp_idx = 17519
        setup.origin_ref = ut.to_float_array([67.311, 1055.137, -132.694])
        setup.offset_ox_ref = ut.to_float_array([157.345, 1054.486, -132.949])
        setup.offset_oy_ref = ut.to_float_array([69.149, 1366.014, -131.962])
        setup.groove_angle_start = 40
        setup.groove_angle_end = 60
        setup.orientation_sp_in_ref = tf.rotation_matrix_z(np.pi / 2)
        setup.coordinates_sp_in_ref = [-20, -10, -8]
        setup.coordinates_temp_1_in_base = [-9.96, 89.47, -0.489]
        setup.coordinates_temp_2_in_base = [10.92, 89.97, -0.27]
        setup.coordinates_temp_3_in_base = [-8.5, 255.6, -0.2]
    elif idx == 5:        
        setup.system_data_index = 18204
        setup.measurement_data_id = 18202
        setup.scan_data_layer_0_scan_idx = 18189
        setup.scan_data_layer_0_tcp_idx = 18203
        setup.scan_data_layer_1_scan_idx = 18194
        setup.scan_data_layer_1_tcp_idx = 18204
        setup.origin_ref = ut.to_float_array([67.311, 1055.137, -132.694])
        setup.offset_ox_ref = ut.to_float_array([157.345, 1054.486, -132.949])
        setup.offset_oy_ref = ut.to_float_array([69.149, 1366.014, -131.962])
        setup.groove_angle_start = 60
        setup.groove_angle_end = 40
        setup.orientation_sp_in_ref = tf.rotation_matrix_z(np.pi / 2)
        setup.coordinates_sp_in_ref = [-18.9, -10, -8]
        setup.coordinates_temp_1_in_base = [-8.299, 84.298, -0.019]
        setup.coordinates_temp_2_in_base = [7.307, 85.235, -0.042]
        setup.coordinates_temp_3_in_base = [-9.331, 233.894, -0.014]
        
        # correct angle - reference coordinate was not perfectly orthogonal to specimen 
        offset_x = 0.42
        offset_y = setup.offset_oy_ref[1] - setup.origin_ref[1]
        angle_corr = np.arcsin(offset_x / offset_y)
        rotation_matrix = tf.rotation_matrix_z(angle_corr)
        setup.orientation_sp_in_ref = np.matmul(rotation_matrix, setup.orientation_sp_in_ref)

    setup.coordinates_cam_in_flange = [325, 0,  427]
    setup.angles_cam_in_flange = [82, 0, -90]
    return setup