# websys.License

**Schema:** websys
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ExpiryDate | date |  |  | SI | - |
| LicenseKey | varchar |  |  | SI | - |
| LicensedEprChartUsers | integer |  |  | SI | - |
| LicensedMedtrakUsers | integer |  |  | SI | - |
| LicensedOrderEntryUsers | integer |  |  | SI | - |
| LicensedRadiologyWBUsers | integer |  |  | SI | - |
| LicensedTheatreWBUsers | integer |  |  | SI | - |
| SiteCode | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*