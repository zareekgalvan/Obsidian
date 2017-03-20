from Structs import *
import pprint

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
pTypes = Stack()

# Temporales
iTempCount = 1
tempTable = {}

# Lista de operandos
ands = ['&&', '||']
comps = ['<', '>', '>=', '<=', '==', '!=']
sums = ['+', '-']
mults = ['*', '/', '%']