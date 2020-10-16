#!/user/bin/env python
"""
w7x option starter
"""
import sys
import argparse
import os
import numpy as np

import w7x
import tfields


class SomeAction(argparse.Action):
    """Some actions."""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(
            "Example action invoked by manage in namespace: %r with values %r"
            " and option string %r" % (namespace, values, option_string)
        )
        setattr(namespace, self.dest, values)

    def showcase_dummy(self):
        """
        You can define a method to expose functionality of the class
        """
        print(self)


def diffuse(args):
    """
    diffuse a extended vmec run and save the result
    """
    raise NotImplementedError("Paths should be set by user.")
    localDir = tfields.lib.in_out.resolve(
        "~/Data/EXTENDER/{args.vmec_id}/".format(**locals())
    )
    datPath = os.path.join(localDir, "{args.vmec_id}.dat".format(**locals()))

    cyl = w7x.extender.getHybridFromDat(datPath)
    grid = w7x.flt.Grid(cylinder=cyl)
    config = w7x.flt.MagneticConfig.from_dat_file(datPath, grid=grid)
    run = w7x.flt.Run(config)

    saveDir = os.path.join(args.baseDir, "{args.vmec_id}".format(**locals()))
    tfields.lib.in_out.mkdir(saveDir, isDir=True)
    path = tfields.lib.in_out.resolve(
        os.path.join(saveDir, "{args.vmec_id}-fld.nest.npz".format(**locals()))
    )
    tracerConnectionResults, componentLoads, startPoints3D = run.line_diffusion(
        startPoints=args.startPoints
    )


def poincare(args):
    """ poincare plot creation """
    phiList = args.phi.values

    if args.phi.deg:
        phiList = [val / 180 * np.pi for val in phiList]

    if not args.assemblies.off:
        machine = w7x.flt.Machine.from_mm_ids(*args.assemblies.values)
    else:
        machine = w7x.flt.Machine()

    relativeCurrents = args.magneticConfig.relativeCurrents
    datPath = args.magneticConfig.path
    if datPath:
        datPath = tfields.lib.in_out.resolve(datPath)
        cyl = w7x.extender.getHybridFromDat(datPath)
        grid = w7x.flt.Grid(cylinder=cyl)
        magneticConfig = w7x.flt.MagneticConfig.from_dat_file(datPath, grid=grid)
    elif relativeCurrents:
        magneticConfig = w7x.flt.MagneticConfig.createWithCurrents(
            relativeCurrents=relativeCurrents
        )
    else:
        magneticConfig = w7x.flt.MagneticConfig.createWithCurrents()

    """ plotting """
    axis = tfields.plotting.gca(2)
    for phi in phiList:
        axis.grid(color="lightgrey")
        machine.plot_poincare(phi, axis=axis)
        magneticConfig.plot_poincare(phi, axis=axis)
        tfields.plotting.save(
            "~/tmp/poincare-{phi:.4f}".format(**locals()), "png", "pgf", "pdf"
        )
        axis.clear()


def manage(args_):
    """Example function."""
    print("Managing!")
    print(args_.x * args_.y)


def parse_args(args_):
    """Parse args."""
    # create the top-level parser
    parser = argparse.ArgumentParser(prog="w7x app")
    parser.add_argument(
        "--version",
        action="version",
        version="v" + w7x.__version__,
        help="Show program's version number and exit",
    )
    parser = argparse.ArgumentParser(prog="w7x app")

    # subparsers
    subparsers = parser.add_subparsers(help="sub-command help")

    # create the parser for the "extend" command
    parser_extend = subparsers.add_parser("extend", help="extend help")
    parser_extend.add_argument("vmec_id", type=str, help="vmec_id to extend")
    parser_extend.set_defaults(func=w7x.extender.extend)

    # create the parser for the "diffuse" command
    parser_diffuse = subparsers.add_parser("diffuse", help="diffuse help")
    parser_diffuse.add_argument("vmec_id", type=str, help="already extended vmec_id")
    parser_diffuse.add_argument(
        "--startPoints",
        type=int,
        help="hit points = 2 * " "startPoints (forward and backward).",
        default=12500,
    )
    parser_diffuse.add_argument(
        "--baseDir",
        type=str,
        default="~/Data/Strikeline/",
        help="already extended vmec_id",
    )
    parser_diffuse.set_defaults(func=diffuse)

    # create the parser for the "poincare" command
    parser_poincare = subparsers.add_parser("poincare", help="poincare help")
    parser_poincare.add_argument(
        "--baseDir",
        type=str,
        default="~/Data/Strikeline/",
        help="already extended vmec_id",
    )
    parser_poincare.add_argument(
        "--phi", dest="phi.values", nargs="*", type=float, default=[0.0]
    )
    parser_poincare.add_argument(
        "--phi.deg",
        dest="phi.deg",
        help="switch phi from radian to degree",
        action="store_true",
    )
    parser_poincare.add_argument(
        "--assemblies",
        dest="assemblies.values",
        nargs="+",
        type=str,
        default=w7x.Defaults.Machine.mm_ids,
    )
    parser_poincare.add_argument("--assemblies.off", action="store_true")
    parser_poincare.add_argument(
        "--magneticConfig.relativeCurrents",
        help="relative currents in case of vacuum config",
    )
    parser_poincare.add_argument(
        "--magneticConfig.coilConfig",
        help="set the coil config for the relative currents",
    )
    parser_poincare.add_argument(
        "--magneticConfig.path",
        default=None,
        help="create config with magnetic field grid at path",
    )
    parser_poincare.set_defaults(func=poincare)

    # If no arguments were used, print base-level help with possible commands.
    if len(args_) == 0:
        parser.print_help(file=sys.stderr)
        sys.exit(1)

    args_ = parser.parse_args(args_)
    # let argparse do the job of calling the appropriate function after
    # argument parsing is complete
    return args_.func(args_)


if __name__ == "__main__":
    _ = parse_args(sys.argv[1:])
