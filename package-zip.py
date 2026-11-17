import os
import zipfile
import sys

def package_app():
    build_dir = 'build'
    zip_filename = 'MCCOD.zip'

    if not os.path.exists(build_dir):
        print(f"Error: '{build_dir}' directory not found. Please run 'npm run build' first.")
        sys.exit(1)

    index_html = os.path.join(build_dir, 'index.html')
    manifest_webapp = os.path.join(build_dir, 'manifest.webapp')

    if not os.path.exists(index_html):
        print("Error: 'build/index.html' not found! Build may be incomplete.")
        sys.exit(1)

    if not os.path.exists(manifest_webapp):
        print("Error: 'build/manifest.webapp' not found!")
        sys.exit(1)

    print(f"Packaging '{build_dir}' into '{zip_filename}' for DHIS2...")

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(build_dir):
            for file in files:
                # Exclude existing zip files and map files to keep zip clean
                if file.endswith('.zip') or file.endswith('.map'):
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, build_dir)
                # Ensure Linux/POSIX standard forward slashes for DHIS2/Tomcat
                arcname = rel_path.replace('\\', '/')
                zipf.write(full_path, arcname)

    print(f"Successfully created {zip_filename} ({os.path.getsize(zip_filename):,} bytes). Ready for DHIS2 App Management upload!")

if __name__ == '__main__':
    package_app()
