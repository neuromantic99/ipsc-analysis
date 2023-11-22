from pathlib import Path

HERE = Path(__file__).parent


def get_ipsc_ops():
    return {
        "fast_disk": [],  # used to store temporary binary file, defaults to save_path0
        "delete_bin": True,  # whether to delete binary file after processing
        "move_bin": False,  # if 1, and fast_disk is different than save_disk, binary file is moved to save_disk
        "nplanes": 1,  # each tiff has these many planes in sequence
        "nchannels": 1,  # each tiff has these many channels per plane
        "tau": 0.75,  # this is the main parameter for deconvolution
        "fs": 5,  # sampling rate (PER PLANE e.g. for 12 plane recordings it will be around 2.5)
        "do_registration": True,  # whether to register data (2 forces re-registration)
        "batch_size": 200,  # number of frames per batch
        "maxregshift": 0.1,  # max allowed registration shift, as a fraction of frame max(width and height)
        "reg_tif": True,  # whether to save registered tiffs
        "diameter": 30,  # use diameter for cellpose, if 0 estimate diameter
        "neucoeff": 0.7,  # neuropil coefficient
        "save_path": HERE,
    }
