# SQLUser.ARC_InsTypePayorNotes

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYNOTE_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ39DR | - |  |  | SI | Child Reference: Orientación |
| PAYNOTE_Childsub | double |  |  | NO | Childsub |
| PAYNOTE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAYNOTE_CreatedDate | date |  |  | SI | Created Date |
| PAYNOTE_CreatedTime | time |  |  | SI | Created Time |
| PAYNOTE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAYNOTE_DateFrom | date |  |  | SI | Date From |
| PAYNOTE_DateTo | date |  |  | SI | Date To |
| PAYNOTE_PayorNotes_DR | bigint |  | FK | NO | Payor Notes |
| PAYNOTE_RowId | varchar |  |  | NO | - |
| PAYNOTE_UpdatedDate | date |  |  | SI | Updated Date |
| PAYNOTE_UpdatedTime | time |  |  | SI | Updated Time |
| PAYNOTE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q20Q1 | - |  |  | SI | Área |
| Q20Q2 | - |  |  | SI | Evaluación |
| Q20Q3 | - |  |  | SI | Observaciones (texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*