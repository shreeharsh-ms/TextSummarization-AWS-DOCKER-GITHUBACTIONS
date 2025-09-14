import nbformat

filename = "Text_Summarization.ipynb"
nb = nbformat.read(filename, as_version=nbformat.NO_CONVERT)
metadata = nb.metadata

# if "widgets" in meta
#     # Add 'state' if missing
#     if "state" not in metadata["widgets"]:
#         metadata["widgets"]["state"] = {}
#     # Or remove 'widgets' entirely (uncomment next line if wanted)
#     # del metadata["widgets"]
if "kernelspec" not in metadata:
    metadata["kernelspec"] = {
        "name": "python3",
        "display_name": "Python 3",
        "language": "python"
    }

nbformat.write(nb, filename)
