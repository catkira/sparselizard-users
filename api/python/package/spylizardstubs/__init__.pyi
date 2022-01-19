from __future__ import annotations
import spylizard
import typing
from spylizard.spylizard import densemat
from spylizard.spylizard import eigenvalue
from spylizard.spylizard import expression
from spylizard.spylizard import field
from spylizard.spylizard import formulation
from spylizard.spylizard import genalpha
from spylizard.spylizard import impliciteuler
from spylizard.spylizard import indexmat
from spylizard.spylizard import integration
from spylizard.spylizard import mat
from spylizard.spylizard import mesh
from spylizard.spylizard import parameter
from spylizard.spylizard import port
from spylizard.spylizard import shape
from spylizard.spylizard import spanningtree
from spylizard.spylizard import spline
from spylizard.spylizard import universe
from spylizard.spylizard import vec
from spylizard.spylizard import vectorfieldselect
from spylizard.spylizard import wallclock

__all__ = [
    "abs",
    "acos",
    "adapt",
    "alladapt",
    "allgather",
    "allpartition",
    "andpositive",
    "array1x1",
    "array1x2",
    "array1x3",
    "array2x1",
    "array2x2",
    "array2x3",
    "array3x1",
    "array3x2",
    "array3x3",
    "asin",
    "atan",
    "barrier",
    "broadcast",
    "comp",
    "compx",
    "compy",
    "compz",
    "continuitycondition",
    "cos",
    "count",
    "crossproduct",
    "curl",
    "dbtoneper",
    "densemat",
    "determinant",
    "div",
    "dof",
    "doubledotproduct",
    "dt",
    "dtdt",
    "dtdtdt",
    "dtdtdtdt",
    "dx",
    "dy",
    "dz",
    "eigenvalue",
    "entry",
    "exchange",
    "exp",
    "expression",
    "eye",
    "field",
    "fieldorder",
    "finalize",
    "formulation",
    "gather",
    "genalpha",
    "getharmonic",
    "getmaxnumthreads",
    "getpi",
    "getrandom",
    "getrank",
    "getsubversion",
    "gettime",
    "gettotalforce",
    "getversion",
    "getversionname",
    "grad",
    "greenlagrangestrain",
    "grouptimesteps",
    "ifpositive",
    "impliciteuler",
    "indexmat",
    "initialize",
    "integral",
    "integration",
    "inverse",
    "isavailable",
    "isdefined",
    "isempty",
    "isinside",
    "istouching",
    "linspace",
    "loadshape",
    "loadvector",
    "log10",
    "logspace",
    "makeharmonic",
    "mat",
    "max",
    "mesh",
    "meshsize",
    "min",
    "mod",
    "moveharmonic",
    "norm",
    "normal",
    "on",
    "orpositive",
    "parameter",
    "periodicitycondition",
    "port",
    "pow",
    "predefinedacousticradiation",
    "predefinedacoustics",
    "predefinedacousticstructureinteraction",
    "predefinedadvectiondiffusion",
    "predefineddiffusion",
    "predefinedelasticity",
    "predefinedelectrostaticforce",
    "predefinedmagnetostaticforce",
    "predefinednavierstokes",
    "predefinedstabilization",
    "predefinedstokes",
    "printtotalforce",
    "printvector",
    "printversion",
    "receive",
    "scatter",
    "scatterwrite",
    "selectall",
    "selectintersection",
    "selectunion",
    "send",
    "setaxisymmetry",
    "setdata",
    "setfundamentalfrequency",
    "setmaxnumthreads",
    "setphysicalregionshift",
    "settime",
    "settimederivative",
    "shape",
    "sin",
    "solve",
    "spanningtree",
    "spline",
    "spylizard",
    "sqrt",
    "strain",
    "sum",
    "t",
    "tan",
    "tangent",
    "tf",
    "trace",
    "transpose",
    "universe",
    "vec",
    "vectorfieldselect",
    "vonmises",
    "wallclock",
    "writeshapefunctions",
    "writevector",
    "zienkiewiczzhu"
]


