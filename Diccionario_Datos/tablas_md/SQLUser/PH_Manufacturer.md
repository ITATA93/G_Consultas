# SQLUser.PH_Manufacturer

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia**. Dispensación de medicamentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHMNF_RowId | bigint | PK |  | NO | - |
| PHMNF_Address | varchar |  |  | SI | Address |
| PHMNF_Code | varchar |  |  | NO | Manufacturer Code |
| PHMNF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHMNF_Name | varchar |  |  | SI | Manufacturer Name |
| PHMNF_Owner | varchar |  |  | SI | Owner |
| PHMNF_Tel | varchar |  |  | SI | Contact Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*