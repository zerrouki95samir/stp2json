# This file is part of pythonOCC.
##
# pythonOCC is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# pythonOCC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.Core.Tesselator import ShapeTesselator


def stp2json(filePath):

    def load_model_file(filePath):
        step_reader = STEPControl_Reader()
        status = step_reader.ReadFile(filePath)

        if status == IFSelect_RetDone:  # check status
            failsonly = False
            step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
            step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)

            ok = step_reader.TransferRoot(1)
            nbs = step_reader.NbShapes()

            shape = step_reader.Shape(1)
            return shape
        else:
            raise Exception(":Error: can't read file - Method: load_STEP_file")

    def exportThreeJS(filePath, shape):
        tess = ShapeTesselator(shape)
        tess.Compute(compute_edges=False, mesh_quality=1.)

        json_shape = tess.ExportShapeToThreejsJSONString(filePath)

        json_shape = json_shape.replace('data\\', 'data/')
        json_shape = json_shape.replace(
            '\\step_postprocessed\\', '/step_postprocessed/')

        return json_shape

    shape = load_model_file(filePath)
    json_shape = exportThreeJS(filePath, shape)

    return json_shape
