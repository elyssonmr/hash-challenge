generate_python_proto:
	@python -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/test.proto

generate_node_proto:
	@echo "Should generate NodeJS Proto"

run_discount_calculator:
	@echo "should run discount calculator"

run_product_list:
	@echo "Should run products list"


setup:
	@echo "Should setup create both images"

setup_install_docker:
	@echo "Download both images and run the services using docker-compose"
