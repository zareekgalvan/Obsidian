from Structs import *
import pprint
from SemanticCube import *

# Tabla de Variables
scope = ['global']
lastType = []
varTable = {}
varTable[scope[len(scope)-1]] = {}

# Directorio de procedimientos
dirProcedures = {}

# Pilas
pilaOp = Stack()
pilaOptr = Stack()
pSaltos = Stack()
pReturnSaltos = Stack()
pTypes = Stack()

# Temporales
iTempCount = 1
tempTable = {}

# Lista de operandos
ands = ['&&', '||']
comps = ['<', '>', '>=', '<=', '==', '!=']
sums = ['+', '-']
mults = ['*', '/', '%']

from Quadruples import *
from Memory import *

# Cuadruplos
quadruples = Quadruples()
paramCount = 0
returnCount = 0
lastFuncCallScope = ""

# Memoria
mem = Memory()

# Debbuging mode
debug = 'on'