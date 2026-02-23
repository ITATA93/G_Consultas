# SQLUser.PH_Distributor

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia**. Dispensación de medicamentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHDIS_RowId | bigint | PK |  | NO | - |
| PHDIS_Address | varchar |  |  | SI | Address |
| PHDIS_Code | varchar |  |  | NO | Distributor Code |
| PHDIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHDIS_Name | varchar |  |  | SI | Distributor Name |
| PHDIS_Owner | varchar |  |  | SI | Owner |
| PHDIS_Tel | varchar |  |  | SI | Contact Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*