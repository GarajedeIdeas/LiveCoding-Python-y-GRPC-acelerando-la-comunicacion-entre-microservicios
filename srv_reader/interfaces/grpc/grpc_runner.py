import time
import grpc
import sys
from concurrent import futures
from service_interfaces.grpc.grpc_service import GrpcService
from service_interfaces.grpc.grpc_constanst import *
from service_interfaces import log

class GrpcRunner:
    def __init__(self, max_grpc_size, beam_pb2, beam_pb2_grpc, port, beam, entity_name='', max_workers=20):
        self.beam_pb2 = beam_pb2
        self.beam_pb2_grpc = beam_pb2_grpc
        self.beam = beam
        self.entity_name = entity_name

        try:         
            self.__server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers),
                options = [
                    ('grpc.max_send_message_length', max_grpc_size),
                    ('grpc.max_receive_message_length', max_grpc_size)
                ]
            )
            
            beam_service = GrpcService(self.beam_pb2, beam, self.entity_name) 
            self.beam_pb2_grpc.add_BeamServicer_to_server(beam_service, self.__server)
            self.__server.add_insecure_port('[::]:' + str(port))
            log.debug(f'GRPC service created on port {port}, with {max_workers} workers.')
        except Exception as e:
            log.error(f'GRPC runner exception: {e}')
            raise e
        
    def run_grpc_service(self):
        self.__server.start()
        self.__server.wait_for_termination()
        log.debug('GPRC service started')