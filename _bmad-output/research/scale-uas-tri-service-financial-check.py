"""Arithmetic check for the tri-service SCALE UAS illustrative scenario."""

from __future__ import annotations

YEARS = tuple(range(1, 11))


def calculate_scenario(
    orders: tuple[int, ...],
    deliveries: tuple[int, ...],
    aircraft_price_cr: float,
    support_rate: float,
) -> list[dict[str, float]]:
    backlog_units = 0
    fleet_units = 0
    rows: list[dict[str, float]] = []
    for year, ordered, delivered in zip(YEARS, orders, deliveries, strict=True):
        opening_fleet = fleet_units
        backlog_units += ordered - delivered
        fleet_units += delivered
        aircraft_revenue = delivered * aircraft_price_cr
        support_revenue = opening_fleet * aircraft_price_cr * support_rate
        rows.append(
            {
                "year": float(year),
                "ordered": float(ordered),
                "delivered": float(delivered),
                "fleet": float(fleet_units),
                "backlog_units": float(backlog_units),
                "aircraft_revenue_cr": aircraft_revenue,
                "support_revenue_cr": support_revenue,
                "total_revenue_cr": aircraft_revenue + support_revenue,
                "backlog_value_cr": backlog_units * aircraft_price_cr,
            }
        )
        assert backlog_units >= 0, f"negative backlog in year {year}"
    return rows


def assert_cumulative_orders_cover_deliveries(
    orders: tuple[int, ...], deliveries: tuple[int, ...]
) -> None:
    cum_o = 0
    cum_d = 0
    for year, ordered, delivered in zip(YEARS, orders, deliveries, strict=True):
        cum_o += ordered
        cum_d += delivered
        assert cum_d <= cum_o, f"deliveries exceed orders by year {year}"


def print_table(label: str, rows: list[dict[str, float]]) -> None:
    print(label)
    print(
        "Y | Ord | Del | Fleet | Back | A/C Rev | Support | Total | Back INR Cr"
    )
    for row in rows:
        print(
            f"{int(row['year']):2d} | "
            f"{int(row['ordered']):3d} | "
            f"{int(row['delivered']):3d} | "
            f"{int(row['fleet']):5d} | "
            f"{int(row['backlog_units']):4d} | "
            f"{row['aircraft_revenue_cr']:7.0f} | "
            f"{row['support_revenue_cr']:7.0f} | "
            f"{row['total_revenue_cr']:7.0f} | "
            f"{row['backlog_value_cr']:7.0f}"
        )
    print()


def main() -> None:
    price = 180.0
    support_rate = 0.10

    # Base: minority dual-award calibration (~36% of 87 ≈ 31) plus modest follow-on.
    # Totals 36 ordered / 14 delivered by Y10.
    orders = (0, 3, 3, 4, 4, 4, 4, 5, 4, 5)
    deliveries = (0, 0, 0, 1, 1, 2, 2, 2, 3, 3)
    assert len(orders) == 10 and len(deliveries) == 10
    assert_cumulative_orders_cover_deliveries(orders, deliveries)
    assert sum(orders) == 36
    assert sum(deliveries) == 14

    base = calculate_scenario(orders, deliveries, price, support_rate)
    print_table("BASE (INR 180 Cr, 10% support on opening fleet)", base)

    # Twelve-month qualification slip: shift deliveries one year right.
    slipped_deliveries = (0, 0, 0, 0, 1, 1, 2, 2, 2, 3)
    assert_cumulative_orders_cover_deliveries(orders, slipped_deliveries)
    slipped = calculate_scenario(orders, slipped_deliveries, price, support_rate)
    print_table("SLIP +12 months on first delivery", slipped)

    # Service-mix assumption for narrative only (not a tender allocation).
    # Inspired by MQ-9B contracted split proportions applied to 36 units.
    navy, army, iaf = 17, 9, 10
    assert navy + army + iaf == 36
    print(
        f"Illustrative domestic mix assumption (not sourced allocation): "
        f"Navy {navy}, Army {army}, IAF {iaf}"
    )
    print("All assertions passed.")


if __name__ == "__main__":
    main()
