# SQLUser.ARC_BillingSchedule

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSC_RowID | bigint | PK |  | NO | - |
| ARCBSC_Code | varchar |  |  | NO | Code |
| ARCBSC_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSC_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBSC_DateTo | date |  |  | SI | Last day the record is active |
| ARCBSC_Desc | varchar |  |  | NO | Description |
| ARCBSC_Owner | varchar |  |  | SI | Owner |
| ChildQ68DR | - |  |  | SI | Child Reference: Ojos |
| Q112Q1 | - |  |  | SI | Pulsos |
| Q112Q2 | - |  |  | SI | Lateralidad |
| Q112Q3 | - |  |  | SI | Hallazgos |
| Q112Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*