def abs(input: spylizard.expression) -> spylizard.expression:
    pass
def acos(input: spylizard.expression) -> spylizard.expression:
    pass
def adapt(verbosity: int = 0) -> bool:
    pass
def alladapt(verbosity: int = 0) -> bool:
    pass
@typing.overload
def allgather(fragment: typing.List[float], gathered: typing.List[float]) -> None:
    pass
@typing.overload
def allgather(fragment: typing.List[float], gathered: typing.List[float], fragsizes: typing.List[int]) -> None:
    pass
@typing.overload
def allgather(fragment: typing.List[int], gathered: typing.List[int]) -> None:
    pass
@typing.overload
def allgather(fragment: typing.List[int], gathered: typing.List[int], fragsizes: typing.List[int]) -> None:
    pass
def allpartition(meshfile: str) -> str:
    pass
def andpositive(exprs: typing.List[spylizard.expression]) -> spylizard.expression:
    pass
def array1x1(arg0: spylizard.expression) -> spylizard.expression:
    pass
def array1x2(arg0: spylizard.expression, arg1: spylizard.expression) -> spylizard.expression:
    pass
def array1x3(arg0: spylizard.expression, arg1: spylizard.expression, arg2: spylizard.expression) -> spylizard.expression:
    pass
def array2x1(arg0: spylizard.expression, arg1: spylizard.expression) -> spylizard.expression:
    pass
def array2x2(arg0: spylizard.expression, arg1: spylizard.expression, arg2: spylizard.expression, arg3: spylizard.expression) -> spylizard.expression:
    pass
def array2x3(arg0: spylizard.expression, arg1: spylizard.expression, arg2: spylizard.expression, arg3: spylizard.expression, arg4: spylizard.expression, arg5: spylizard.expression) -> spylizard.expression:
    pass
def array3x1(arg0: spylizard.expression, arg1: spylizard.expression, arg2: spylizard.expression) -> spylizard.expression:
    pass
def array3x2(arg0: spylizard.expression, arg1: spylizard.expression, arg2: spylizard.expression, arg3: spylizard.expression, arg4: spylizard.expression, arg5: spylizard.expression) -> spylizard.expression:
    pass
def array3x3(arg0: spylizard.expression, arg1: spylizard.expression, arg2: spylizard.expression, arg3: spylizard.expression, arg4: spylizard.expression, arg5: spylizard.expression, arg6: spylizard.expression, arg7: spylizard.expression, arg8: spylizard.expression) -> spylizard.expression:
    pass
def asin(input: spylizard.expression) -> spylizard.expression:
    pass
def atan(input: spylizard.expression) -> spylizard.expression:
    pass
def barrier() -> None:
    pass
@typing.overload
def broadcast(broadcaster: int, data: typing.List[float]) -> None:
    pass
@typing.overload
def broadcast(broadcaster: int, data: typing.List[int]) -> None:
    pass
def comp(selectedcomp: int, input: spylizard.expression) -> spylizard.expression:
    pass
def compx(input: spylizard.expression) -> spylizard.expression:
    pass
def compy(input: spylizard.expression) -> spylizard.expression:
    pass
