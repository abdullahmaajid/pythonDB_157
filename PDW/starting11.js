// Fungsi untuk mengatur efek paralaks pada lapisan latar belakang
window.addEventListener('scroll', function() {
    let scrollPosition = window.pageYOffset; // Mendapatkan posisi scroll vertikal
    let backgroundLayer = document.querySelector('.background-layer');
    backgroundLayer.style.backgroundPositionY = -scrollPosition * 0.5 + 'px'; // Mengatur background-position berdasarkan posisi scroll
});

// Fungsi untuk memberikan efek animasi saat memperbesar gambar pemain dan informasi pemain saat cursor hover
document.querySelectorAll('.player-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.querySelector('img').style.transform = 'scale(1.1)'; // Memperbesar gambar saat hover
        this.querySelector('.player-info').style.transform = 'scale(1.1)'; // Memperbesar informasi pemain saat hover
    });
    card.addEventListener('mouseleave', function() {
        this.querySelector('img').style.transform = 'scale(1)'; // Mengembalikan ukuran gambar ke ukuran semula saat keluar dari hover
        this.querySelector('.player-info').style.transform = 'scale(1)'; // Mengembalikan ukuran informasi pemain ke ukuran semula saat keluar dari hover
    });
});

