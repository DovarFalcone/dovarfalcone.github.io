---
layout: post
title: Real HTTPS Names for Self-Hosted Apps
subtitle: For when your router won't do local DNS
category: Project
tags: [Home Lab, HTTPS, Tailscale, Cloudflare, Docker]
comments: true
topic: homelab
---

This is a walkthrough for anyone stuck with an ISP router (Verizon Fios and similar) that won't let you add local DNS records. When you're done:

- `https://grafana.home.example.com` (and any other app) works at home with a valid certificate.
- The same name works away from home through Tailscale.
- Nothing is opened to the internet, and the router's DNS settings stay untouched.

## Placeholders

Replace these everywhere in the steps below.

| Placeholder | Meaning |
| --- | --- |
| `example.com` | your domain, with DNS on Cloudflare |
| `192.168.1.0/24` | your home network (Fios default) |
| `192.168.1.10` | the always-on machine that will run the proxy |
| `192.168.1.20:3000` | an example app (the IP:port you use today) |

## What you need

- A domain whose DNS is hosted on Cloudflare. The free plan is fine.
- One always-on Linux machine with Docker and Docker Compose. A mini PC or a NAS works. Avoid a Raspberry Pi 3, which is too slow for step 7: it handled about 234 Mbit/s through Tailscale, versus about 851 Mbit/s on a mini PC.
- A free Tailscale account, plus the Tailscale app on your phone and laptop.

<!-- STEPS PENDING: waiting on the rest of Dennis's walkthrough -->
