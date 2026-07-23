# Operations glossary (synthetic fixture)

- `delay_minutes`: elapsed departure delay for a flight record; `0` means no recorded delay.
- `cancellation_flag`: `1` when the flight was cancelled and `0` otherwise.
- `weather_flag`: a synthetic indicator that weather was recorded as a contributing factor.
- `maintenance_flag`: a synthetic indicator that maintenance was recorded as a contributing factor.
- `turnaround_minutes`: synthetic minutes between an arriving aircraft and its next departure.

This glossary is deliberately small and is not an operational data contract. It exists to make the local evaluation reproducible.
