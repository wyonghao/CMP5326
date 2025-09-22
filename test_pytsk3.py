#!/usr/bin/env python3
"""
Simple test script to verify pytsk3 installation and basic functionality.
"""

import re
import sys

def test_pytsk3_import():
    """Test if pytsk3 can be imported successfully."""
    try:
        import pytsk3
        print("✓ pytsk3 imported successfully")
        print(f"  Version: {pytsk3.TSK_VERSION_STR}")
        return True
    except ImportError as e:
        print(f"✗ Failed to import pytsk3: {e}")
        return False

def test_regex_functionality():
    """Test basic regex functionality for forensic pattern matching."""
    try:
        # Test email pattern matching (common in forensics)
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        test_text = "Found emails: john.doe@example.com and admin@forensics.lab"
        
        emails = re.findall(email_pattern, test_text)
        
        if len(emails) == 2:
            print("✓ Regex functionality working correctly")
            print(f"  Found emails: {emails}")
            return True
        else:
            print(f"✗ Regex test failed - expected 2 emails, found {len(emails)}")
            return False
    except Exception as e:
        print(f"✗ Regex test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing Digital Forensics Environment Setup...")
    print("=" * 50)
    
    pytsk3_ok = test_pytsk3_import()
    regex_ok = test_regex_functionality()
    
    print("=" * 50)
    
    if pytsk3_ok and regex_ok:
        print("🎉 All tests passed! Your environment is ready for digital forensics work.")
        return 0
    else:
        print("❌ Some tests failed. Please check your installation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())