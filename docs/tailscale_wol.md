# Tailscale and Wake-on-LAN

## Tailscale

Install:

```powershell
winget install Tailscale.Tailscale
tailscale up
tailscale ip -4
```

Use your Tailscale IPv4 address to access the app remotely:

```text
http://[tailscale-ip]:8501
```

## Wake-on-LAN

Get your MAC address:

```powershell
ipconfig /all | findstr "Physical Address"
```

Check wake-enabled devices:

```powershell
powercfg /devicequery wake_armed
```

### BIOS
- Reboot
- Press `F2` or `Del`
- Enable **Wake on LAN**

### Phone WoL app settings
- IP: Tailscale IP
- MAC: your machine MAC address
- Port: 9
