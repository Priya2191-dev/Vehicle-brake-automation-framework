import can

bus = can.interface.Bus(channel="virtual", bustype="virtual")

message = can.Message(
    arbitration_id=0x101,
    data=[int(vehicle.speed), vehicle.brake_pressure, int(vehicle.abs_active)],
    is_extended_id=False
)

bus.send(message)

print("CAN Message Sent:", message)
