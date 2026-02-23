# SQLUser.SS_ExternalData

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| SSEXD_ClassName | varchar |  |  | SI | Class Name  |
| SSEXD_EnteredLocation | varchar |  |  | SI | Entered Location
Stored as a string because the l... |
| SSEXD_EnteredUser | varchar |  |  | SI | Entered User
Stored as a string because the user ... |
| SSEXD_Object_DR | varchar |  | FK | NO | Object Reference |
| SSEXD_ReadOnly | bit |  |  | NO | Read Only
The record is not managed by TrakCare. ... |
| SSEXD_RowID | varchar |  |  | SI | Row ID  |
| SSEXD_SendingFacility | varchar |  |  | SI | Sending Facility |
| SSEXD_SendingFacilityCode | varchar |  |  | SI | Sending Facility Code
The external facility code ... |
| SSEXD_SendingIdentifier | varchar |  |  | SI | Sending Identifier
The unique record ID from the ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*