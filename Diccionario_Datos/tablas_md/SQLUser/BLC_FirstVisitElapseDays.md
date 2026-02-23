# SQLUser.BLC_FirstVisitElapseDays

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FVED_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: Antecedentes de su Red |
| FVED_CreatedDate | date |  |  | SI | Created Date |
| FVED_CreatedTime | time |  |  | SI | Created Time |
| FVED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FVED_DateFrom | date |  |  | NO | Date From |
| FVED_DateTo | date |  |  | SI | Date To |
| FVED_ElapsedDays | numeric |  |  | NO | Elapsed Days |
| FVED_UpdatedDate | date |  |  | SI | Updated Date |
| FVED_UpdatedTime | time |  |  | SI | Updated Time |
| FVED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Gestor Terapéutico |
| Q09Q2 | - |  |  | SI | OBJETIVO TERAPEUTICO |
| Q09Q3 | - |  |  | SI | ACTIVIDAD |
| Q09Q4 | - |  |  | SI | A QUIEN VA DIRIGIDO |
| Q09Q5 | - |  |  | SI | QUIEN LO REALIZA |
| Q09Q6 | - |  |  | SI | PLAZOS |
| Q09Q7 | - |  |  | SI | CUMPLIMIENTO |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*