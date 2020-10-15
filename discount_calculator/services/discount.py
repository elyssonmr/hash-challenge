from discount_calculator.generated_grpc import discount_calculator_pb2_grpc
from discount_calculator.generated_grpc.discount_calculator_pb2 import (
    CalcDiscountRequest,
    CalcDiscountReply
)


class DiscountService(discount_calculator_pb2_grpc.DiscountCalculator):
    def CalculateDiscount(self, request, context):
        return CalcDiscountReply(calculated_discount=0)
