# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sales_record_pb2 as sales__record__pb2


class SalesRecordStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PingSalesRecords = channel.unary_unary(
                '/SalesRecord/PingSalesRecords',
                request_serializer=sales__record__pb2.EmptyMesssage.SerializeToString,
                response_deserializer=sales__record__pb2.SalesRecordPingResponse.FromString,
                )
        self.SendSalesRecords = channel.unary_unary(
                '/SalesRecord/SendSalesRecords',
                request_serializer=sales__record__pb2.SalesRecordRequest.SerializeToString,
                response_deserializer=sales__record__pb2.SalesRecordResponse.FromString,
                )
        self.SendSalesPayload = channel.unary_unary(
                '/SalesRecord/SendSalesPayload',
                request_serializer=sales__record__pb2.PayloadRequest.SerializeToString,
                response_deserializer=sales__record__pb2.SalesRecordResponse.FromString,
                )
        self.SendSalesRecordsStream = channel.stream_unary(
                '/SalesRecord/SendSalesRecordsStream',
                request_serializer=sales__record__pb2.SalesRecordRequest.SerializeToString,
                response_deserializer=sales__record__pb2.SalesRecordResponse.FromString,
                )


class SalesRecordServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PingSalesRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSalesRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSalesPayload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSalesRecordsStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SalesRecordServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PingSalesRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.PingSalesRecords,
                    request_deserializer=sales__record__pb2.EmptyMesssage.FromString,
                    response_serializer=sales__record__pb2.SalesRecordPingResponse.SerializeToString,
            ),
            'SendSalesRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSalesRecords,
                    request_deserializer=sales__record__pb2.SalesRecordRequest.FromString,
                    response_serializer=sales__record__pb2.SalesRecordResponse.SerializeToString,
            ),
            'SendSalesPayload': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSalesPayload,
                    request_deserializer=sales__record__pb2.PayloadRequest.FromString,
                    response_serializer=sales__record__pb2.SalesRecordResponse.SerializeToString,
            ),
            'SendSalesRecordsStream': grpc.stream_unary_rpc_method_handler(
                    servicer.SendSalesRecordsStream,
                    request_deserializer=sales__record__pb2.SalesRecordRequest.FromString,
                    response_serializer=sales__record__pb2.SalesRecordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SalesRecord', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SalesRecord(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PingSalesRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SalesRecord/PingSalesRecords',
            sales__record__pb2.EmptyMesssage.SerializeToString,
            sales__record__pb2.SalesRecordPingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSalesRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SalesRecord/SendSalesRecords',
            sales__record__pb2.SalesRecordRequest.SerializeToString,
            sales__record__pb2.SalesRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSalesPayload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SalesRecord/SendSalesPayload',
            sales__record__pb2.PayloadRequest.SerializeToString,
            sales__record__pb2.SalesRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSalesRecordsStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/SalesRecord/SendSalesRecordsStream',
            sales__record__pb2.SalesRecordRequest.SerializeToString,
            sales__record__pb2.SalesRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
