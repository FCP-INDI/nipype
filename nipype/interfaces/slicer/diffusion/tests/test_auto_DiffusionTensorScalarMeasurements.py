# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..diffusion import DiffusionTensorScalarMeasurements


def test_DiffusionTensorScalarMeasurements_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    enumeration=dict(argstr='--enumeration %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='%s',
    position=-3,
    ),
    outputScalar=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = DiffusionTensorScalarMeasurements.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_DiffusionTensorScalarMeasurements_outputs():
    output_map = dict(outputScalar=dict(position=-1,
    ),
    )
    outputs = DiffusionTensorScalarMeasurements.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
