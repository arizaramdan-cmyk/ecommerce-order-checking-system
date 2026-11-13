# Project Overview

**E-Commerce Order Checking System** is an independent Python demonstration of order verification logic with fictional data.

## Demonstrated capabilities

- Receipt-level order identity and SKU validation
- Per-item quantity reconciliation and excess-quantity rejection
- Statuses for not scanned, partial, completed, mismatched, and canceled orders
- One active mismatch case per order, even after repeated invalid scans
- Separate statistics for completed SKU lines and completed orders
- Automated Python `unittest` checks

## Important scope clarification

The public repository demonstrates **business logic only**. It is not a full Windows desktop application or a smartphone scanning server. Database persistence, Excel integration, camera scanning, voice guidance, user accounts, and production dashboards are possible future extensions and are not included in this demo.

All identifiers and sample marketplace labels are fictional. The repository intentionally excludes employer branding, real order data, and operational secrets.
