SCHEMAS=./schemas
LIB_MODULES=./canpar_lib
find "${LIB_MODULES}" -name "*.py" -exec rm -r {} \;
touch "${LIB_MODULES}/__init__.py"

generateDS --no-namespace-defs -o "${LIB_MODULES}/CanparAddonsService.py" "${SCHEMAS}/CanparAddonsService.xsd"
generateDS --no-namespace-defs -o "${LIB_MODULES}/CanparRatingService.py" "${SCHEMAS}/CanparRatingService.xsd"
generateDS --no-namespace-defs -o "${LIB_MODULES}/CanshipBusinessService.py" "${SCHEMAS}/CanshipBusinessService.xsd"