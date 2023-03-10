# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pyParflowio
else:
    import _pyParflowio

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyParflowio.delete_SwigPyIterator

    def value(self) -> "PyObject *":
        return _pyParflowio.SwigPyIterator_value(self)

    def incr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _pyParflowio.SwigPyIterator_incr(self, n)

    def decr(self, n: "size_t"=1) -> "swig::SwigPyIterator *":
        return _pyParflowio.SwigPyIterator_decr(self, n)

    def distance(self, x: "SwigPyIterator") -> "ptrdiff_t":
        return _pyParflowio.SwigPyIterator_distance(self, x)

    def equal(self, x: "SwigPyIterator") -> "bool":
        return _pyParflowio.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _pyParflowio.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _pyParflowio.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _pyParflowio.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _pyParflowio.SwigPyIterator_previous(self)

    def advance(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _pyParflowio.SwigPyIterator_advance(self, n)

    def __eq__(self, x: "SwigPyIterator") -> "bool":
        return _pyParflowio.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: "SwigPyIterator") -> "bool":
        return _pyParflowio.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _pyParflowio.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator &":
        return _pyParflowio.SwigPyIterator___isub__(self, n)

    def __add__(self, n: "ptrdiff_t") -> "swig::SwigPyIterator *":
        return _pyParflowio.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _pyParflowio.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _pyParflowio:
_pyParflowio.SwigPyIterator_swigregister(SwigPyIterator)

class IntArray3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        return _pyParflowio.IntArray3_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        return _pyParflowio.IntArray3___nonzero__(self)

    def __bool__(self) -> "bool":
        return _pyParflowio.IntArray3___bool__(self)

    def __len__(self) -> "std::array< int,3 >::size_type":
        return _pyParflowio.IntArray3___len__(self)

    def __getslice__(self, i: "std::array< int,3 >::difference_type", j: "std::array< int,3 >::difference_type") -> "std::array< int,3 > *":
        return _pyParflowio.IntArray3___getslice__(self, i, j)

    def __setslice__(self, *args) -> "void":
        return _pyParflowio.IntArray3___setslice__(self, *args)

    def __delslice__(self, i: "std::array< int,3 >::difference_type", j: "std::array< int,3 >::difference_type") -> "void":
        return _pyParflowio.IntArray3___delslice__(self, i, j)

    def __delitem__(self, *args) -> "void":
        return _pyParflowio.IntArray3___delitem__(self, *args)

    def __getitem__(self, *args) -> "std::array< int,3 >::value_type const &":
        return _pyParflowio.IntArray3___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        return _pyParflowio.IntArray3___setitem__(self, *args)

    def __init__(self, *args):
        _pyParflowio.IntArray3_swiginit(self, _pyParflowio.new_IntArray3(*args))

    def empty(self) -> "bool":
        return _pyParflowio.IntArray3_empty(self)

    def size(self) -> "std::array< int,3 >::size_type":
        return _pyParflowio.IntArray3_size(self)

    def swap(self, v: "IntArray3") -> "void":
        return _pyParflowio.IntArray3_swap(self, v)

    def begin(self) -> "std::array< int,3 >::iterator":
        return _pyParflowio.IntArray3_begin(self)

    def end(self) -> "std::array< int,3 >::iterator":
        return _pyParflowio.IntArray3_end(self)

    def rbegin(self) -> "std::array< int,3 >::reverse_iterator":
        return _pyParflowio.IntArray3_rbegin(self)

    def rend(self) -> "std::array< int,3 >::reverse_iterator":
        return _pyParflowio.IntArray3_rend(self)

    def front(self) -> "std::array< int,3 >::value_type const &":
        return _pyParflowio.IntArray3_front(self)

    def back(self) -> "std::array< int,3 >::value_type const &":
        return _pyParflowio.IntArray3_back(self)

    def fill(self, u: "std::array< int,3 >::value_type const &") -> "void":
        return _pyParflowio.IntArray3_fill(self, u)
    __swig_destroy__ = _pyParflowio.delete_IntArray3

# Register IntArray3 in _pyParflowio:
_pyParflowio.IntArray3_swigregister(IntArray3)

