# SQLUser.PAC_ServiceAgreementProcedure

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROC_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| ChildQ06DR | - |  |  | SI | Child Reference: Day 4 |
| PROC_Childsub | double |  |  | NO | Childsub |
| PROC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROC_CreatedDate | date |  |  | SI | Created Date |
| PROC_CreatedTime | time |  |  | SI | Created Time |
| PROC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROC_Procedure_DR | bigint |  | FK | SI | Des Ref Procedure |
| PROC_RowId | varchar |  |  | NO | - |
| PROC_UpdatedDate | date |  |  | SI | Updated Date |
| PROC_UpdatedTime | time |  |  | SI | Updated Time |
| PROC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | Insertion date / time |
| Q01Q10 | - |  |  | SI | Nurse / Clinician |
| Q01Q2 | - |  |  | SI | Insertion time |
| Q01Q3 | - |  |  | SI | Day/Shift |
| Q01Q4 | - |  |  | SI | Visual Infusion Phlebitis (VIP) Score |
| Q01Q5 | - |  |  | SI | Site visible |
| Q01Q6 | - |  |  | SI | Dressing intact / clean / dated? |
| Q01Q7 | - |  |  | SI | Moisture / Leak from site |
| Q01Q8 | - |  |  | SI | Flow problems / flushed |
| Q01Q9 | - |  |  | SI | Needle-free device / extension in situ |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*