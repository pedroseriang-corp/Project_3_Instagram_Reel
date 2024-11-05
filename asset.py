import pygame  # Mengimpor modul pygame
import time

# Inisialisasi pygame
pygame.init()

# Menentukan ukuran layar tampilan
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Definisi warna yang akan digunakan
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Warna biru muda untuk setiap huruf

# Pengaturan font dan ukuran teks
font_size = 30
font = pygame.font.Font(None, font_size)

# Daftar lirik yang akan ditampilkan secara bergantian
lyrics = [
    "Where d'you wanna go?",
    "How much you wanna risk?",
    "I'm not lookin' for somebody with some superhuman gifts",
    "Some superhero",
    "some fairytale bliss",
    "Just something I can turn to, somebody I can kiss",
    "I want something just like this",
]

# Membuat clock untuk mengatur frame rate (FPS)
clock = pygame.time.Clock()

# Fungsi untuk menampilkan teks dengan efek fade in (muncul perlahan) dan fade out (menghilang perlahan)
def display_text(text, fade_in_duration=1, fade_out_duration=1):
    # Mulai dengan transparansi alpha 0 (tidak terlihat)
    alpha = 0
    # Render setiap huruf menjadi surface yang dapat ditampilkan di layar
    letter_surfaces = [font.render(char, True, LIGHT_BLUE) for char in text]
    total_text_width = sum(letter.get_width() for letter in letter_surfaces)
    
    # Mendapatkan posisi awal teks sehingga berada di tengah layar
    start_x = (screen_width - total_text_width) // 2
    y_pos = screen_height // 2

    # Fade In (Muncul perlahan)
    for _ in range(fade_in_duration * 60):  # 60 FPS
        # Memeriksa jika pengguna menekan tombol "QUIT" untuk keluar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Meningkatkan nilai alpha untuk membuat teks lebih terlihat
        alpha += 255 / (fade_in_duration * 60)
        alpha = min(alpha, 255)  # Pastikan alpha tidak melebihi 255
        screen.fill(BLACK)  # Mengisi layar dengan warna hitam
        
        # Menampilkan setiap huruf dengan posisi yang sesuai dan transparansi yang sama
        x_pos = start_x
        for letter in letter_surfaces:
            letter.set_alpha(alpha)
            screen.blit(letter, (x_pos, y_pos))
            x_pos += letter.get_width()  # Geser posisi x untuk huruf berikutnya
        
        pygame.display.flip()  # Memperbarui tampilan layar
        clock.tick(60)  # Menunggu sesuai FPS

    # Menunggu sejenak agar teks dapat terlihat jelas sebelum menghilang
    pygame.time.wait(1000)

    # Fade Out (Menghilang perlahan)
    for _ in range(fade_out_duration * 60):  # 60 FPS
        # Memeriksa event untuk keluar dari aplikasi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Mengurangi nilai alpha untuk membuat teks semakin transparan
        alpha -= 255 / (fade_out_duration * 60)
        alpha = max(alpha, 0)  # Pastikan alpha tidak kurang dari 0
        screen.fill(BLACK)  # Mengisi layar dengan warna hitam

        # Menampilkan setiap huruf dengan posisi yang sesuai dan transparansi yang sama
        x_pos = start_x
        for letter in letter_surfaces:
            letter.set_alpha(alpha)
            screen.blit(letter, (x_pos, y_pos))
            x_pos += letter.get_width()  # Geser posisi x untuk huruf berikutnya

        pygame.display.flip()  # Memperbarui tampilan layar
        clock.tick(60)  # Menunggu sesuai FPS

# Fungsi utama untuk menampilkan setiap baris lirik dengan efek fade in dan fade out
def show_lyrics():
    running = True  # Menandakan program sedang berjalan
    for line in lyrics:  # Iterasi melalui setiap baris lirik
        if not running:  # Jika sudah tidak berjalan, keluar dari loop
            break
        for event in pygame.event.get():  # Mengecek event "QUIT" di awal setiap lirik
            if event.type == pygame.QUIT:
                running = False  # Menghentikan loop jika pengguna keluar
        
        # Menampilkan lirik dengan efek fade in dan fade out
        display_text(line)

    pygame.quit()  # Menutup jendela Pygame setelah loop selesai

# Menjalankan program jika file ini dieksekusi langsung
if __name__ == "__main__":
    show_lyrics()
