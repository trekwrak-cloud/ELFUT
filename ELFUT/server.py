import http.server
import socketserver
import webbrowser
import socket
import time

# --- AYARLAR ---
PORT = 8000
FILENAME = "elfut_elite.html"  # HTML dosyanın adı

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Konsolu kirletmemek için her isteği loglamaz, sadece kritik olanları yazar
        pass

def start_server():
    my_ip = get_ip()
    url = f"http://localhost:{PORT}"
    
    print("\n" + "="*50)
    print("      --- ELFUT ROBOTIC OPERATIONAL SYSTEM ---")
    print("="*50)
    print(f"[BİLGİ] Sunucu Hazırlanıyor...")
    time.sleep(0.5)
    
    print(f"[OK]    Yerel Adres: {url}")
    print(f"[OK]    Ağ Adresi:   http://{my_ip}:{PORT}")
    print(f"[BİLGİ] Arayüz Dosyası: {FILENAME}")
    print("-" * 50)
    print(f"[SİSTEM] HTTP SUNUCUSU AKTİF! Tarayıcı başlatılıyor...")
    print("-" * 50)
    print("Kapatmak için: CTRL + C")

    # Tarayıcıyı otomatik aç
    webbrowser.open(url)

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[KAPANIŞ] Sunucu güvenli bir şekilde durduruldu.")
            httpd.shutdown()

if __name__ == "__main__":
    start_server()