# Laptop Troubleshooting Guide

## Common Issues and Solutions

This guide covers the most common laptop issues and their solutions. For issues not covered here, contact IT support at extension 200.

## Performance Issues

### Slow Performance

**Symptoms:**
- Applications take long to load
- System freezes frequently
- High CPU usage

**Solutions:**

1. **Check Task Manager**
   - Press Ctrl+Shift+Esc
   - Identify resource-intensive applications
   - Close unnecessary applications

2. **Restart Your Laptop**
   - Saves all work
   - Clears temporary files
   - Resets system resources

3. **Check for Malware**
   - Run company antivirus scan
   - Full scan recommended weekly
   - Quarantine any threats found

4. **Free Up Disk Space**
   - Delete temporary files: `%temp%`
   - Empty recycle bin
   - Uninstall unused applications

5. **Update System**
   - Windows Update: Settings > Update & Security
   - Install all critical updates
   - Restart after updates

### Overheating

**Symptoms:**
- Fan runs constantly
- Laptop feels hot to touch
- System shuts down unexpectedly

**Solutions:**

1. **Check Ventilation**
   - Ensure vents are not blocked
   - Use on hard surface (not bed/couch)
   - Clean dust from vents with compressed air

2. **Close Resource-Intensive Apps**
   - Check Task Manager
   - Close high CPU usage applications
   - Avoid running multiple heavy apps

3. **Update Drivers**
   - Update graphics drivers
   - Update chipset drivers
   - Download from manufacturer website

## Network Issues

### No Internet Connection

**Symptoms:**
- Cannot access websites
- Network icon shows disconnected
- VPN won't connect

**Solutions:**

1. **Check Wi-Fi**
   - Verify Wi-Fi is enabled
   - Check if connected to correct network
   - Forget and reconnect to network

2. **Check Ethernet**
   - Verify cable is connected
   - Check cable for damage
   - Try different port on router

3. **Restart Network Adapter**
   - Open Command Prompt as admin
   - Run: `ipconfig /release`
   - Run: `ipconfig /renew`
   - Run: `ipconfig /flushdns`

4. **Check VPN**
   - Disconnect VPN
   - Test internet without VPN
   - Reconnect VPN if needed

### Slow Internet

**Symptoms:**
- Websites load slowly
- Downloads take long time
- Video buffering

**Solutions:**

1. **Check Speed**
   - Run speed test: speedtest.net
   - Minimum required: 10 Mbps
   - Contact ISP if below minimum

2. **Check Network Usage**
   - Close other devices on network
   - Stop large downloads
   - Check for background updates

3. **Restart Router**
   - Unplug router for 30 seconds
   - Plug back in
   - Wait for full restart

## Display Issues

### Screen Not Working

**Symptoms:**
- Black screen
- Flickering screen
- Distorted display

**Solutions:**

1. **Check Brightness**
   - Increase brightness using function keys
   - Check if brightness is at minimum

2. **External Display**
   - Connect to external monitor
   - Press Windows+P to switch display mode
   - Test if external display works

3. **Update Graphics Drivers**
   - Device Manager > Display Adapters
   - Right-click graphics card > Update driver
   - Restart after update

4. **Safe Mode**
   - Restart in Safe Mode
   - If screen works in Safe Mode, driver issue
   - Uninstall recent driver updates

## Audio Issues

### No Sound

**Symptoms:**
- No audio from speakers
- Audio not working with headphones

**Solutions:**

1. **Check Volume**
   - Click volume icon in taskbar
   - Ensure volume is not muted
   - Increase volume

2. **Check Audio Device**
   - Right-click volume icon > Open Sound Settings
   - Select correct output device
   - Test audio

3. **Update Audio Drivers**
   - Device Manager > Sound, video and game controllers
   - Right-click audio device > Update driver
   - Restart after update

4. **Restart Audio Service**
   - Run `services.msc`
   - Find Windows Audio
   - Restart the service

## Battery Issues

### Battery Not Charging

**Symptoms:**
- Battery percentage not increasing
- Laptop only works when plugged in
- Battery not detected

**Solutions:**

1. **Check Power Adapter**
   - Verify adapter is connected properly
   - Check for damage to cable
   - Try different power outlet

2. **Check Battery Health**
   - Settings > System > Battery
   - View battery usage report
   - Replace if health below 50%

3. **Update BIOS**
   - Check manufacturer website
   - Download latest BIOS update
   - Follow installation instructions carefully

### Battery Draining Quickly

**Symptoms:**
- Battery lasts less than 2 hours
- Sudden drops in percentage

**Solutions:**

1. **Check Power Settings**
   - Settings > System > Power & sleep
   - Select "Power saver" mode
   - Reduce screen brightness

2. **Close Background Apps**
   - Check Task Manager
   - Close unnecessary applications
   - Disable startup apps

3. **Check Battery Usage**
   - Settings > System > Battery
   - Identify battery-draining apps
   - Close or uninstall heavy apps

## Application Issues

### Application Won't Open

**Symptoms:**
- Application crashes on launch
- Application freezes
- Application not responding

**Solutions:**

1. **Restart Application**
   - Close application completely
   - Wait 10 seconds
   - Reopen application

2. **Run as Administrator**
   - Right-click application
   - Run as administrator
   - Confirm with UAC prompt

3. **Reinstall Application**
   - Uninstall application
   - Download latest version
   - Reinstall application

4. **Check for Updates**
   - Check application settings for updates
   - Install latest version
   - Restart after update

### Application Crashes

**Symptoms:**
- Application closes unexpectedly
- Error messages appear
- Data loss possible

**Solutions:**

1. **Check Error Logs**
   - Event Viewer > Windows Logs > Application
   - Look for error messages
   - Note error codes

2. **Update Application**
   - Check for updates
   - Install latest version
   - Check patch notes for crash fixes

3. **Clear Application Cache**
   - Navigate to application folder
   - Delete cache folder
   - Restart application

## Hardware Issues

### Keyboard Not Working

**Symptoms:**
- Keys not responding
- Wrong characters typed
- Keyboard not detected

**Solutions:**

1. **Check Keyboard Connection**
   - For external keyboards, check USB connection
   - Try different USB port
   - Test with another keyboard

2. **Restart Laptop**
   - Save all work
   - Restart laptop
   - Test keyboard after restart

3. **Update Keyboard Drivers**
   - Device Manager > Keyboards
   - Right-click keyboard > Update driver
   - Restart after update

### Touchpad Not Working

**Symptoms:**
- Cursor doesn't move
- Clicks not registering
- Gestures not working

**Solutions:**

1. **Enable Touchpad**
   - Check if touchpad is disabled
   - Use function key to enable
   - Check settings > Devices > Touchpad

2. **Update Drivers**
   - Device Manager > Mice and other pointing devices
   - Right-click touchpad > Update driver
   - Restart after update

3. **Check Settings**
   - Settings > Devices > Touchpad
   - Ensure touchpad is enabled
   - Adjust sensitivity if needed

## When to Contact IT

Contact IT support (extension 200) for:

- Hardware failure (physical damage)
- Data recovery needs
- Security incidents
- Issues not resolved by above steps
- System errors with error codes

### Information to Provide

When contacting IT, have ready:
- Laptop model and serial number
- Operating system version
- Detailed description of issue
- Steps already taken to resolve
- Error messages (if any)

---

Last updated: March 2024
