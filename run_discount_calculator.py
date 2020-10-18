import grpc

from discount_calculator.generated_grpc import discount_calculator_pb2_grpc

from concurrent.futures import ThreadPoolExecutor

from discount_calculator.handlers import DiscountService

from pymongo import MongoClient


def setup_db_client():
    return MongoClient()


def setup_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    db_client = setup_db_client()
    discount_calculator_pb2_grpc.add_DiscountCalculatorServicer_to_server(
        DiscountService(db_client),
        server
    )
    server.add_insecure_port('[::]:51000')

    return server

if __name__ == "__main__":
    
    server.start()
    print('Server Started at port 51000')
    server.wait_for_termination()
