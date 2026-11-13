"""Independent portfolio demonstration. Synthetic orders only; no company code/data."""

from dataclasses import dataclass, field
from collections import Counter


@dataclass
class Order:
    receipt: str
    marketplace: str
    requested: dict[str, int]
    checked: Counter = field(default_factory=Counter)
    mismatched: bool = False
    cancelled: str | None = None

    @property
    def complete(self) -> bool:
        return not self.cancelled and all(
            self.checked[sku] >= qty for sku, qty in self.requested.items()
        )

    @property
    def status(self) -> str:
        if self.cancelled:
            return self.cancelled
        if self.complete:
            return "SUDAH SCAN"
        if self.mismatched:
            return "TIDAK MATCH"
        if any(self.checked.values()):
            return "SEBAGIAN"
        return "BELUM SCAN"

    def scan(self, sku: str) -> str:
        if self.cancelled:
            return "PESANAN CANCEL"
        if sku not in self.requested:
            self.mismatched = True  # one receipt, one outstanding mismatch
            return "SALAH ARTIKEL"
        if self.checked[sku] >= self.requested[sku]:
            return "QTY LEBIH"
        self.checked[sku] += 1
        self.mismatched = False
        return "COCOK"


def totals(orders: list[Order]) -> dict[str, int]:
    return {
        "resi_total": len(orders),
        "resi_selesai": sum(order.complete for order in orders),
        "baris_selesai": sum(
            order.checked[sku] >= qty
            for order in orders if not order.cancelled
            for sku, qty in order.requested.items()
        ),
        "tidak_match": sum(order.mismatched for order in orders if not order.cancelled),
    }


def sample_orders() -> list[Order]:
    return [
        Order("DEMO-001", "Marketplace A", {"SKU-A-40": 2, "SKU-B-41": 1}),
        Order("DEMO-002", "Marketplace B", {"SKU-C-39": 1}),
        Order("DEMO-003", "Marketplace C", {"SKU-D-42": 1}, cancelled="CANCEL CUSTOMER"),
    ]


def main():
    orders = sample_orders()
    print("=== DEMO CHECKING E-COMMERCE ===")
    print("Resi:", orders[0].receipt)
    for sku in ("SKU-TIDAK-ADA", "SKU-TIDAK-ADA", "SKU-A-40", "SKU-A-40", "SKU-B-41"):
        print(f"  Scan {sku}: {orders[0].scan(sku)} → {orders[0].status}")
    print("Statistik:", totals(orders))


if __name__ == "__main__":
    main()
