import openstack

from config import *

def create_cluster(conn):
    print("Create cluster:")

    spec = {
        "name": CLUSTER_NAME,
        "profile_id": PROFILE_ID,
        "min_size": 0,
        "max_size": -1,
        "desired_capacity": 1,
    }

    cluster = conn.clustering.create_cluster(**spec)
    print(cluster.to_dict())


def get_cluster(conn):
    print("Get cluster:")

    cluster = conn.clustering.get_cluster(CLUSTER_ID)
    print(cluster.to_dict())



def add_nodes_to_cluster(conn,NODE_ID):
    print("Add nodes to cluster:")
    node_ids = [NODE_ID]
    res = conn.clustering.add_nodes_to_cluster(CLUSTER_ID, node_ids)
    print(res)



def create_node(conn,NODE_NAME):
    print("Create Node:")

    spec = {
        'name': NODE_NAME,
        'profile_id': PROFILE_ID,
    }
    node = conn.clustering.create_node(**spec)
    print(node.to_dict())

##################################################

def main():
    print("start connection...")
    conn = openstack.connect(cloud='openstack')
    print("openstack connected...")
    create_cluster(conn)
    print("create cluster...")
    for i in range(3):
        create_node(conn,'node'+i)
        add_nodes_to_cluster(conn,'node'+i)
        print("create node"+i)

    print("cluster detail:")
    get_cluster(conn)

if __name__ == "__main__":
    main()