class PFData(object):
    r"""
    class: PFData
    The PFData class refers to the contents of ParflowBinary File. This class provides several methods to read
    and write those files as well as export the data.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyParflowio.delete_PFData

    def fileReadPoint(self, z: "int", y: "int", x: "int") -> "double":
        r"""
         Read a single point from the file, without loading it all into memory.
        :type z: int
        :param z:       Z index of the point
        :type y: int
        :param y:       Y index of the point
        :type x: int
        :param x:       X index of the point
        :rtype: float
        :return: Value of the data at the specified point.
        """
        return _pyParflowio.PFData_fileReadPoint(self, z, y, x)

    def fileReadSubgridAtPointIndex(self, z: "int", y: "int", x: "int") -> "std::vector< double,std::allocator< double > >":
        r"""
         Read in the subgrid containing the specified point from the file.
        :type z: int
        :param z:   Z index of the point inside the desired subgrid.
        :type y: int
        :param y:   Y index of the point inside the desired subgrid.
        :type x: int
        :param x:   X index of the point inside the desired subgrid.
        :rtype: std::vector< double,std::allocator< double > >
        :return: The subgrid containing the specified point.
        """
        return _pyParflowio.PFData_fileReadSubgridAtPointIndex(self, z, y, x)

    def fileReadSubgridAtGridIndex(self, gridZ: "int", gridY: "int", gridX: "int") -> "std::vector< double,std::allocator< double > >":
        r"""
         Read in the subgrid at the specified subgrid index. Note that this is different than the point indicies.
        :type gridZ: int
        :param gridZ:   The Z index of the subgrid.
        :type gridY: int
        :param gridY:   The Y index of the subgrid.
        :type gridX: int
        :param gridX:   The X index of the subgrid.
        :rtype: std::vector< double,std::allocator< double > >
        :return: Value of the subgrid at the specified index.
        """
        return _pyParflowio.PFData_fileReadSubgridAtGridIndex(self, gridZ, gridY, gridX)

    def getSubgridIndexZ(self, idx: "int") -> "int":
        r"""
         Returns the Z subgrid index of the point at the specified Z index.
        :type idx: int
        :param idx:   The Z index of the point.
        :rtype: int
        :return: The Z index of the subgrid containing the point.
        """
        return _pyParflowio.PFData_getSubgridIndexZ(self, idx)

    def getSubgridIndexY(self, idx: "int") -> "int":
        r"""
         Returns the Y subgrid index of the point at the specified Y index.
        :type idx: int
        :param idx:   The Y index of the point.
        :rtype: int
        :return: The Y index of the subgrid containing the point.
        """
        return _pyParflowio.PFData_getSubgridIndexY(self, idx)

    def getSubgridIndexX(self, idx: "int") -> "int":
        r"""
         Returns the X subgrid index of the point at the specified X index.
        :type idx: int
        :param idx:   The X index of the point.
        :rtype: int
        :return: The X index of the subgrid containing the point.
        """
        return _pyParflowio.PFData_getSubgridIndexX(self, idx)

    def getSubgridSizeZ(self, idx: "int") -> "int":
        r"""
         Returns the size in the Z direction of the subgrid at the specified Z index.
        :type idx: int
        :param idx:   The Z index of the target subgrid.
        :rtype: int
        :return: The Z size of the subgrid at the specified index.
        """
        return _pyParflowio.PFData_getSubgridSizeZ(self, idx)

    def getSubgridSizeY(self, idx: "int") -> "int":
        r"""
         Returns the size in the Y direction of the subgrid at the specified Y index.
        :type idx: int
        :param idx:   The Y index of the target subgrid.
        :rtype: int
        :return: The Y size of the subgrid at the specified index.
        """
        return _pyParflowio.PFData_getSubgridSizeY(self, idx)

    def getSubgridSizeX(self, idx: "int") -> "int":
        r"""
         Returns the size in the X direction of the subgrid at the specified X index.
        :type idx: int
        :param idx:   The X index of the target subgrid.
        :rtype: int
        :return: The X size of the subgrid at the specified index.
        """
        return _pyParflowio.PFData_getSubgridSizeX(self, idx)

    def getSubgridStartZ(self, gridIdx: "int") -> "int":
        r"""
        Returns the starting Z index of the specified subgrid.
        :param idx:   The Z subgrid index of the specified subgrid.
        :rtype: int
        :return: The first Z index of the subgrid.
        """
        return _pyParflowio.PFData_getSubgridStartZ(self, gridIdx)

    def getSubgridStartY(self, gridIdx: "int") -> "int":
        r"""See also: getSubgridStartZ"""
        return _pyParflowio.PFData_getSubgridStartY(self, gridIdx)

    def getSubgridStartX(self, gridIdx: "int") -> "int":
        r"""See also: getSubgridStartZ"""
        return _pyParflowio.PFData_getSubgridStartX(self, gridIdx)

    def getNormalBlockSizeZ(self) -> "int":
        r"""
         Returns the size in the Z direction of a normal block.
        :rtype: int
        :return: Z size of a normal block.
        """
        return _pyParflowio.PFData_getNormalBlockSizeZ(self)

    def getNormalBlockSizeY(self) -> "int":
        r"""See also: getNormalBlockSizeZ"""
        return _pyParflowio.PFData_getNormalBlockSizeY(self)

    def getNormalBlockSizeX(self) -> "int":
        r"""See also: getNormalBlockSizeZ"""
        return _pyParflowio.PFData_getNormalBlockSizeX(self)

    def getNormalBlockStartZ(self) -> "int":
        r"""
         Returns the index where normal blocks begin(inclusive).
        :rtype: int
        :return: Zero if there are no remainder blocks.
        """
        return _pyParflowio.PFData_getNormalBlockStartZ(self)

    def getNormalBlockStartY(self) -> "int":
        r"""See also: getNormalBlockStartZ"""
        return _pyParflowio.PFData_getNormalBlockStartY(self)

    def getNormalBlockStartX(self) -> "int":
        r"""See also: getNormalBlockStartZ"""
        return _pyParflowio.PFData_getNormalBlockStartX(self)

    def getNormalBlockStartGridZ(self) -> "int":
        r"""
         Similar to getNormalBlockStartZ, but returns the grid index instead of the point index.
        :rtype: int
        :return: The grid index where normal blocks begin (inclusive)
        """
        return _pyParflowio.PFData_getNormalBlockStartGridZ(self)

    def getNormalBlockStartGridY(self) -> "int":
        r"""See also: getNormalBlockStartGridZ"""
        return _pyParflowio.PFData_getNormalBlockStartGridY(self)

    def getNormalBlockStartGridX(self) -> "int":
        r""" See also: getNormalBlockStartGridZ"""
        return _pyParflowio.PFData_getNormalBlockStartGridX(self)

    def loadHeader(self) -> "int":
        r"""loadHeader"""
        return _pyParflowio.PFData_loadHeader(self)

    def loadPQR(self) -> "int":
        r"""
         This function loads the subgrid headers in order to calculate PQR. The only way to do this is by reading all of the subgrids and counting them, so this function incurs an performance penalty proportional to seeking and reading each subgrid header.
        :rtype: int
        :return: 0 on success. Other values indicate an error.
        """
        return _pyParflowio.PFData_loadPQR(self)

    def getFilename(self) -> "std::string":
        return _pyParflowio.PFData_getFilename(self)

    def loadData(self) -> "int":
        r"""loadData"""
        return _pyParflowio.PFData_loadData(self)

    def loadClipOfData(self, clip_x: "int", clip_y: "int", extent_x: "int", extent_y: "int") -> "int":
        return _pyParflowio.PFData_loadClipOfData(self, clip_x, clip_y, extent_x, extent_y)

    def loadDataThreaded(self, numThreads: "int") -> "int":
        r"""
        Performs the same functionality as loadData(), but loads the file in parallel, using the supplied number of threads.
        :type numThreads: int
        :param numThreads:  The number of threads to use, must be at least one.
        :rtype: int
        :return: 0 if success, non-zero if error.
        """
        return _pyParflowio.PFData_loadDataThreaded(self, numThreads)

    def writeFile(self, filename: "std::string") -> "int":
        r"""
        writeFile
        :param string: filenamee
        :rtype: int
        :return: int
        """
        return _pyParflowio.PFData_writeFile(self, filename)

    def distFile(self, P: "int", Q: "int", R: "int", outFile: "std::string") -> "int":
        r"""
        distFile
        :param int: P
        :param int: Q
        :param int: R
        :param string: outFile
        :rtype: int
        :return: int
        """
        return _pyParflowio.PFData_distFile(self, P, Q, R, outFile)
    differenceType_none = _pyParflowio.PFData_differenceType_none
    differenceType_z = _pyParflowio.PFData_differenceType_z
    differenceType_y = _pyParflowio.PFData_differenceType_y
    differenceType_x = _pyParflowio.PFData_differenceType_x
    differenceType_dZ = _pyParflowio.PFData_differenceType_dZ
    differenceType_dY = _pyParflowio.PFData_differenceType_dY
    differenceType_dX = _pyParflowio.PFData_differenceType_dX
    differenceType_nZ = _pyParflowio.PFData_differenceType_nZ
    differenceType_nY = _pyParflowio.PFData_differenceType_nY
    differenceType_nX = _pyParflowio.PFData_differenceType_nX
    differenceType_data = _pyParflowio.PFData_differenceType_data

    def compare(self, otherObj: "PFData") -> "PFData::differenceType":
        r"""
         Compares `this` and another PFData object. Comparison is based on `Z`, `Y`, `X`, `DZ`, `DY`, `DX`, and the data.
        Note: The behavior is undefined if `this` or `otherObj` is not fully initialized. The return value corresponds to the first difference found.
        :type otherObj: :py:class:`PFData`, in
        :param otherObj:        Other object to compare with.
        :type diffIndex: std::array< int,3 >, out
        :param diffIndex:       Unused if it is `nullptr` and/or the return values are not `data` Otherwise contains the location where the first difference occurs.
        """
        return _pyParflowio.PFData_compare(self, otherObj)

    def unflattenIndex(self, index: "int") -> "std::array< int,3 >":
        r"""
         Given a flattened index into `data`, unflatten it into its `ZYX` components.
        Note: The behavior is undefined if the dimension data is not fully initialized.
        :type index: int, int
        :param index:           The flattened index of the `data`
        """
        return _pyParflowio.PFData_unflattenIndex(self, index)

    def unflattenGridIndex(self, index: "int") -> "std::array< int,3 >":
        r"""
         Given a flattened subgrid index (value in range [0, getNumSubgrids()), unflatten it.
        :type index: int
        :param index:           Subgrid index, [0, getNumSubgrids())
        """
        return _pyParflowio.PFData_unflattenGridIndex(self, index)

    def getZ(self) -> "double":
        r"""
        :param double: get[Z,Y,X] [Z] is the lower left corner of the Computational Grid.
            This function is useful either when reading an existing file or when confirming the configuration
            of a file that is being created where the computational grid has already been set.
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData_getZ(self)

    def getY(self) -> "double":
        r"""
         :param double:  get[Z,Y,X] [Y] is the lower left corner of the Computational Grid.
            This function is useful either when reading an existing file or when confirming the configuration
            of a file that is being created where the computational grid has already been set.
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData_getY(self)

    def getX(self) -> "double":
        r"""
         :param double: get[Z,Y,X] [X] is the lower left corner of the Computational Grid.
            This function is useful either when reading an existing file or when
            confirming the configuration of a file that is being created where the
            computational grid has already been set.
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData_getX(self)

    def getP(self) -> "int":
        r"""
        get[P,Q,R]
        [P,Q,R] define processor topology for blocking the file
        This function is useful either when reading an existing file or when confirming the configuration
        of a file that is being created where the computational grid has already been set.
        :rtype: int
        :return: int
        """
        return _pyParflowio.PFData_getP(self)

    def getQ(self) -> "int":
        return _pyParflowio.PFData_getQ(self)

    def getR(self) -> "int":
        return _pyParflowio.PFData_getR(self)

    def setP(self, P: "int") -> "void":
        r"""
        set[P,Q,R]
        :param int: [P,Q,R]
            [P,Q,R] define processor topology for blocking the file
            This function is useful when creating a new pfb file. It is important to note that you can call this
            function on an existing file, but it will invalidate the file and break all subsequent uses of the class
            unless you call load_file() again to reset the value back to the one used in the file.
        """
        return _pyParflowio.PFData_setP(self, P)

    def setQ(self, Q: "int") -> "void":
        return _pyParflowio.PFData_setQ(self, Q)

    def setR(self, R: "int") -> "void":
        return _pyParflowio.PFData_setR(self, R)

    def setZ(self, Z: "double") -> "void":
        r"""
        set[Z,Y,X]
        :param double: [Z,Y,X]
            [Z,Y,X] is the lower left corner of the Computational Grid.
            This function is useful when creating a new pfb file. It is important to note that you can call this
            function on an existing file, but it will invalidate the file and break all subsequent uses of the class
            unless you call load_file() again to reset the value back to the one used in the file.
              :param double: set[Z,Y,X] [Z] is the lower left corner of the Computational
            Grid. This function is useful when creating a new pfb file. It is
            important to note that you can call this function on an existing file,
            but it will invalidate the file and break all subsequent uses of the
            class unless you call load_file() again to reset the value back to the
            one used in the file.
        """
        return _pyParflowio.PFData_setZ(self, Z)

    def setY(self, Y: "double") -> "void":
        r"""
        :param double: set[Z,Y,X] [Y] is the lower left corner of the Computational
           Grid. This function is useful when creating a new pfb file. It is
           important to note that you can call this function on an existing file,
           but it will invalidate the file and break all subsequent uses of the
           class unless you call load_file() again to reset the value back to the
           one used in the file.
        """
        return _pyParflowio.PFData_setY(self, Y)

    def setX(self, X: "double") -> "void":
        r"""
        :param double: set[Z,Y,X] [X] is the lower left corner of the Computational
           Grid. This function is useful when creating a new pfb file. It is
           important to note that you can call this function on an existing file,
           but it will invalidate the file and break all subsequent uses of the
           class unless you call load_file() again to reset the value back to the
           one used in the file.
        """
        return _pyParflowio.PFData_setX(self, X)

    def getNZ(self) -> "int":
        r"""
         :param get[NZ,NY,NX]: [NZ] describes the dimensions of the
            computational domain. This function is useful either when reading an
            existing file or when confirming the configuration of a file that is
            being created where the computational grid has already been set.
        :rtype: int
        :return: int
        """
        return _pyParflowio.PFData_getNZ(self)

    def getNY(self) -> "int":
        r"""
         :param get[NZ,NY,NX]: [NY] describes the dimensions of the
            computational domain. This function is useful either when reading an
            existing file or when confirming the configuration of a file that is
            being created where the computational grid has already been set.
        :rtype: int
        :return: int
        """
        return _pyParflowio.PFData_getNY(self)

    def getNX(self) -> "int":
        r"""
         :param get[NZ,NY,NX]: [NX] describe the dimensions of the
            computational domain. This function is useful either when reading an
            existing file or when confirming the configuration of a file that is
            being created where the computational grid has already been set.
        :rtype: int
        :return: int
        """
        return _pyParflowio.PFData_getNX(self)

    def setNZ(self, NZ: "int") -> "void":
        r"""
        :param double: set[NZ,NY,NX] [NZ] describes the dimensions of the
           computational grid. This function is useful when creating a new pfb file.
           It is important to note that you can call this function on an existing
           file, but it will invalidate the file and break all subsequent uses of
           the class unless you call load_file() again to reset the value back to
           the one used in the file.
        """
        return _pyParflowio.PFData_setNZ(self, NZ)

    def setNY(self, NY: "int") -> "void":
        r"""
        :param double: set[NZ,NY,NX] [NY] describes the dimensions of the
           computational grid. This function is useful when creating a new pfb file.
           It is important to note that you can call this function on an existing
           file, but it will invalidate the file and break all subsequent uses of
           the class unless you call load_file() again to reset the value back to
           the one used in the file.
        """
        return _pyParflowio.PFData_setNY(self, NY)

    def setNX(self, NX: "int") -> "void":
        r"""
        :param double: set[NZ,NY,NX] [NX] describes the dimensions of the
           computational grid. This function is useful when creating a new pfb file.
           It is important to note that you can call this function on an existing
           file, but it will invalidate the file and break all subsequent uses of
           the class unless you call load_file() again to reset the value back to
           the one used in the file.
        """
        return _pyParflowio.PFData_setNX(self, NX)

    def getDZ(self) -> "double":
        r"""
         param get[DZ,DY,DX] [DZ] describes the dimensions of the
        computational grid. This function is useful either when reading an
        existing file or when confirming the configuration of a file that is
        being created where the computational grid has already been set.
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData_getDZ(self)

    def getDY(self) -> "double":
        r"""
         :param get[DZ,DY,DX]: [DY] describes the dimensions of the
            computational grid. This function is useful either when reading an
            existing file or when confirming the configuration of a file that is
            being created where the computational grid has already been set.
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData_getDY(self)

    def getDX(self) -> "double":
        r"""
         :param get[DZ,DY,DX]: [DX] describes the dimensions of the
            computational grid. This function is useful either when reading an
            existing file or when confirming the configuration of a file that is
            being created where the computational grid has already been set.
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData_getDX(self)

    def setDZ(self, DZ: "double") -> "void":
        r"""
        :param double[DZ,DY,DX]: [DZ] describes the dimensions of the
           computational grid. This function is useful when creating a new pfb file.
           It is important to note that you can call this function on an existing
           file, but it will invalidate the file and break all subsequent uses of
           the class unless you call load_file() again to reset the value back to
           the one used in the file.
        """
        return _pyParflowio.PFData_setDZ(self, DZ)

    def setDY(self, DY: "double") -> "void":
        r"""
        :param double: [DZ,DY,DX] [DY] describes the dimensions of the
           computational grid. This function is useful when creating a new pfb file.
           It is important to note that you can call this function on an existing
           file, but it will invalidate the file and break all subsequent uses of
           the class unless you call load_file() again to reset the value back to
           the one used in the file.
        """
        return _pyParflowio.PFData_setDY(self, DY)

    def setDX(self, DX: "double") -> "void":
        r"""
        :param double: [DZ,DY,DX] [DX] describes the dimensions of the
           computational grid. This function is useful when creating a new pfb file.
           It is important to note that you can call this function on an existing
           file, but it will invalidate the file and break all subsequent uses of
           the class unless you call load_file() again to reset the value back to
           the one used in the file.
        """
        return _pyParflowio.PFData_setDX(self, DX)

    def getNumSubgrids(self) -> "int":
        r"""
        getNumSubgrids() const
        :param empty:
        :rtype: int
        :return: no return
        """
        return _pyParflowio.PFData_getNumSubgrids(self)

    def setNumSubgrids(self, mNumSubgrids: "int") -> "void":
        r"""
         setNumSubgrids
        :param int: mNumSubgrids
        :rtype: void
        :return: no return
        """
        return _pyParflowio.PFData_setNumSubgrids(self, mNumSubgrids)

    def __call__(self, z: "int", y: "int", x: "int") -> "double":
        r"""
        operator
        :type z: int
        :param z:
        :type y: int
        :param y:
        :type x: int
        :param x:
        :rtype: float
        :return: double
        """
        return _pyParflowio.PFData___call__(self, z, y, x)

    def getSubgridData(self, grid: "int") -> "double *":
        r"""
        getSubgridData
        :param int: grid
        """
        return _pyParflowio.PFData_getSubgridData(self, grid)

    def getIndexOrder(self) -> "std::string":
        r"""
        getIndexOrder
        :rtype: string
        :return: string
        """
        return _pyParflowio.PFData_getIndexOrder(self)

    def setIndexOrder(self, indexOrder: "std::string") -> "void":
        r"""
        setIndexOrder
        :param string: indexOrder
        """
        return _pyParflowio.PFData_setIndexOrder(self, indexOrder)

    def close(self) -> "void":
        r"""close file. Destructor should automatically handle this in almost all cases."""
        return _pyParflowio.PFData_close(self)

    def setIsDataOwner(self, isOwner: "bool") -> "void":
        r"""
        Sets if the class owns the backing data or not. Mostly provided for compatibility with SWIG.
        :type isOwner: boolean
        :param isOwner:     True if the class should free the data upon destruction, false otherwise.
        """
        return _pyParflowio.PFData_setIsDataOwner(self, isOwner)

    def __init__(self, *args):
        _pyParflowio.PFData_swiginit(self, _pyParflowio.new_PFData(*args))

    def setDataArray(self, pyObjIn: "PyObject *") -> "void":
        return _pyParflowio.PFData_setDataArray(self, pyObjIn)

    def moveDataArray(self) -> "PyObject *":
        return _pyParflowio.PFData_moveDataArray(self)

    def copyDataArray(self) -> "PyObject *":
        return _pyParflowio.PFData_copyDataArray(self)

    def viewDataArray(self) -> "PyObject *":
        return _pyParflowio.PFData_viewDataArray(self)

    def __str__(self):
        s = str(self.__class__.__name__) + "(X={}, Y={}, Z={}, NX={}, NY={}, NZ={}, DX={}, DY={}, DZ={}, indexOrder={})".format(
                self.getX(), self.getY(), self.getZ(), self.getNX(), self.getNY(), self.getNZ(), self.getDX(),
                self.getDY(), self.getDZ(), self.getIndexOrder())
        return s


# Register PFData in _pyParflowio:
_pyParflowio.PFData_swigregister(PFData)


def calcOffset(extent: "int", block_count: "int", block_idx: "int") -> "int":
    r"""
    calcOffset
    :param int: extent
    :param int: block_count
    :param int: block_idx
    """
    return _pyParflowio.calcOffset(extent, block_count, block_idx)

def calcExtent(extent: "int", block_count: "int", block_idx: "int") -> "int":
    r"""
    calcExtent
    :param int: extent
    :param int: block_count
    :param int: block_idx
    :rtype: int
    :return: int
    """
    return _pyParflowio.calcExtent(extent, block_count, block_idx)


