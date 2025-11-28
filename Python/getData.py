import ctypes
import ctypes.wintypes as wintypes

PROCESS_ALL_ACCESS = 0x1F0FFF

# Windows API 함수 로드
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
OpenProcess = ctypes.windll.kernel32.OpenProcess
CloseHandle = ctypes.windll.kernel32.CloseHandle

def read_memory(pid, address, size=4):
    process = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if not process:
        raise Exception("프로세스를 열 수 없습니다.")

    buffer = ctypes.create_string_buffer(size)
    bytes_read = wintypes.DWORD()

    # 메모리 읽기
    if ReadProcessMemory(process,
                         ctypes.c_void_p(address),
                         buffer,
                         size,
                         ctypes.byref(bytes_read)):
        CloseHandle(process)
        return buffer.raw
    else:
        CloseHandle(process)
        raise Exception("메모리 읽기 실패")

# ==== 실험용 코드 ====

pid = int(input("읽을 PID 입력: "))
addr = int(input("읽을 메모리 주소(hex): "), 16)

data = read_memory(pid, addr, 4)
print("읽어온 RAW 데이터:", data)
print("정수로 해석:", int.from_bytes(data, byteorder='little'))
