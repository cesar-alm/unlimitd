import vision_unlimtd
import pickle

print("Testing dumping")
# Make sure to save as `shapenet_random#.pickle`, where # is the random seed for the projection (seed=2, 3, 4, 5, 6)
# Also make sure to edit the name in the bottom of the file
with open("logs_final/shapenet_random6.pickle", "wb") as handle:
    pickle.dump({}, handle, protocol=pickle.HIGHEST_PROTOCOL)

seed = 1655235988902897757

init_params, _, _, post_state, _, post_losses, post_evals = vision_unlimtd.vision_unlimtd_r(seed=seed,
                                                                                                 proj_seed=6,
                                                                                                 n_epochs=10000,
                                                                                                 n_tasks=10,
                                                                                                 K=15,
                                                                                                 data_noise=0,
                                                                                                 maddox_noise=0.01,
                                                                                                 meta_lr=0.001,
                                                                                                 subspace_dimension=100)

output = {}
output["seed"] = seed
output["pre_n_epochs"]=0
output["pre_n_tasks"]=0
output["pre_K"]=15
output["post_n_epochs"]=10000
output["post_n_tasks"]=10
output["post_K"]=15
output["data_noise"]=0
output["maddox_noise"]=0.01
output["meta_lr"]=0.001
output["subspace_dimension"]=100
# output["pre_losses"]=pre_losses
output["post_losses"]=post_losses
output["init_params"]=init_params
# output["intermediate_params"]=pre_state.params
output["trained_params"]=post_state.params
# output["intermediate_mean"]=pre_state.mean
output["trained_mean"]=post_state.mean
# output["intermediate_batch_stats"]=pre_state.batch_stats
output["trained_batch_stats"]=post_state.batch_stats
output["trained_scale"]=post_state.scale
output["proj"]=post_state.proj
# output["pre_evals"] = pre_evals
output["post_evals"] = post_evals

print("Saving")
with open("logs_final/shapenet_random6.pickle", "wb") as handle:
    pickle.dump(output, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Ended...")