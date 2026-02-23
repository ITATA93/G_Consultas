# SQLUser.PAC_RefDoctorSubstitute

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBS_ParRef | bigint | PK |  | NO | PAC_RefDoctor Parent Reference |
| ChildQ8DR | - |  |  | SI | Child Reference: Nasal swab |
| Q7Q1 | - |  |  | SI | Date |
| Q7Q2 | - |  |  | SI | Transport classification |
| Q7Q3 | - |  |  | SI | 24 hour urine volume, Residual Renal Function (RRF... |
| Q7Q4 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUBS_Childsub | double |  |  | NO | Childsub |
| SUBS_CreatedDate | date |  |  | SI | Created Date |
| SUBS_CreatedTime | time |  |  | SI | Created Time |
| SUBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBS_DateFrom | date |  |  | SI | Date From |
| SUBS_DateTo | date |  |  | SI | Date To |
| SUBS_RefDoctor_DR | bigint |  | FK | SI | Des Ref RefDoctor |
| SUBS_RowId | varchar |  |  | NO | - |
| SUBS_UpdatedDate | date |  |  | SI | Updated Date |
| SUBS_UpdatedTime | time |  |  | SI | Updated Time |
| SUBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*