# SQLUser.BLC_LongStayDiscount

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LONGSD_RowId | bigint | PK |  | NO | - |
| ChildQ16DR | - |  |  | SI | Child Reference: OTROS |
| LONGSD_CreatedDate | date |  |  | SI | Created Date |
| LONGSD_CreatedTime | time |  |  | SI | Created Time |
| LONGSD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LONGSD_DayFrom | double |  |  | SI | Day From |
| LONGSD_DayTo | double |  |  | SI | Day To |
| LONGSD_InsType_DR | bigint |  | FK | SI | Des Ref to InsType_DR |
| LONGSD_Perc | double |  |  | SI | % Discount |
| LONGSD_UpdatedDate | date |  |  | SI | Updated Date |
| LONGSD_UpdatedTime | time |  |  | SI | Updated Time |
| LONGSD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q06Q1 | - |  |  | SI | Objetivos |
| Q06Q2 | - |  |  | SI | Estrategias o Actividades |
| Q06Q3 | - |  |  | SI | Responsables |
| Q06Q4 | - |  |  | SI | Plazo |
| Q06Q5 | - |  |  | SI | Indicador de Logro |
| Q06Q6 | - |  |  | SI | Cumplimiento |
| Q06Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*