# VPN Setup Guide

## Overview

This guide provides step-by-step instructions for setting up and using the company VPN (Virtual Private Network). All remote work and access to internal resources requires VPN connection.

## Prerequisites

- Company laptop or approved personal device
- Active employee account
- VPN client software (download from IT portal)
- Authentication token (provided by IT)

## Installation

### Windows

1. Download the VPN client from the IT portal (https://it.company.com/vpn)
2. Run the installer: `CompanyVPN_Setup.exe`
3. Follow the installation wizard:
   - Accept license agreement
   - Choose installation location (default recommended)
   - Complete installation
4. Restart your computer

### macOS

1. Download the VPN client from the IT portal
2. Open the downloaded `.dmg` file
3. Drag the CompanyVPN app to Applications folder
4. Launch the app from Applications

### Linux

```bash
# Download the package
wget https://it.company.com/vpn/company-vpn-linux.deb

# Install
sudo dpkg -i company-vpn-linux.deb

# Start the service
sudo systemctl start company-vpn
```

## Configuration

### First-Time Setup

1. Launch the VPN client
2. Enter the server address: `vpn.company.com`
3. Enter your username (employee email)
4. Enter your authentication token (from IT)
5. Click "Connect"

### Saving Credentials

- For convenience, you can save your credentials
- Check "Remember me" option
- Credentials are encrypted locally
- Never share your authentication token

## Usage

### Connecting to VPN

1. Launch the VPN client
2. Click "Connect"
3. Enter your password if prompted
4. Wait for connection confirmation (green indicator)
5. You now have access to internal resources

### Disconnecting

1. Click "Disconnect" in the VPN client
2. Wait for disconnection confirmation
3. Close the client if desired

### Auto-Connect

- Enable auto-connect on startup for convenience
- Settings > General > Auto-connect on startup
- Recommended for remote workers

## Troubleshooting

### Connection Failed

**Error: "Authentication failed"**
- Verify username and password
- Check authentication token expiration
- Contact IT if token is expired

**Error: "Server not reachable"**
- Check internet connection
- Verify server address: `vpn.company.com`
- Try alternative server: `vpn-backup.company.com`

**Error: "Connection timeout"**
- Check firewall settings
- Disable other VPN services
- Restart the VPN client

### Slow Performance

**Symptoms:**
- Slow file transfers
- Lag in remote desktop
- Poor video call quality

**Solutions:**
- Check internet speed (minimum 10 Mbps required)
- Connect to wired network instead of Wi-Fi
- Close bandwidth-intensive applications
- Try connecting to different VPN server region

### Split Tunneling

Split tunneling allows you to access both internal and external resources simultaneously.

**To enable:**
1. Go to Settings > Network
2. Enable "Split Tunneling"
3. Add internal network ranges:
   - `10.0.0.0/8`
   - `172.16.0.0/12`
   - `192.168.0.0/16`

## Security Best Practices

### Password Security
- Never share your VPN password
- Change password every 90 days
- Use strong passwords (minimum 12 characters)

### Token Security
- Keep authentication token secure
- Report lost tokens immediately to IT
- Never store token in plain text

### Public Wi-Fi
- Always use VPN on public Wi-Fi
- Disable file sharing on public networks
- Use company device when possible

## Supported Resources

### Internal Websites
- Company intranet: `intranet.company.com`
- HR portal: `hr.company.com`
- Project management: `projects.company.com`

### File Servers
- Shared drives: `\\fileserver.company.com`
- Department folders: `\\fileserver.company.com\departments`
- Personal folders: `\\fileserver.company.com\home\username`

### Applications
- Remote desktop: `rdp.company.com`
- Database access: `db.company.com`
- Development servers: `dev.company.com`

## Access Policies

### Access Hours
- VPN access available 24/7
- Maintenance windows: Sundays 2:00 AM - 4:00 AM
- Planned downtime announced via email

### Data Transfer
- No PII (Personally Identifiable Information) over VPN without encryption
- Maximum file size: 2 GB per transfer
- Use approved file transfer methods for large files

### Compliance
- All VPN traffic is logged
- Security audits conducted quarterly
- Violations may result in access revocation

## Getting Help

### IT Help Desk
- Email: support@company.com
- Phone: extension 200
- Hours: 24/7 for VPN issues

### Common Issues Resolution Time
- Authentication issues: 1 hour
- Connection problems: 2 hours
- Performance issues: 4 hours
- Configuration issues: 2 hours

### Emergency Contact
- For critical VPN outages: 555-0123 (24/7 hotline)

## Updates

### Client Updates
- Automatic updates enabled by default
- Update notifications sent via email
- Manual update available from IT portal

### Policy Updates
- VPN policy reviewed annually
- Changes communicated via email
- Training provided for major changes

---

Last updated: March 2024
