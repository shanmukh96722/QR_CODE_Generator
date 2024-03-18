import streamlit as st
import qrcode
from io import BytesIO

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    st.title("QR Code Generator")

    url = st.text_input("Enter the URL:")
    if st.button("Generate QR Code"):
        if url:
            qr_img = generate_qr_code(url)
            # Convert PIL image to bytes-like object
            img_bytes = BytesIO()
            qr_img.save(img_bytes, format='PNG')
            st.image(img_bytes, caption='QR Code', use_column_width=False)
        else:
            st.error("Please enter a URL.")

if __name__ == "__main__":
    main()
