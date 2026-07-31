# Printer Setup Guide

## Overview

This guide provides instructions for setting up and using company printers. All office printers are networked and require proper configuration.

## Available Printers

### Main Office Printers

1. **HP LaserJet Pro MFP M428fdw** (3rd Floor)
   - Location: 3rd Floor, near elevators
   - Features: Print, Scan, Copy, Fax
   - Color: Black and white only
   - IP: 192.168.1.50

2. **Canon imageCLASS MF743Cdw** (2nd Floor)
   - Location: 2nd Floor, break room
   - Features: Print, Scan, Copy
   - Color: Full color
   - IP: 192.168.1.51

3. **Brother HL-L6200DW** (1st Floor)
   - Location: 1st Floor, reception
   - Features: Print only
   - Color: Black and white only
   - IP: 192.168.1.52

## Installation

### Windows

1. **Connect to Network**
   - Ensure laptop is connected to company network
   - VPN must be connected for remote workers

2. **Add Printer**
   - Open Control Panel > Devices and Printers
   - Click "Add a printer"
   - Select "The printer that I want isn't listed"
   - Select "Add a printer using a TCP/IP address or hostname"
   - Enter printer IP address (see above)
   - Uncheck "Query the printer and automatically select the driver"
   - Click Next

3. **Install Driver**
   - Select manufacturer (HP, Canon, or Brother)
   - Select model from list
   - If not listed, download driver from manufacturer website
   - Complete installation

4. **Test Print**
   - Right-click printer > Printer Properties
   - Click "Print Test Page"
   - Verify print quality

### macOS

1. **Add Printer**
   - System Preferences > Printers & Scanners
   - Click "+" to add printer
   - Select "IP" tab
   - Enter printer IP address
   - Protocol: LPD
   - Queue: leave blank
   - Name: Enter descriptive name
   - Location: Enter printer location

2. **Select Driver**
   - Select "Select Software"
   - Choose appropriate driver
   - If not listed, download from manufacturer
   - Click Add

3. **Test Print**
   - Open any document
   - File > Print
   - Select new printer
   - Print test page

## Configuration

### Default Printer

**To set default printer:**
- Windows: Control Panel > Devices and Printers > Right-click printer > Set as default printer
- macOS: System Preferences > Printers & Scanners > Select printer > Set Default Printer

### Duplex Printing

**To enable double-sided printing:**
- Windows: Printer Properties > Device Settings > Duplex Unit > Installed
- macOS: Print dialog > Two-Sided > Long-Edge binding

### Color Printing

**For color printers (Canon only):**
- Windows: Printer Preferences > Color > Automatic
- macOS: Print dialog > Color Mode > Color

**Note:** Color printing should be used sparingly. Black and white is default for all documents.

## Usage

### Printing Documents

1. Open document to print
2. File > Print (or Ctrl+P)
3. Select printer from dropdown
4. Configure settings:
   - Copies: Number of copies
   - Pages: All or specific pages
   - Color: Color or black and white
   - Duplex: Single or double-sided
5. Click Print

### Scanning Documents

**HP LaserJet (3rd Floor):**
1. Place document in automatic feeder or on glass
2. Press Scan button on printer
3. Select "Scan to Computer"
4. Select destination folder
5. Start scan

**Canon (2nd Floor):**
1. Place document on glass
2. Use Canon software on computer
3. Select scan settings
4. Start scan

### Copying Documents

1. Place document on glass or in feeder
2. Press Copy button on printer
3. Select number of copies
4. Start copy

## Troubleshooting

### Printer Offline

**Symptoms:**
- Printer shows as offline
- Print jobs stuck in queue
- Cannot communicate with printer

**Solutions:**

1. **Check Network Connection**
   - Verify printer is powered on
   - Check network cable connection
   - Ping printer IP address

2. **Restart Printer**
   - Power off printer
   - Wait 30 seconds
   - Power on printer
   - Wait for full startup

3. **Restart Print Spooler**
   - Windows: Run `services.msc`
   - Find Print Spooler
   - Restart service

### Paper Jam

**Symptoms:**
- Printer indicates paper jam
- Paper stuck in printer
- Cannot print

**Solutions:**

1. **Locate Jam**
   - Check all paper trays
   - Check rear access door
   - Check automatic feeder
   - Check output tray

2. **Remove Paper**
   - Gently pull paper in direction of paper path
   - Do not tear paper
   - Remove all fragments

3. **Reset Printer**
   - Open and close all doors
   - Power cycle printer
   - Test print

### Low Quality Prints

**Symptoms:**
- Faded prints
- Streaks on paper
- Smudges

**Solutions:**

1. **Check Toner/Cartidge**
   - Check toner levels
   - Replace if low
   - Shake toner cartridge to distribute

2. **Clean Printer**
   - Run printer cleaning cycle
   - Clean print heads
   - Clean rollers

3. **Check Paper**
   - Use recommended paper type
   - Ensure paper is dry
   - Check for damaged paper

### Cannot Connect to Printer

**Symptoms:**
- Cannot add printer
- Connection timeout
- Access denied

**Solutions:**

1. **Check VPN**
   - Ensure VPN is connected
   - Try different VPN server
   - Disconnect and reconnect VPN

2. **Check Firewall**
   - Temporarily disable firewall
   - Add printer IP to firewall exceptions
   - Contact IT for firewall configuration

3. **Verify IP Address**
   - Confirm correct printer IP
   - Check IP hasn't changed
   - Contact IT if IP changed

## Printing Policies

### Color Printing

- Color printing available on 2nd floor Canon only
- Use color only when necessary
- Marketing materials: approved for color
- Internal documents: black and white default
- Client presentations: approved for color

### Large Print Jobs

- Print jobs over 100 pages: notify IT in advance
- Large jobs should be printed during off-hours
- Consider print shop for very large jobs
- Contact IT for print shop coordination

### Confidential Documents

- Use secure print feature for confidential documents
- Enter PIN at printer to release job
- Never leave confidential documents at printer
- Shred confidential documents after use

### Cost Tracking

- All printing is tracked by department
- Monthly reports sent to department heads
- Excessive printing may be reviewed
- Contact IT for usage reports

## Mobile Printing

### Email to Print

**For HP and Canon printers:**

1. Compose email
2. Attach document to print
3. Send to printer email address:
   - HP: hp50@print.company.com
   - Canon: canon51@print.company.com
4. Document will print automatically

### Mobile App

**HP Smart App:**
- Download from app store
- Add printer by IP address
- Print from mobile device

**Canon PRINT Business:**
- Download from app store
- Add printer by IP address
- Print from mobile device

## Maintenance

### Regular Maintenance

- IT performs monthly maintenance
- Cleaning performed quarterly
- Toner replaced when low
- Firmware updated as needed

### User Maintenance

- Keep printer area clean
- Report issues promptly
- Use quality paper
- Do not force paper if jammed

## Getting Help

### IT Support
- Email: support@company.com
- Phone: extension 200
- For printer issues: mention "Printer" in subject

### Common Issues Resolution Time
- Paper jams: 30 minutes
- Toner replacement: 1 hour
- Connection issues: 2 hours
- Hardware issues: 4 hours

### Supplies
- Extra toner stored in supply room
- Paper available in supply room
- Contact reception for access

---

Last updated: March 2024
