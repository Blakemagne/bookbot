#!/usr/bin/env python3
"""
PDF Transfer Utility for BookBot

This utility helps transfer PDF files from Windows Desktop to WSL environment.
It provides multiple methods for easy PDF management.

Usage:
    python3 pdf_transfer.py --list                    # List available PDFs
    python3 pdf_transfer.py --copy <filename>         # Copy specific PDF
    python3 pdf_transfer.py --copy-all               # Copy all PDFs from Desktop
    python3 pdf_transfer.py --analyze <filename>     # Copy and analyze PDF
"""

import os
import shutil
import argparse
from pathlib import Path

# Windows Desktop path through WSL
WINDOWS_DESKTOP = "/mnt/c/Users/*/Desktop"
LOCAL_PDF_DIR = "pdfs"

def get_windows_desktop_path():
    """
    Finds the Windows Desktop path in WSL environment.
    
    Returns:
        str: Path to Windows Desktop or None if not found
    """
    import glob
    
    # Common Windows user paths including Library subdirectory
    possible_paths = [
        "/mnt/c/Users/*/Desktop",
        "/mnt/c/Users/*/Desktop/Library",
        "/mnt/c/Users/*/Desktop/library", 
        "/mnt/c/Users/*/OneDrive/Desktop",
        "/mnt/c/Users/*/OneDrive/Desktop/Library",
        "/mnt/c/Users/*/OneDrive/Desktop/library",
        "/mnt/c/Users/*/OneDrive - */Desktop",
        "/mnt/c/Users/*/OneDrive - */Desktop/Library",
        "/mnt/c/Users/*/OneDrive - */Desktop/library"
    ]
    
    for pattern in possible_paths:
        matches = glob.glob(pattern)
        if matches:
            return matches[0]  # Return first match
    
    return None

def list_pdfs():
    """
    Lists all PDF files found on Windows Desktop.
    
    Returns:
        list: List of PDF file paths
    """
    desktop_path = get_windows_desktop_path()
    if not desktop_path:
        print("❌ Windows Desktop not found in WSL environment")
        return []
    
    pdf_files = []
    desktop = Path(desktop_path)
    
    if desktop.exists():
        pdf_files = list(desktop.glob("*.pdf"))
        pdf_files.extend(list(desktop.glob("**/*.pdf")))  # Include all subdirectories recursively
    
    return pdf_files

def copy_pdf(pdf_path, destination_dir="pdfs"):
    """
    Copies a PDF file to the local directory.
    
    Args:
        pdf_path (str): Source PDF file path
        destination_dir (str): Destination directory
        
    Returns:
        str: Path to copied file or None if failed
    """
    try:
        # Ensure destination directory exists
        os.makedirs(destination_dir, exist_ok=True)
        
        pdf_path = Path(pdf_path)
        destination = Path(destination_dir) / pdf_path.name
        
        # Copy the file
        shutil.copy2(pdf_path, destination)
        print(f"✅ Copied: {pdf_path.name} -> {destination}")
        
        return str(destination)
        
    except Exception as e:
        print(f"❌ Error copying {pdf_path}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="PDF Transfer Utility for BookBot")
    parser.add_argument("--list", action="store_true", help="List available PDFs on Desktop")
    parser.add_argument("--copy", type=str, help="Copy specific PDF file by name")
    parser.add_argument("--copy-all", action="store_true", help="Copy all PDFs from Desktop")
    parser.add_argument("--analyze", type=str, help="Copy and analyze specific PDF")
    parser.add_argument("--desktop-path", type=str, help="Override Windows Desktop path")
    
    args = parser.parse_args()
    
    if args.desktop_path:
        global WINDOWS_DESKTOP
        WINDOWS_DESKTOP = args.desktop_path
    
    if args.list:
        print("🔍 Scanning Windows Desktop for PDFs...")
        pdfs = list_pdfs()
        
        if pdfs:
            print(f"\n📚 Found {len(pdfs)} PDF(s):")
            for i, pdf in enumerate(pdfs, 1):
                size_mb = pdf.stat().st_size / (1024 * 1024)
                print(f"  {i}. {pdf.name} ({size_mb:.1f} MB)")
        else:
            print("❌ No PDF files found on Desktop")
    
    elif args.copy:
        print(f"📋 Looking for PDF: {args.copy}")
        pdfs = list_pdfs()
        
        # Find matching PDF (case-insensitive)
        matching_pdf = None
        for pdf in pdfs:
            if args.copy.lower() in pdf.name.lower():
                matching_pdf = pdf
                break
        
        if matching_pdf:
            copied_path = copy_pdf(matching_pdf)
            if copied_path:
                print(f"📖 PDF ready for analysis: python3 main.py {copied_path}")
        else:
            print(f"❌ PDF '{args.copy}' not found on Desktop")
            print("💡 Use --list to see available PDFs")
    
    elif args.copy_all:
        print("📋 Copying all PDFs from Desktop...")
        pdfs = list_pdfs()
        
        if pdfs:
            copied_count = 0
            for pdf in pdfs:
                if copy_pdf(pdf):
                    copied_count += 1
            
            print(f"\n✅ Successfully copied {copied_count}/{len(pdfs)} PDFs")
            print(f"📁 PDFs are now in the '{LOCAL_PDF_DIR}' directory")
        else:
            print("❌ No PDF files found to copy")
    
    elif args.analyze:
        print(f"📋 Copying and analyzing: {args.analyze}")
        pdfs = list_pdfs()
        
        # Find matching PDF
        matching_pdf = None
        for pdf in pdfs:
            if args.analyze.lower() in pdf.name.lower():
                matching_pdf = pdf
                break
        
        if matching_pdf:
            copied_path = copy_pdf(matching_pdf)
            if copied_path:
                print(f"\n🚀 Running analysis...")
                os.system(f"python3 main.py {copied_path}")
        else:
            print(f"❌ PDF '{args.analyze}' not found on Desktop")
    
    else:
        parser.print_help()
        print("\n💡 Quick Examples:")
        print("  python3 pdf_transfer.py --list")
        print("  python3 pdf_transfer.py --copy 'learning python'")
        print("  python3 pdf_transfer.py --analyze 'docker'")

if __name__ == "__main__":
    main()