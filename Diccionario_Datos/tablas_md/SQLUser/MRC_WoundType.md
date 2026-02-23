# SQLUser.MRC_WoundType

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WT_RowId | bigint | PK |  | NO | - |
| Q04Q10 | - |  |  | SI | Servicio Clínico |
| Q04Q11 | - |  |  | SI | Recibió Alimentación Asistida |
| Q04Q5 | - |  |  | SI | Turno Mañana 08:00 a 14:00 |
| Q04Q6 | - |  |  | SI | Turno Tarde 14:00 a 20:00 |
| Q04Q7 | - |  |  | SI | Turno Noche 20:00 a 08:00 |
| Q04Q8 | - |  |  | SI | Nombre del Cuidador |
| Q04Q9 | - |  |  | SI | Fecha |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WT_Code | varchar |  |  | NO | Code |
| WT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WT_CreatedDate | date |  |  | SI | Created Date |
| WT_CreatedTime | time |  |  | SI | Created Time |
| WT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WT_Desc | varchar |  |  | NO | Description |
| WT_Owner | varchar |  |  | SI | Owner |
| WT_UpdatedDate | date |  |  | SI | Updated Date |
| WT_UpdatedTime | time |  |  | SI | Updated Time |
| WT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*