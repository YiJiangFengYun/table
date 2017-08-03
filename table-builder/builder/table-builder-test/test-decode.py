import append_custom_paths
from output.python import table_pb2
from output.python import packet_id_allocate_pb2

print(append_custom_paths)

binary_path = "output/packet id allocate"
file = open(binary_path, "rb")
binary = file.read()
file.close()
wrapper = table_pb2.Wrapper()
wrapper.ParseFromString(binary)
packet_id_allocate = None
for content in wrapper.contents:
    if content.Is(packet_id_allocate_pb2.Packet_id_allocate.DESCRIPTOR):
        packet_id_allocate = packet_id_allocate_pb2.Packet_id_allocate()
        content.Unpack(packet_id_allocate)

print(packet_id_allocate)
