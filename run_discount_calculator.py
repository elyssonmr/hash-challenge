import grpc

from discount_calculator.generated_grpc import discount_calculator_pb2_grpc

from concurrent.futures import ThreadPoolExecutor

from discount_calculator.services import DiscountService


if __name__ == "__main__":
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    discount_calculator_pb2_grpc.add_DiscountCalculatorServicer_to_server(
        DiscountService(),
        server
    )
    server.add_insecure_port('[::]:51000')
    server.start()
    print('Server Started at port 51000')
    server.wait_for_termination()
