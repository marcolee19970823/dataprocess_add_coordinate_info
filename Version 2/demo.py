import pandas as pd
import time

node_df = pd.read_csv("node.csv")
link_df = pd.read_csv("link.csv")

x_coord_dict = node_df[['node_id', 'x_coord']].to_dict()['x_coord']
y_coord_dict = node_df[['node_id', 'y_coord']].to_dict()['y_coord']


# LINESTRING (-109.788403 34.301335, -109.7883991 34.3014166)
def concat_fun(from_node_id, to_node_id):
    return "LINESTRING (" + str(x_coord_dict[from_node_id]) + " " + str(y_coord_dict[from_node_id]) \
           + ", " + str(x_coord_dict[to_node_id]) + " " + str(y_coord_dict[to_node_id]) + ")"


# way 1 for loop
st = time.time()
for i in link_df.index:
    from_node_id = link_df.loc[i, "from_node_id"]
    to_node_id = link_df.loc[i, "to_node_id"]
    link_df.loc[i, "geometry"] = concat_fun(from_node_id, to_node_id)
print(f"Elapsed time for way 1: {time.time() - st:.2f} s")

# way 2 use apply() and lambda expression to conduct
st = time.time()
link_df["geometry2"] = link_df.apply(lambda row: concat_fun(row['from_node_id'], row['to_node_id']), axis=1)
print(f"Elapsed time for way 2: {time.time() - st:.2f} s")

link_df.to_csv("output_link.csv", index=False)
