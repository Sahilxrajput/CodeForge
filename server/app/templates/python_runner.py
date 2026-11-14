import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import runpy
import traceback
import os

saved_files = []

_original_savefig = plt.savefig


def custom_savefig(filename, *args, **kwargs):
    filename = os.path.basename(str(filename))

    output_path = os.path.join("/code", filename)

    saved_files.append(output_path)

    return _original_savefig(output_path, *args, **kwargs)


plt.savefig = custom_savefig


try:
    runpy.run_path("solution.py", run_name="__main__")

    if not saved_files:
        for num in plt.get_fignums():

            filename = f"figure_{num}.png"
            output_path = os.path.join("/code", filename)

            fig = plt.figure(num)

            fig.savefig(
                output_path,
                dpi=150,
                bbox_inches="tight",
            )

            saved_files.append(output_path)

    plt.close("all")

except Exception:
    traceback.print_exc()
