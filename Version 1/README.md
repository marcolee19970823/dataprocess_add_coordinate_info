## What does this source code do?

Input files: node.csv and link.csv.
![image](https://user-images.githubusercontent.com/47074370/128634299-7d2c462f-323e-43c9-9a13-86586b876845.png)
node.csv file has three fields, namely node_id, x_coord, and y_coord.

![image](https://user-images.githubusercontent.com/47074370/128634331-bf19f19d-0a10-48bf-a6e5-5ab147a798fd.png)
link.csv file has four fields, namely link_id, from_node_id, to_node_id, and length.

Note that the link.csv does not have geometry field, the geometry field is used to describe the geometry of the link and is encoded by WKT format. Fore more infomation of WKT format, please refer to: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry

Therefore, this source code is to add geometry field into link.csv, according to the coordinate info provided by node.csv.

## How to use this source code?

Open this folder as a project, run data_process.py. The "link_after_process.csv" file will be outputted into this folder.
