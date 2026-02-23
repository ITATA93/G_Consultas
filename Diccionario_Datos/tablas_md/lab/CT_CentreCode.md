# lab.CT_CentreCode

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCC_RowId | varchar | PK |  | NO | - |
| CTCC_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTCC_Address | varchar |  |  | SI | Address |
| CTCC_Address1 | varchar |  |  | SI | Address 1 |
| CTCC_Address2 | varchar |  |  | SI | Address 2 |
| CTCC_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTCC_Address4_State | varchar |  |  | SI | State |
| CTCC_Address5_PostCode | varchar |  |  | SI | PostCode |
| CTCC_Code | varchar |  |  | NO | Code |
| CTCC_Desc | varchar |  |  | SI | Name |
| CTCC_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTCC_LicenceChange | date |  |  | SI | Licence Change |
| CTCC_LicenceNumber | varchar |  |  | SI | Licence Number |
| CTCC_OldLicenceNo | varchar |  |  | SI | Old Licence No |
| CTCC_Phone | varchar |  |  | SI | Phone |
| CTCC_SCPType_DR | varchar |  | FK | SI | SCP Type DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*