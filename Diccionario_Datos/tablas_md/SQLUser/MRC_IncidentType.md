# SQLUser.MRC_IncidentType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCIDT_RowId | bigint | PK |  | NO | - |
| INCIDT_Code | varchar |  |  | NO | Code |
| INCIDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCIDT_CreatedDate | date |  |  | SI | Created Date |
| INCIDT_CreatedTime | time |  |  | SI | Created Time |
| INCIDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCIDT_DateFrom | date |  |  | SI | DateFrom |
| INCIDT_DateTo | date |  |  | SI | DateTo |
| INCIDT_Desc | varchar |  |  | NO | Description |
| INCIDT_Owner | varchar |  |  | SI | Owner |
| INCIDT_UpdatedDate | date |  |  | SI | Updated Date |
| INCIDT_UpdatedTime | time |  |  | SI | Updated Time |
| INCIDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | Movimiento |
| Q01Q2 | - |  |  | SI | Tipo |
| Q01Q3 | - |  |  | SI | Segmento |
| Q01Q4 | - |  |  | SI | Lateralidad |
| Q01Q5 | - |  |  | SI | ROM |
| Q01Q6 | - |  |  | SI | Fuerza |
| Q01Q7 | - |  |  | SI | EVA |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*