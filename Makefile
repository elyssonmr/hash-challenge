generate_python_proto:
	@python -m grpc_tools.protoc -Iprotos --python_out=discount_calculator/grpc --grpc_python_out=discount_calculator/grpc protos/discount_calculator.proto

generate_node_proto:
	@echo "Should generate NodeJS Proto"

run_discount_calculator:
	@echo "Running Discount calculator service"

	@cd discount_calculator && python run_discount_calculator.py

run_product_list:
	@echo "Should run products list"


setup:
	@echo "Should setup create both images"

setup_install_docker:
	@echo "Download both images and run the services using docker-compose"
