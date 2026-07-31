import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import runpy
import traceback

saved_files = []

_original_savefig = plt.savefig

def custom_savefig(filename, *args, **kwargs):
    saved_files.append(filename)
    return _original_savefig(filename, *args, **kwargs)

plt.savefig = custom_savefig

try:
    runpy.run_path("solution.py", run_name="__main__")

    if not saved_files:
        for num in plt.get_fignums():
            fig = plt.figure(num)
            fig.savefig(
                f"figure_{num}.png",
                dpi=300,
                bbox_inches="tight",
            )

    plt.close("all")

except Exception:
    traceback.print_exc()