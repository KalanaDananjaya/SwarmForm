from swarmform import SwarmPad
from swarmform.core.swarmwork import SwarmFlow
from swarmform.core.cluster import cluster_sf

if __name__ == "__main__":
	# set up the SwarmPad and reset it
	swarmpad = SwarmPad()
	swarmpad.reset('', require_password=False)

	filename = "/home/kalana/fyp/fyp-new/SwarmForm/swarmform/examples/workflow_generator_examples/Montage_25-1603604836/Montage_25.yaml"
	# create the Firework consisting of a custom "Addition" task
	unclustered_sf = SwarmFlow.from_file(filename)

	# store workflow
	swarmpad.add_sf(unclustered_sf)

	sf = swarmpad.get_sf_by_id(unclustered_sf.sf_id)

	# Cluster the SwarmFlow
	clustered_sf = cluster_sf(swarmpad, unclustered_sf.sf_id, "wpa")

	# Archive unclustered SwarmFlow
	unclustered_sf_fw_id = unclustered_sf.fws[0].fw_id

	swarmpad.archive_wf(unclustered_sf_fw_id)

	swarmpad.add_sf(clustered_sf)
