import qrcode

def main():
     # Data to be encoded
    data = "https://jenga.github.io/shiny-spoon/"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image
    img.save("qr_code.png")


if __name__ == "__main__":
    main()
