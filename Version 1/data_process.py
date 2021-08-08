import pandas as pd
import csv

node_df = pd.read_csv("node.csv")
link_df = pd.read_csv("link.csv")

print(link_df.head())

geometry_list = []

with open("link.csv", "r", encoding='utf-8') as fp:
    reader = csv.DictReader(fp)
    for line in reader:
        from_node_id = int(line['from_node_id'])
        to_node_id = int(line['to_node_id'])

        from_node_coord_x = node_df.loc[node_df['node_id'] == from_node_id].x_coord.values[0]
        from_node_coord_y = node_df.loc[node_df['node_id'] == from_node_id].y_coord.values[0]
        to_node_coord_x = node_df.loc[node_df['node_id'] == to_node_id].x_coord.values[0]
        to_node_coord_y = node_df.loc[node_df['node_id'] == to_node_id].y_coord.values[0]
        geometry = 'LINESTRING (' + str(from_node_coord_x) + ' ' + str(from_node_coord_y) + ', ' + str(to_node_coord_x) + ' ' + str(to_node_coord_y) + ')'
        geometry_list.append(geometry)

link_df.insert(loc=len(link_df.columns), column="geometry", value=geometry_list)
link_df.to_csv("link_after_process.csv", index=False)
