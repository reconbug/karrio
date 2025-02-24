SCHEMAS=./schemas
LIB_MODULES=./amazon_mws_lib
find "${LIB_MODULES}" -name "*.py" -exec rm -r {} \;
touch "${LIB_MODULES}/__init__.py"

quicktype () {
    echo "Generating $1..."
    docker run -it -v $PWD:/app -e SCHEMAS=/app/schemas -e LIB_MODULES=/app/amazon_mws_lib \
    karrio/tools /quicktype/script/quicktype --no-uuids --no-date-times --no-enums --src-lang json --lang jstruct \
    --no-nice-property-names --all-properties-optional $@
}

quicktype --src="${SCHEMAS}/create_shipment_request.json" --out="${LIB_MODULES}/create_shipment_request.py"
quicktype --src="${SCHEMAS}/create_shipment_response.json" --out="${LIB_MODULES}/create_shipment_response.py"
quicktype --src="${SCHEMAS}/error_response.json" --out="${LIB_MODULES}/error_response.py"
quicktype --src="${SCHEMAS}/purchase_label_request.json" --out="${LIB_MODULES}/purchase_label_request.py"
quicktype --src="${SCHEMAS}/purchase_label_response.json" --out="${LIB_MODULES}/purchase_label_response.py"
quicktype --src="${SCHEMAS}/purchase_shipment_request.json" --out="${LIB_MODULES}/purchase_shipment_request.py"
quicktype --src="${SCHEMAS}/purchase_shipment_response.json" --out="${LIB_MODULES}/purchase_shipment_response.py"
quicktype --src="${SCHEMAS}/rate_request.json" --out="${LIB_MODULES}/rate_request.py"
quicktype --src="${SCHEMAS}/rate_response.json" --out="${LIB_MODULES}/rate_response.py"
quicktype --src="${SCHEMAS}/shipping_label.json" --out="${LIB_MODULES}/shipping_label.py"
quicktype --src="${SCHEMAS}/tracking_response.json" --out="${LIB_MODULES}/tracking_response.py"
