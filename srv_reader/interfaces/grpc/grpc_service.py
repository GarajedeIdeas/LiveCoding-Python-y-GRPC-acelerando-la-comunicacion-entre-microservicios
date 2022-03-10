import sys
from beam_pb2s import beam_pb2_grpc
from service_interfaces.beam_connections_adapter import BeamConnectionsAdapter
from service_interfaces import log

class GrpcService(beam_pb2_grpc.BeamServicer):
    def __init__(self, beam_pb2, beam, entity_name=''):
        self.beam_pb2 = beam_pb2
        self.beam = beam
        self.entity_name = entity_name

        
    def StartTask(self, request, context):
        log.debug('startTask invoked')
        response = self.beam_pb2.StartTaskMessageResponse()
        response.load_uuid = request.load_uuid
        try:
            BeamConnectionsAdapter().executeStartTask(request, self.beam, self.entity_name)

            response.status_code = 200
            response.status_description = 'Start task accepted'
            
        except Exception as e:
            response.status_code = 404
            response.status_description = f'Start task error: {e}'
        
        return response

    def TestConnection(self, request, context):
        log.debug('testConnection invoked')
        response = self.beam_pb2.TestConnectionMessageResponse()

        try:
            result = BeamConnectionsAdapter().executeTestConnection(request, self.beam)
            
            if result :
                response.status_code = 200
                response.status_description = 'Test connection ok'
            else:
                raise Exception('Beam return test connection = false')

        except Exception as e:
            response.status_code = 404
            response.status_description = f'Test connection failed: {e}'

        return response

    def GetData(self, request, context):
        log.debug('testConnection invoked')
        response = self.beam_pb2.GetDataMessageResponse()

        try:
            payload = BeamConnectionsAdapter().executeGetData(request, self.beam, self.entity_name)
            
            response.status_code = 200
            response.status_description = 'Get data ok'
            response.payload = payload

        except Exception as e:
            response.status_code = 404
            response.status_description = f'Get data error: {e}'
            response.payload = ''

        return response