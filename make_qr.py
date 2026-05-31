import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

# --- 👇 決定したURL ---
target_url = "https://growvia-official.netlify.app"
# --------------------

# QRコードの設定
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
qr.add_data(target_url)
qr.make(fit=True)

# 色の設定（白ドット・背景透明）
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(
        front_color=(255, 255, 255, 255), # 白
        back_color=(0, 0, 0, 0)      # 透明
    )
)

# 保存
file_name = "growvia_qr_white.png"
img.save(file_name, "PNG")

print(f"✅ 完成！URL: {target_url} のQRコードを作成しました。")