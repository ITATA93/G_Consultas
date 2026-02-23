# SQLUser.CT_LocExtAvailable

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLEA_RowId | bigint | PK |  | NO | - |
| CTLEA_Code | varchar |  |  | NO | Code |
| CTLEA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTLEA_CreatedDate | date |  |  | SI | Created Date |
| CTLEA_CreatedTime | time |  |  | SI | Created Time |
| CTLEA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTLEA_DateFrom | date |  |  | SI | Date From |
| CTLEA_DateTo | date |  |  | SI | Date To |
| CTLEA_Desc | varchar |  |  | NO | Description |
| CTLEA_Owner | varchar |  |  | SI | Owner |
| CTLEA_UpdatedDate | date |  |  | SI | Updated Date |
| CTLEA_UpdatedTime | time |  |  | SI | Updated Time |
| CTLEA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ42DR | - |  |  | SI | Child Reference: ETT re-positioning detail |
| Q32Q1 | - |  |  | SI | Airway device |
| Q32Q2 | - |  |  | SI | Device size |
| Q32Q3 | - |  |  | SI | Laryngoscope |
| Q32Q4 | - |  |  | SI | Blade details |
| Q32Q5 | - |  |  | SI | Grade of view |
| Q32Q6 | - |  |  | SI | Airway adjuncts |
| Q32Q7 | - |  |  | SI | Insertion location |
| Q32Q8 | - |  |  | SI | Notes |
| Q32Q9 | - |  |  | SI | Attempted by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*