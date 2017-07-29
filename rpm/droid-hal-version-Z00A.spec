# rpm_device is the name of the ported device
%define rpm_device Z00A
# rpm_vendor is used in the rpm space
%define rpm_vendor asus

# Manufacturer and device name to be shown in the UI
%define vendor_pretty ASUS
%define device_pretty Zenfone 2

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator
%define have_led

%define device_target_cpu i486

%include droid-hal-version/droid-hal-version.inc
