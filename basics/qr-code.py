from qrcode.main import QRCode


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = QRCode(box_size=size, border=padding)

    def create_qr(self, location: str, fg: str, bg: str):
        self.qr.add_data('www.test.com')  # encode data

        try:
            img = self.qr.make_image(fill_color=fg, back_color=bg)
            img.save(location)
            print('QR Code generated')
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    qr = MyQR(40, 1)
    qr.create_qr('my_qr.png', 'black', 'white')
