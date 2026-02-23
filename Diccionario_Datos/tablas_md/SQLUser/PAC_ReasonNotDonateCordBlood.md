# SQLUser.PAC_ReasonNotDonateCordBlood

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REANDCB_RowId | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Verbal Disruption |
| Q01Q1 | - |  |  | SI | Date |
| Q01Q2 | - |  |  | SI | Time |
| Q01Q3 | - |  |  | SI | Behaviour |
| Q01Q4 | - |  |  | SI | What happened before |
| Q01Q5 | - |  |  | SI | What happened next |
| Q01Q6 | - |  |  | SI | Is the person sleeping (record times) |
| Q01Q7 | - |  |  | SI | Persons present |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REANDCB_Code | varchar |  |  | NO | Code |
| REANDCB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REANDCB_CreatedDate | date |  |  | SI | Created Date |
| REANDCB_CreatedTime | time |  |  | SI | Created Time |
| REANDCB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REANDCB_DateFrom | date |  |  | SI | Date From |
| REANDCB_DateTo | date |  |  | SI | Date To |
| REANDCB_Desc | varchar |  |  | NO | Description |
| REANDCB_Owner | varchar |  |  | SI | Owner |
| REANDCB_UpdatedDate | date |  |  | SI | Updated Date |
| REANDCB_UpdatedTime | time |  |  | SI | Updated Time |
| REANDCB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*