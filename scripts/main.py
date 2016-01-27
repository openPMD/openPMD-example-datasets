"""
This scripts runs Warp simulations which produce the openPMD data
for this repository.

Usage
-----
Simply type in a terminal:
$ python main.py
"""
import os

def produce_data( script_name, output_folder ):
    """
    Run a Warp simulation and compress the resulting directory of data

    Parameters
    ----------
    script_name: string
        The name of the Warp script to be run

    output_folder: string
        The name of the folder that will be created by Warp,
        and which is to be compressed
    """
    # Run the simulation
    command_line = 'python %s' %script_name
    os.system( command_line )

    # Compress the file
    tar_name = '%s.tar.gz' %output_folder
    if os.path.exists( tar_name ):
        os.remove( tar_name )
    command_line = 'tar -zcvf %s %s' %(tar_name, output_folder)
    os.system( command_line )


if __name__ == '__main__':

    # Run the 2D simulation 
    produce_data( 'warp_2d_script.py', 'example-2d' )

    # Run the thetaMode simulation
    produce_data( 'warp_thetaMode_script.py', 'example-thetaMode' )
    
    # Run the 3D simulation
    produce_data( 'warp_3d_script.py', 'example-3d' )
