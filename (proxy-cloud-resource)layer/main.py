import openstack
import openstack.config.loader
import openstack.compute.v2.server
from pprint import pprint

# Ansii color class
class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'  # RESET COLOR

def main():

    while 1:
        x = input("whitch option?\n" + bcolors.GREEN + "1) Proxy layer\n" + bcolors.YELLOW + "2) Cloud layer\n" + bcolors.RED + "3) resource layer\n" + bcolors.YELLOW + ">> " + bcolors.RESET)

        try:
            if(x == "1"):
                proxy_layer()
            elif(x == "2"):
                cloud_layer()

            elif(x == "3"):
                resource_layer()

            else:
                print("Invalid input")

        except KeyboardInterrupt:
            exit()

def proxy_layer():
    # openstack.enable_logging(debug=True)
    openstack.enable_logging(debug=False)
    conn = openstack.connect(cloud='openstack')
    for server in conn.compute.servers():
        pprint(server.to_dict())

def cloud_layer():
    # openstack.enable_logging(debug=True)
    openstack.enable_logging(debug=False)
    conn = openstack.connect(cloud='openstack')
    for server in conn.list_servers():
        pprint(server.to_dict())

def resource_layer():
    # openstack.enable_logging(debug=True)
    openstack.enable_logging(debug=False)
    conn = openstack.connect(cloud='openstack')
    for server in openstack.compute.v2.server.Server.list(session=conn.compute):
        pprint(server.to_dict())


if __name__ == "__main__":
    main()
