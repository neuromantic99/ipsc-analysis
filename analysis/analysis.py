from pathlib import Path


import tifffile
from aicsimageio import AICSImage
from ops import get_ipsc_ops
from suite2p.run_s2p import run_s2p

HERE = Path(__file__).parent


# path = Path("/Users/jamesrowland/Documents/data/DG-TauKO/KOLF-Experiment-1074.czi")
path = Path("/Volumes/MarcBusche/Francesca/CD7/DG TauKO/Day 1/TauKO.czi")

img = AICSImage(path)  # selects the first scene found

for idx, scene in enumerate(img.scenes):
    img.set_scene(idx)
    data = img.data.squeeze().astype("float32")

    tiff_path = HERE / path.stem / img.current_scene / "data.tiff"

    tiff_path.parent.mkdir(exist_ok=True, parents=True)

    tifffile.imsave(tiff_path, data)
    save_folder = str(tiff_path.resolve().parent)

    run_s2p(
        ops={**get_ipsc_ops(), **{"save_path0": save_folder}},
        db={"data_path": [save_folder]},
    )


# plt.figure(figsize=(16, 16))
# for idx, scene in enumerate(img.scenes):
#     print("Scene: ", scene)
#     img.set_scene(scene)

#     data = img.data.squeeze()
#     frame = data[0, :, :]

#     plt.subplot(4, 4, idx + 1)
#     plt.imshow(frame)
#     if idx == 3:
#         break

# plt.show()
