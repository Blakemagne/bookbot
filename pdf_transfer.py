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

def get_windows_desktop_paths():
    """
    Finds all possible Windows Desktop paths in WSL environment.
    
    Returns:
        list: List of all valid desktop paths found
    """
    import glob
    import os
    
    # Get actual username from environment or system
    username = os.environ.get('USER', '*')
    
    # Base patterns for different OneDrive configurations
    base_patterns = [
        f"/mnt/c/Users/{username}/Desktop",
        f"/mnt/c/Users/{username}/OneDrive/Desktop", 
        f"/mnt/c/Users/{username}/OneDrive - */Desktop",
        "/mnt/c/Users/*/Desktop",
        "/mnt/c/Users/*/OneDrive/Desktop",
        "/mnt/c/Users/*/OneDrive - */Desktop",
        # Additional common patterns
        "/mnt/c/Users/*/Documents/Desktop",
        "/mnt/c/Users/*/Desktop - Shortcut",
    ]
    
    # Subdirectory patterns within desktop locations
    subdirs = ["", "/Library", "/library", "/Books", "/books", "/PDFs", "/pdfs", "/Documents"]
    
    # Generate all combinations
    all_patterns = []
    for base in base_patterns:
        for subdir in subdirs:
            all_patterns.append(base + subdir)
    
    # Find all existing paths
    valid_paths = []
    for pattern in all_patterns:
        try:
            matches = glob.glob(pattern)
            for match in matches:
                if os.path.isdir(match) and match not in valid_paths:
                    valid_paths.append(match)
        except Exception:
            continue  # Skip invalid patterns
    
    return valid_paths

def list_pdfs():
    """
    Lists all PDF files found across all Windows Desktop locations.
    
    Returns:
        list: List of PDF file paths with source directory info
    """
    desktop_paths = get_windows_desktop_paths()
    if not desktop_paths:
        print("❌ No Windows Desktop locations found in WSL environment")
        print("💡 Searched common paths like:")
        print("   /mnt/c/Users/*/Desktop")
        print("   /mnt/c/Users/*/OneDrive/Desktop") 
        print("   /mnt/c/Users/*/OneDrive - */Desktop")
        return []
    
    all_pdf_files = []
    found_locations = []
    
    for desktop_path in desktop_paths:
        desktop = Path(desktop_path)
        if desktop.exists():
            # Find PDFs in this location
            pdf_files = list(desktop.glob("*.pdf"))
            pdf_files.extend(list(desktop.glob("**/*.pdf")))  # Include subdirectories
            
            if pdf_files:
                found_locations.append(f"📁 {desktop_path} ({len(pdf_files)} PDFs)")
                all_pdf_files.extend(pdf_files)
    
    # Print summary of locations searched
    if found_locations:
        print("🔍 Found PDFs in:")
        for location in found_locations:
            print(f"   {location}")
        print()
    
    # Remove duplicates while preserving order
    seen = set()
    unique_pdfs = []
    for pdf in all_pdf_files:
        pdf_key = (pdf.name, pdf.stat().st_size)  # Use name + size as unique key
        if pdf_key not in seen:
            seen.add(pdf_key)
            unique_pdfs.append(pdf)
    
    return unique_pdfs

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
    
    # Manual desktop path override for testing
    if args.desktop_path:
        print(f"🔧 Using custom desktop path: {args.desktop_path}")
        # Test the custom path
        test_path = Path(args.desktop_path)
        if not test_path.exists():
            print(f"❌ Custom path does not exist: {args.desktop_path}")
            return
    
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
                print(f'📖 PDF ready for analysis: python3 main.py "{copied_path}"')
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
                # Use quotes to handle spaces in filename
                os.system(f'python3 main.py "{copied_path}"')
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