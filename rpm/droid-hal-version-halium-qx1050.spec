# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device halium-qx1050
%define vendor fxtec

# Manufacturer and device name to be shown in UI
%define vendor_pretty FxTec
%define device_pretty Pro1-X

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1

%define native_build 1

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

