#!/usr/bin/env python3
"""Strip embedded page images from CattoEPUB EPUB — keep only OCR text"""
import zipfile, io, re, sys, os

def strip_images(input_path, output_path=None):
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = base + ' (text-only)' + ext

    z_in = zipfile.ZipFile(input_path, 'r')
    buf = io.BytesIO()
    z_out = zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED)

    # Find page image files to skip (img0.jpg, img1.png, etc.)
    img_files = set(n for n in z_in.namelist() if re.match(r'OEBPS/img\d+\.(jpg|jpeg|png|webp)$', n))
    
    skipped = 0
    fixed_pages = 0

    for item in z_in.infolist():
        data = z_in.read(item.filename)

        # Skip page image files (but keep cover)
        if item.filename in img_files:
            skipped += 1
            continue

        # Remove <img> tags and their wrapper divs from XHTML pages
        if item.filename.endswith('.xhtml') and b'page-img' in data:
            text = data.decode('utf-8')
            # Remove the whole div containing the page image
            text = re.sub(r'<div[^>]*>\s*<img[^>]*class="page-img"[^>]*/>\s*</div>', '', text)
            data = text.encode('utf-8')
            fixed_pages += 1

        # Remove image items from content.opf manifest
        if item.filename.endswith('content.opf'):
            text = data.decode('utf-8')
            text = re.sub(r'<item\s+id="img\d+"[^/]*/>\n?', '', text)
            data = text.encode('utf-8')

        # Write with same compression as mimetype
        if item.filename == 'mimetype':
            z_out.writestr(item, data, compress_type=zipfile.ZIP_STORED)
        else:
            z_out.writestr(item, data, compress_type=zipfile.ZIP_DEFLATED)

    z_out.close()
    
    with open(output_path, 'wb') as f:
        f.write(buf.getvalue())

    orig_size = os.path.getsize(input_path)
    new_size = os.path.getsize(output_path)
    print(f'✅ Done!')
    print(f'   Removed {skipped} images, fixed {fixed_pages} pages')
    print(f'   {orig_size:,} bytes → {new_size:,} bytes ({100-new_size*100//orig_size}% smaller)')
    print(f'   Saved: {output_path}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 fix_epub.py <input.epub> [output.epub]')
        sys.exit(1)
    strip_images(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