def compz(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def continuitycondition(gamma1: int, gamma2: int, u1: spylizard.field, u2: spylizard.field, lagmultorder: int, errorifnotfound: bool = True) -> typing.List[spylizard.integration]:
    pass
@typing.overload
def continuitycondition(gamma1: int, gamma2: int, u1: spylizard.field, u2: spylizard.field, rotcent: typing.List[float], rotangz: float, angzmod: float, factor: float, lagmultorder: int) -> typing.List[spylizard.integration]:
    pass
def cos(input: spylizard.expression) -> spylizard.expression:
    pass
def count() -> int:
    pass
def crossproduct(a: spylizard.expression, b: spylizard.expression) -> spylizard.expression:
    pass
def curl(input: spylizard.expression) -> spylizard.expression:
    pass
def dbtoneper(toconvert: spylizard.expression) -> spylizard.expression:
    pass
def determinant(input: spylizard.expression) -> spylizard.expression:
    pass
def div(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def dof(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def dof(input: spylizard.expression, physreg: int) -> spylizard.expression:
    pass
def doubledotproduct(a: spylizard.expression, b: spylizard.expression) -> spylizard.expression:
    pass
def dt(input: spylizard.expression) -> spylizard.expression:
    pass
def dtdt(input: spylizard.expression) -> spylizard.expression:
    pass
def dtdtdt(input: spylizard.expression) -> spylizard.expression:
    pass
def dtdtdtdt(input: spylizard.expression) -> spylizard.expression:
    pass
def dx(input: spylizard.expression) -> spylizard.expression:
    pass
def dy(input: spylizard.expression) -> spylizard.expression:
    pass
def dz(input: spylizard.expression) -> spylizard.expression:
    pass
def entry(row: int, col: int, input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def exchange(targetranks: typing.List[int], sends: typing.List[typing.List[float]], receives: typing.List[typing.List[float]]) -> None:
    pass
@typing.overload
def exchange(targetranks: typing.List[int], sends: typing.List[typing.List[int]], receives: typing.List[typing.List[int]]) -> None:
    pass
@typing.overload
def exchange(targetranks: typing.List[int], sendvalues: typing.List[float], receivevalues: typing.List[float]) -> None:
    pass
@typing.overload
def exchange(targetranks: typing.List[int], sendvalues: typing.List[int], receivevalues: typing.List[int]) -> None:
    pass
def exp(input: spylizard.expression) -> spylizard.expression:
    pass
def eye(size: int) -> spylizard.expression:
    pass
def fieldorder(input: spylizard.field, alpha: float = -1.0, absthres: float = 0.0) -> spylizard.expression:
    pass
def finalize() -> None:
    pass
@typing.overload
def gather(gatherer: int, fragment: typing.List[float], gathered: typing.List[float]) -> None:
    pass
@typing.overload
def gather(gatherer: int, fragment: typing.List[float], gathered: typing.List[float], fragsizes: typing.List[int]) -> None:
    pass
@typing.overload
def gather(gatherer: int, fragment: typing.List[int], gathered: typing.List[int]) -> None:
    pass
@typing.overload
def gather(gatherer: int, fragment: typing.List[int], gathered: typing.List[int], fragsizes: typing.List[int]) -> None:
    pass
def getharmonic(harmnum: int, input: spylizard.expression, numfftharms: int = -1) -> spylizard.expression:
    pass
def getmaxnumthreads() -> int:
    pass
def getpi() -> float:
    pass
def getrandom() -> float:
    pass
def getrank() -> int:
    pass
def getsubversion() -> int:
    pass
def gettime() -> float:
    pass
@typing.overload
def gettotalforce(physreg: int, EorH: spylizard.expression, epsilonormu: spylizard.expression, extraintegrationorder: int = 0) -> typing.List[float]:
    pass
@typing.overload
def gettotalforce(physreg: int, meshdeform: spylizard.expression, EorH: spylizard.expression, epsilonormu: spylizard.expression, extraintegrationorder: int = 0) -> typing.List[float]:
    pass
def getversion() -> int:
    pass
def getversionname() -> str:
    pass
def grad(input: spylizard.expression) -> spylizard.expression:
    pass
def greenlagrangestrain(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def grouptimesteps(filename: str, fileprefix: str, firstint: int, timevals: typing.List[float]) -> None:
    pass
@typing.overload
def grouptimesteps(filename: str, filestogroup: typing.List[str], timevals: typing.List[float]) -> None:
    pass
def ifpositive(condexpr: spylizard.expression, trueexpr: spylizard.expression, falseexpr: spylizard.expression) -> spylizard.expression:
    pass
def initialize() -> None:
    pass
@typing.overload
def integral(physreg: int, meshdeform: spylizard.expression, tointegrate: spylizard.expression, integrationorderdelta: int = 0, blocknumber: int = 0) -> spylizard.integration:
    pass
@typing.overload
def integral(physreg: int, numcoefharms: int, meshdeform: spylizard.expression, tointegrate: spylizard.expression, integrationorderdelta: int = 0, blocknumber: int = 0) -> spylizard.integration:
    pass
@typing.overload
def integral(physreg: int, numcoefharms: int, tointegrate: spylizard.expression, integrationorderdelta: int = 0, blocknumber: int = 0) -> spylizard.integration:
    pass
@typing.overload
def integral(physreg: int, tointegrate: spylizard.expression, integrationorderdelta: int = 0, blocknumber: int = 0) -> spylizard.integration:
    pass
def inverse(input: spylizard.expression) -> spylizard.expression:
    pass
def isavailable() -> bool:
    pass
def isdefined(physreg: int) -> bool:
    pass
def isempty(physreg: int) -> bool:
    pass
def isinside(physregtocheck: int, physreg: int) -> bool:
    pass
def istouching(physregtocheck: int, physreg: int) -> bool:
    pass
def linspace(a: float, b: float, num: int) -> typing.List[float]:
    pass
def loadshape(meshfile: str) -> typing.List[typing.List[spylizard.shape]]:
    pass
def loadvector(filename: str, delimiter: str = ',', sizeincluded: bool = False) -> typing.List[float]:
    pass
def log10(input: spylizard.expression) -> spylizard.expression:
    pass
def logspace(a: float, b: float, num: int, basis: float = 10.0) -> typing.List[float]:
    pass
def makeharmonic(harms: typing.List[int], exprs: typing.List[spylizard.expression]) -> spylizard.expression:
    pass
@typing.overload
def max(a: spylizard.expression, b: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def max(a: spylizard.field, b: spylizard.field) -> spylizard.expression:
    pass
@typing.overload
def max(a: spylizard.parameter, b: spylizard.parameter) -> spylizard.expression:
    pass
@typing.overload
def max(data: typing.List[float]) -> None:
    pass
@typing.overload
def max(data: typing.List[int]) -> None:
    pass
def meshsize(integrationorder: int) -> spylizard.expression:
    pass
@typing.overload
def min(a: spylizard.expression, b: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def min(a: spylizard.field, b: spylizard.field) -> spylizard.expression:
    pass
@typing.overload
def min(a: spylizard.parameter, b: spylizard.parameter) -> spylizard.expression:
    pass
def mod(input: spylizard.expression, modval: float) -> spylizard.expression:
    pass
def moveharmonic(origharms: typing.List[int], destharms: typing.List[int], input: spylizard.expression, numfftharms: int = -1) -> spylizard.expression:
    pass
def norm(arg0: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def normal() -> spylizard.expression:
    pass
@typing.overload
def normal(pointoutofphysreg: int) -> spylizard.expression:
    pass
@typing.overload
def on(physreg: int, coordshift: spylizard.expression, expression: spylizard.expression, errorifnotfound: bool = True) -> spylizard.expression:
    pass
@typing.overload
def on(physreg: int, expression: spylizard.expression, errorifnotfound: bool = True) -> spylizard.expression:
    pass
def orpositive(exprs: typing.List[spylizard.expression]) -> spylizard.expression:
    pass
def periodicitycondition(gamma1: int, gamma2: int, u: spylizard.field, dat1: typing.List[float], dat2: typing.List[float], factor: float, lagmultorder: int) -> typing.List[spylizard.integration]:
    pass
def pow(base: spylizard.expression, exponent: spylizard.expression) -> spylizard.expression:
    pass
def predefinedacousticradiation(dofp: spylizard.expression, tfp: spylizard.expression, soundspeed: spylizard.expression, neperattenuation: spylizard.expression) -> spylizard.expression:
    pass
def predefinedacoustics(dofp: spylizard.expression, tfp: spylizard.expression, soundspeed: spylizard.expression, neperattenuation: spylizard.expression) -> spylizard.expression:
    pass
def predefinedacousticstructureinteraction(dofp: spylizard.expression, tfp: spylizard.expression, dofu: spylizard.expression, tfu: spylizard.expression, soundspeed: spylizard.expression, fluiddensity: spylizard.expression, normal: spylizard.expression, neperattenuation: spylizard.expression, scaling: float = 1.0) -> spylizard.expression:
    pass
def predefinedadvectiondiffusion(doff: spylizard.expression, tff: spylizard.expression, v: spylizard.expression, alpha: spylizard.expression, beta: spylizard.expression, gamma: spylizard.expression, isdivvzero: bool = True) -> spylizard.expression:
    pass
def predefineddiffusion(doff: spylizard.expression, tff: spylizard.expression, alpha: spylizard.expression, beta: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def predefinedelasticity(dofu: spylizard.expression, tfu: spylizard.expression, Eyoung: spylizard.expression, nupoisson: spylizard.expression, myoption: str = '') -> spylizard.expression:
    pass
@typing.overload
def predefinedelasticity(dofu: spylizard.expression, tfu: spylizard.expression, elasticitymatrix: spylizard.expression, myoption: str = '') -> spylizard.expression:
    pass
@typing.overload
def predefinedelasticity(dofu: spylizard.expression, tfu: spylizard.expression, u: spylizard.field, Eyoung: spylizard.expression, nupoisson: spylizard.expression, prestress: spylizard.expression, myoption: str = '') -> spylizard.expression:
    pass
@typing.overload
def predefinedelasticity(dofu: spylizard.expression, tfu: spylizard.expression, u: spylizard.field, elasticitymatrix: spylizard.expression, prestress: spylizard.expression, myoption: str = '') -> spylizard.expression:
    pass
def predefinedelectrostaticforce(input: spylizard.expression, E: spylizard.expression, epsilon: spylizard.expression) -> spylizard.expression:
    pass
def predefinedmagnetostaticforce(input: spylizard.expression, H: spylizard.expression, mu: spylizard.expression) -> spylizard.expression:
    pass
def predefinednavierstokes(dofv: spylizard.expression, tfv: spylizard.expression, v: spylizard.expression, dofp: spylizard.expression, tfp: spylizard.expression, mu: spylizard.expression, rho: spylizard.expression, dtrho: spylizard.expression, gradrho: spylizard.expression, includetimederivs: bool = False, isdensityconstant: bool = True, isviscosityconstant: bool = True) -> spylizard.expression:
    pass
def predefinedstabilization(stabtype: str, delta: spylizard.expression, f: spylizard.expression, v: spylizard.expression, diffusivity: spylizard.expression, residual: spylizard.expression) -> spylizard.expression:
    pass
def predefinedstokes(dofv: spylizard.expression, tfv: spylizard.expression, dofp: spylizard.expression, tfp: spylizard.expression, mu: spylizard.expression, rho: spylizard.expression, dtrho: spylizard.expression, gradrho: spylizard.expression, includetimederivs: bool = False, isdensityconstant: bool = True, isviscosityconstant: bool = True) -> spylizard.expression:
    pass
@typing.overload
def printtotalforce(physreg: int, EorH: spylizard.expression, epsilonormu: spylizard.expression, extraintegrationorder: int = 0) -> typing.List[float]:
    pass
@typing.overload
def printtotalforce(physreg: int, meshdeform: spylizard.expression, EorH: spylizard.expression, epsilonormu: spylizard.expression, extraintegrationorder: int = 0) -> typing.List[float]:
    pass
@typing.overload
def printvector(input: typing.List[bool]) -> None:
    pass
@typing.overload
def printvector(input: typing.List[float]) -> None:
    pass
@typing.overload
def printvector(input: typing.List[int]) -> None:
    pass
def printversion() -> None:
    pass
@typing.overload
def receive(source: int, tag: int, data: typing.List[float]) -> None:
    pass
@typing.overload
def receive(source: int, tag: int, data: typing.List[int]) -> None:
    pass
@typing.overload
def scatter(scatterer: int, toscatter: typing.List[float], fragment: typing.List[float]) -> None:
    pass
@typing.overload
def scatter(scatterer: int, toscatter: typing.List[float], fragment: typing.List[float], fragsizes: typing.List[int]) -> None:
    pass
@typing.overload
def scatter(scatterer: int, toscatter: typing.List[int], fragment: typing.List[int]) -> None:
    pass
@typing.overload
def scatter(scatterer: int, toscatter: typing.List[int], fragment: typing.List[int], fragsizes: typing.List[int]) -> None:
    pass
def scatterwrite(filename: str, xcoords: typing.List[float], ycoords: typing.List[float], zcoords: typing.List[float], compxevals: typing.List[float], compyevals: typing.List[float] = [], compzevals: typing.List[float] = []) -> None:
    pass
def selectall() -> int:
    pass
def selectintersection(physregs: typing.List[int]) -> int:
    pass
def selectunion(physregs: typing.List[int]) -> int:
    pass
@typing.overload
def send(destination: int, tag: int, data: typing.List[float]) -> None:
    pass
@typing.overload
def send(destination: int, tag: int, data: typing.List[int]) -> None:
    pass
def setaxisymmetry() -> None:
    pass
def setdata(invec: vec) -> None:
    pass
def setfundamentalfrequency(f: float) -> None:
    pass
def setmaxnumthreads(mnt: int) -> None:
    pass
def setphysicalregionshift(shiftamount: int) -> None:
    pass
def settime(t: float) -> None:
    pass
@typing.overload
def settimederivative(dtx: vec) -> None:
    pass
@typing.overload
def settimederivative(dtx: vec, dtdtx: vec) -> None:
    pass
def sin(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def solve(A: spylizard.mat, b: typing.List[vec], soltype: str = 'lu') -> typing.List[vec]:
    pass
@typing.overload
def solve(A: spylizard.mat, b: vec, sol: vec, relrestol: float, maxnumit: int, soltype: str = 'bicgstab', precondtype: str = 'sor', verbosity: int = 1, diagscaling: bool = False) -> None:
    pass
@typing.overload
def solve(A: spylizard.mat, b: vec, soltype: str = 'lu', diagscaling: bool = False) -> vec:
    pass
def sqrt(input: spylizard.expression) -> spylizard.expression:
    pass
def strain(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def sum(data: typing.List[float]) -> None:
    pass
@typing.overload
def sum(data: typing.List[int]) -> None:
    pass
def t() -> spylizard.expression:
    pass
def tan(input: spylizard.expression) -> spylizard.expression:
    pass
def tangent() -> spylizard.expression:
    pass
@typing.overload
def tf(input: spylizard.expression) -> spylizard.expression:
    pass
@typing.overload
def tf(input: spylizard.expression, physreg: int) -> spylizard.expression:
    pass
def trace(a: spylizard.expression) -> spylizard.expression:
    pass
def transpose(input: spylizard.expression) -> spylizard.expression:
    pass
def vonmises(stress: spylizard.expression) -> spylizard.expression:
    pass
def writeshapefunctions(filename: str, sftypename: str, elementtypenumber: int, maxorder: int, allorientations: bool = False) -> None:
    pass
def writevector(filename: str, towrite: typing.List[float], delimiter: str = ',', writesize: bool = False) -> None:
    pass
def zienkiewiczzhu(input: spylizard.expression) -> spylizard.expression:
    pass
