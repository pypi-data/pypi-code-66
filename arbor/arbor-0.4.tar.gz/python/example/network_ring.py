import arbor
import pandas, seaborn
from math import sqrt

# Construct a cell with the following morphology.
# The soma (at the root of the tree) is marked 's', and
# the end of each branch i is marked 'bi'.
#
#         b1
#        /
# s----b0
#        \
#         b2

def make_cable_cell(gid):
    # Associate labels to tags
    labels = arbor.label_dict()
    labels['soma'] = '(tag 1)'
    labels['dend'] = '(tag 3)'

    # Build a segment tree
    tree = arbor.segment_tree()

    # Soma (tag=1) with radius 6 μm, modelled as cylinder of length 2*radius
    s = tree.append(arbor.mnpos, arbor.mpoint(-12, 0, 0, 6), arbor.mpoint(0, 0, 0, 6), tag=1)

    # Single dendrite (tag=3) of length 100 μm and radius 2 μm attached to soma.
    b0 = tree.append(s, arbor.mpoint(0, 0, 0, 2), arbor.mpoint(100, 0, 0, 2), tag=3)

    # Attach two dendrites (tag=3) of length 50 μm to the end of the first dendrite.
    # Radius tapers from 2 to 0.5 μm over the length of the dendrite.
    b1 = tree.append(b0, arbor.mpoint(100, 0, 0, 2), arbor.mpoint(100+50/sqrt(2), 50/sqrt(2), 0, 0.5), tag=3)
    # Constant radius of 1 μm over the length of the dendrite.
    b2 = tree.append(b0, arbor.mpoint(100, 0, 0, 1), arbor.mpoint(100+50/sqrt(2), -50/sqrt(2), 0, 1), tag=3)

    # Mark location for synapse at the midpoint of branch 1 (the first dendrite).
    labels['synapse_site'] = '(location 1 0.5)'
    # Mark the root of the tree.
    labels['root'] = '(root)'

    cell = arbor.cable_cell(tree, labels)

    # Put hh dynamics on soma, and passive properties on the dendrites.
    cell.paint('"soma"', 'hh')
    cell.paint('"dend"', 'pas')
    # Attach a single synapse.
    cell.place('"synapse_site"', 'expsyn')
    # Attach a spike detector with threshold of -10 mV.
    cell.place('"root"', arbor.spike_detector(-10))

    return cell

class ring_recipe (arbor.recipe):

    def __init__(self, n=10):
        # The base C++ class constructor must be called first, to ensure that
        # all memory in the C++ class is initialized correctly.
        arbor.recipe.__init__(self)
        self.ncells = n

    # The num_cells method that returns the total number of cells in the model
    # must be implemented.
    def num_cells(self):
        return self.ncells

    # The cell_description method returns a cell
    def cell_description(self, gid):
        return make_cable_cell(gid)

    def num_targets(self, gid):
        return 1

    def num_sources(self, gid):
        return 1

    # The kind method returns the type of cell with gid.
    # Note: this must agree with the type returned by cell_description.
    def cell_kind(self, gid):
        return arbor.cell_kind.cable

    # Make a ring network
    def connections_on(self, gid):
        src = (gid-1)%self.ncells
        w = 0.01
        d = 5
        return [arbor.connection(arbor.cell_member(src,0), arbor.cell_member(gid,0), w, d)]

    # Attach a generator to the first cell in the ring.
    def event_generators(self, gid):
        if gid==0:
            sched = arbor.explicit_schedule([1])
            return [arbor.event_generator(arbor.cell_member(0,0), 0.1, sched)]
        return []

    def get_probes(self, gid):
        loc = arbor.location(0, 0) # at the soma
        return [arbor.cable_probe('voltage', loc)]

context = arbor.context(threads=12, gpu_id=None)
print(context)

meters = arbor.meter_manager()
meters.start(context)

ncells = 4
recipe = ring_recipe(ncells)
print(f'{recipe}')

meters.checkpoint('recipe-create', context)

hint = arbor.partition_hint()
hint.prefer_gpu = True
hint.gpu_group_size = 1000
print(f'{hint}')

hints = dict([(arbor.cell_kind.cable, hint)])
decomp = arbor.partition_load_balance(recipe, context, hints)
print(f'{decomp}')

meters.checkpoint('load-balance', context)

sim = arbor.simulation(recipe, decomp, context)

meters.checkpoint('simulation-init', context)

spike_recorder = arbor.attach_spike_recorder(sim)

# Attach a sampler to the voltage probe on cell 0.
# Sample rate of 10 sample every ms.
samplers = [arbor.attach_sampler(sim, 0.1, arbor.cell_member(gid,0)) for gid in range(ncells)]

tfinal=100
sim.run(tfinal)
print(f'{sim} finished')

meters.checkpoint('simulation-run', context)

# Print profiling information
print(f'{arbor.meter_report(meters, context)}')

# Print spike times
print('spikes:')
for sp in spike_recorder.spikes:
    print(' ', sp)

# Plot the recorded voltages over time.
print("Plotting results ...")
df_list = []
for gid in range(ncells):
    times = [s.time  for s in samplers[gid].samples(arbor.cell_member(gid,0))]
    volts = [s.value for s in samplers[gid].samples(arbor.cell_member(gid,0))]
    df_list.append(pandas.DataFrame({'t/ms': times, 'U/mV': volts, 'Cell': f"cell {gid}"}))

df = pandas.concat(df_list)
seaborn.relplot(data=df, kind="line", x="t/ms", y="U/mV",hue="Cell").savefig('network_ring_result.svg')
