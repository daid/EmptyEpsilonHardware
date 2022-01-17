import ustruct
import usocket
from machine import Pin
import esp

ROOT_LAYER = "HH12sHI16s"
FRAME_LAYER = "HI64sBHBBH"
DMP_LAYER = "HBBHHH"
FMT = ">" + ROOT_LAYER + FRAME_LAYER + DMP_LAYER

def decodeE131(packet):
    if len(packet) < 125:
        return None
    preamble_size, postamble_size, packet_identifier, root_flags_length, root_vector, sender_id, \
    frame_flags_Length, frame_vector, source_name, priority, synchronization_address, sequence_number, options, universe, \
    dpm_flags_length, dpm_vector, address_data_type, first_property_address, addres_increment, property_count \
     = ustruct.unpack(FMT, packet[:125])
    if preamble_size != 0x10 or postamble_size != 0x00:
        return None
    if packet_identifier != b'\x41\x53\x43\x2d\x45\x31\x2e\x31\x37\x00\x00\x00':
        return None
    if root_vector != 4 or frame_vector != 2 or dpm_vector != 2 or address_data_type != 0xA1:
        return None
    # There are a few more things that could be checked, like lengths and stuff.
    # But at this point we should be pretty sure this is DMX data.
    return packet[126:]


s = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM, usocket.IPPROTO_IP)
s.bind(('', 5568))

pin = Pin(2, Pin.OUT)
# Turn off 150 neopixels
esp.neopixel_write(pin, b'\x00\x00\x00' * 150, True)

while True:
    data, client = s.recvfrom(2048)
    data = decodeE131(data)
    if data is not None:
        esp.neopixel_write(pin, data, True)
