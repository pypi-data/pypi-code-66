import grpc

import communication_pb2
import communication_pb2_grpc


def handle_sync_state(stub: communication_pb2_grpc.CommunicationStub):
    response = stub.SyncState(communication_pb2.State(status="client good"))
    print(response)


def start():
    with grpc.insecure_channel("localhost:50051") as channel:
        channel_ready = grpc.channel_ready_future(channel)
        print("Waiting for channel ready...")
        channel_ready.result()
        print("Channel is ready")
        stub = communication_pb2_grpc.CommunicationStub(channel)
        handle_sync_state(stub)


if __name__ == "__main__":
    start()
