import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/airou/PycharmProjects/arcpro_rl_base_case_waypointer/src/robo_racer/src/f1tenth_teleop/install/f1tenth_teleop'
